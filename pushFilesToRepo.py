#!/usr/bin/python

# This script takes a lab number such as lab00 as the command line argument,
# and tries to update all of the lab00_* repos in the 
# UCSB-CS56-S13 organization by deleting all files in the repo currently,
# and replacing them with all files from those under the directory
# lab00_prototype
#

import getpass

import sys

import argparse

import os

PyGitHubLocs = ["/cs/faculty/pconrad/github/github-acadwf-scripts/PyGithub",
                "./PyGithub"]
#  "/Users/pconrad/github/github-acadwf-scripts/PyGithub"]

for loc in PyGitHubLocs:
    if os.path.isdir(loc):
        print("Adding " + loc + " to sys.path")
        sys.path.append(loc)

from github import Github
from github import GithubException


def populateRepo(repo):
    print("Populating repo " + repo.name)


def find_team(org,teamName):

    teams = org.get_teams();
    for team in teams:
        if team.name == teamName:
            return team
    return False



def locateGithubUser(githubUserIdString):
    ## REFACTOR THIS INTO FUNCTION common to both this and other scripts

    try:
        user = g.get_user(githubUserIdString)
        if (user == None):
            print("No such github user: ",githubUserIdString)
            return False
        else:
            print("Found user: " + user.login);
            return user

    except GithubException as e:
        print("No such github user: " + githubUserIdString) 
        print(e)
        return False




parser = argparse.ArgumentParser(description='push files from labxx_prototype directory to labxx_* repos')

parser.add_argument('lab',metavar='labxx',  
                    help="which lab (e.g. lab00, lab01, etc.)")

parser.add_argument('-f','--firstName', 
                    help="if passed, only update labxx_FirstName",
                    default="")

parser.add_argument('-u','--githubUsername', 
                    help="github username, default is current OS user",
                    default=getpass.getuser())

args = parser.parse_args()


pw = getpass.getpass()

g = Github(args.githubUsername, pw)

org = g.get_organization("UCSB-CS56-S13")

protoDirName = args.lab + "_prototype"

# check to see if protoDirName exists.  If not, bail

if (not os.path.isdir(protoDirName)):
    raise Exception(protoDirName + " does not exist.")


if (args.firstName!=""):
    try:
        repoName = (args.lab + "_" + args.firstName)
        repo = org.get_repo(repoName)
        populateRepo(repo)
    except GithubException as ghe:
        print("Could not find repo " + repoName + ":" + str(ghe))

else:
       
    # User wants to update ALL repos that start with labxx_

    repos = org.get_repos()
    for repo in repos:
        if (repo.name.startswith(args.lab+"_")):
            populateRepo(repo)
            




