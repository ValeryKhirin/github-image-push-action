#!/usr/bin/python3

import sys
from github import Github

# Get the repository name from the command line arguments
repo_name = sys.argv[1]

# Set up the GitHub API client
access_token = "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"
g = Github(access_token)

# Get the repository
repo = g.get_repo(repo_name)

# Get the default branch and its merge commit SHA
default_branch = repo.default_branch
merge_commit_sha = repo.get_branch(default_branch).commit.commit.tree.sha


# Get the contents of the .github/workflows folder
workflows = repo.get_contents(".github/workflows")

# Check if any of the contents of the folder have changed
folder_changed = False
changed_files = []
for item in workflows:
    if item.sha != merge_commit_sha:
        folder_changed = True
        changed_files.append(item.path)

# Print a message indicating whether or not changes were detected, and show what changed
if folder_changed:
    print("Changes were detected in the .github/workflows folder:")
    for file_path in changed_files:
        file = repo.get_contents(file_path)
        previous_commit = repo.get_commits(path=file_path, sha=default_branch)[0]
        diff = repo.compare(previous_commit.sha, file.sha).diff_url
        print(f"\nChanges in {file_path}: {diff}\n")

        # Parse the YAML content
        content = file.decoded_content.decode("utf-8")
        data = yaml.safe_load(content)

        # Print the changes in the YAML content
        previous_content = repo.get_contents(path=file_path, ref=previous_commit.sha).decoded_content.decode("utf-8")
        previous_data = yaml.safe_load(previous_content)
        print("Changes in the YAML content:")
        for key in data.keys():
            if key not in previous_data.keys() or data[key] != previous_data[key]:
                print(f"{key}: {previous_data.get(key, '')} -> {data[key]}")
else:
    print("No changes were detected in the .github/workflows folder since the last merge.")
