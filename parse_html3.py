import re

with open("ui/cloudbrains/index.html", "r", encoding="utf-8") as f:
    layout_html = f.read()

with open("/tmp/file_attachments/OpenI - 启智AI开源社区提供普惠算力！/index.html", "r", encoding="utf-8") as f:
    old_html = f.read()

# Using find instead of regex to guarantee extraction of the entire container
start_str = '<div data-v-426e9c7c="" class="ai-task-create-global-c">'
start_idx = old_html.find(start_str)
if start_idx != -1:
    # Need to match the closing div for `<div data-v-426e9c7c="" class="ai-task-create-global-c">`
    # A simple way to get it is finding where the page script starts, or finding the next major structural block.
    # We can also just count div tags to find the closing div.
    div_count = 0
    end_idx = -1
    for i in range(start_idx, len(old_html)):
        if old_html.startswith('<div', i):
            div_count += 1
        elif old_html.startswith('</div', i):
            div_count -= 1
            if div_count == 0:
                end_idx = i + 6
                break

    if end_idx != -1:
        form_content = old_html[start_idx:end_idx]
    else:
        print("Failed to find end of div")
        exit(1)
else:
    print("Could not find start of div")
    exit(1)

# Now inject it back just like before
main_start = layout_html.find('<main class="main">')
main_end = layout_html.find('</main>')

pagehead_match = re.search(r'(<div class="pagehead">.*?</div>\s*</div>)', layout_html, re.DOTALL)
pagehead = ""
if pagehead_match:
    pagehead = pagehead_match.group(1)
    pagehead = pagehead.replace('<h1>计算任务</h1>', '<h1>新建计算任务</h1>')
    pagehead = re.sub(r'<div class="pagehead__actions">.*?</div>', '', pagehead, flags=re.DOTALL)
    pagehead = pagehead.replace('<b>工作台</b> <span>/</span> 计算任务', '<b>工作台</b> <span>/</span> <a href="/cloudbrains" style="color:inherit;text-decoration:none;">计算任务</a> <span>/</span> 新建计算任务')

new_main_content = f'\n    {pagehead}\n\n    <div class="create-form-wrap">\n      {form_content}\n    </div>\n  '
new_layout_html = layout_html[:main_start + len('<main class="main">')] + new_main_content + layout_html[main_end:]

with open("ui/cloudbrains/create/index.html", "w", encoding="utf-8") as f:
    f.write(new_layout_html)

print("Merged successfully.")
