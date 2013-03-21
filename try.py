#!/usr/bin/python3

import getpass
import sys


sys.path.append("/cs/faculty/pconrad/github/github-acadwf-scripts/PyGithub");

from github import Github

print("Password: ",end='')

pw = getpass.getpass()

g = Github("pconrad", pw)
  

for repo in g.get_user().get_repos():
    print (repo.name)

