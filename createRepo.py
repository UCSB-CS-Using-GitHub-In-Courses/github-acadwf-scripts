#!/usr/bin/python

import getpass
import sys


sys.path.append("/cs/faculty/pconrad/github/github-acadwf-scripts/PyGithub");

from github import Github



user = raw_input("Github Username:")
pw = getpass.getpass()

g = Github(user, pw)

org = g.get_organization("UCSB-CS56-S13")
  
org.create_repo(
    "lab00_Conrad", # name -- string
    "lab00 for CS56 for Conrad", # description -- string
    "", # homepage -- string
    True, # private -- bool
    True, # has_issues -- bool
    True, # has_wiki -- bool
    True, # has_downloads -- bool
    auto_init=True,
    gitignore_template="Java")

  #  NotSet, # team_id -- github.Team.Team
  #  True, # auto_init -- bool
  #  "Java") # gitignore_template -- string

