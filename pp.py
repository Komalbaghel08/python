import os
from datetime import datetime

# commit message with time
commit_message = f"Auto commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# git commands
commands = [
    "git add .",
    f'git commit -m "{commit_message}"',
    "git push"
]

# run commands
for command in commands:
    os.system(command)

print("✅ Code pushed to GitHub successfully!")