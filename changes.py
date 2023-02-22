#!/usr/bin/python3
####
import sys
from github import Github
import os
import re

repo_name = sys.argv[1]
access_token = os.environ.get('ACCESS_TOKEN')
regex = re.compile("^\.github\/workflows\/.+\.ya?ml$")
there_is_a_change = False

g = Github(access_token)

repo = g.get_repo(repo_name)
pulls = repo.get_pulls(state='closed')
i = 0
while not pulls.get_page(0)[i].merged:
    i += 1  
pr = repo.get_pull(pulls.get_page(0)[i].number)

commits = pr.get_commits()
for commit in commits:
    files = commit.files
    for file in files:
        filename = file.filename
        contents = repo.get_contents(filename, ref=commit.sha).decoded_content
        if regex.match(filename):
            there_is_a_change = True
            print("There was a change in the YAML file --> " + filename + " since the last merge")
            print("The last merge was on pull request number: " + str(pr.number))

if not there_is_a_change:
    print("There was no change in the YAML file since the last merge!")
    print("The last merge was on pull request number: " + str(pr.number))

