import re

with open("ui/cloudbrains/create.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update CSS for a wider and more consistent form
css_update = """
.ai-task-create-global-c .task-items-c {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}
.ai-task-create-global-c .task-item {
  border: 1px solid var(--border-2);
  background: var(--bg-2);
  padding: 16px 20px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
  flex: 1;
  min-width: 140px;
  max-width: 180px;
}
.ai-task-create-global-c .create-task-warp {
  max-width: 1200px;
  margin-top: 20px;
}
"""

html = html.replace('</style>', css_update + '\n</style>')

with open("ui/cloudbrains/create.html", "w", encoding="utf-8") as f:
    f.write(html)
