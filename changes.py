import os
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
for item in workflows:
    if item.sha != repo.get_commit(repo.default_branch).commit.tree.sha:
        folder_changed = True
        break

# Print a message indicating if the folder has changed or not
if folder_changed:
    print("There were changes in .github/workflows folder.")

    # Get the contents of the folder at the latest commit
    latest_contents = repo.get_contents(".github/workflows", ref=repo.default_branch)

    # Compare the contents of the folder at the latest commit to the current contents
    for item in latest_contents:
        if item.sha != item.sha:
            print(f"{item.path} has changed.")
else:
    print("There were no changes in .github/workflows folder.")

