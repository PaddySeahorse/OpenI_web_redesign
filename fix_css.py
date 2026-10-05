import re

with open("ui/cloudbrains/create/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Ah! The regex that extracted `form_content` was too greedy or too strict and it cut off right after the `task-items-c` row!
