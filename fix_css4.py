import re

with open("ui/cloudbrains/create.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add a little top margin to the wrapper so that the topnav doesn't overlap the new pagehead!
# Also fix the top padding/margin for the whole page.
css_update = """
.shell {
  padding-top: var(--nav-h);
}
"""

html = html.replace('</style>', css_update + '\n</style>')

with open("ui/cloudbrains/create.html", "w", encoding="utf-8") as f:
    f.write(html)
