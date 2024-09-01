import os

# set git_path to the current working directory
# (this is the directory where the .git folder is located)
git_path = os.getcwd()

# Attempt to list the directory (simulate the Docker environment issue)
with os.popen(f'ls {git_path}') as f:
    f.read()

# Check git's opinion about the origin.
cmd = f'cd {git_path} && git config --get remote.origin.url'
with os.popen(cmd) as p:
    repo_url = p.read().strip()

if not repo_url:
    raise ValueError("No remote origin URL found in the Git configuration.")

repo_split = repo_url.split('/')
repo_name = ''
while not repo_name and repo_split:
    repo_name = repo_split.pop()

if not repo_name:
    raise ValueError("Failed to determine the repository name from the URL.")

if not repo_split:
    raise ValueError("Failed to determine the repository user from the URL.")

repo_user = repo_split.pop()

s1 = repo_user.split('/')[-1]
s2 = repo_user.split(':')[-1]
repo_user = s1 if len(s1) < len(s2) else s2

print(f"Repository User: {repo_user}")
print(f"Repository Name: {repo_name}")
