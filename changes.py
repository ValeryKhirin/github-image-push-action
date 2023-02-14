import sys
from github import Github

# Get the repository name from the command line arguments
repo_name = sys.argv[1]

# Set up the GitHub API client
access_token = "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"
g = Github(access_token)

# Get the repository
repo = g.get_repo(repo_name)

# Get the contents of the .github/workflows folder
workflows = repo.get_contents(".github/workflows")

# Check if any of the contents of the folder have changed
folder_changed = False
changed_files = []
for item in workflows:
    if item.sha != repo.get_commit(repo.default_branch).commit.tree.sha:
        folder_changed = True
        changed_files.append(item.path)

# Print a message indicating whether or not changes were detected, and show what changed
if folder_changed:
    print("Changes were detected in the .github/workflows folder:")
    print('\n'.join(changed_files))
else:
    print("No changes were detected in the .github/workflows folder.")

