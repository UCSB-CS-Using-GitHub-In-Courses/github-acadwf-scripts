#!/usr/bin/python

# This script reads all the users from the CSV file created
# by the Google Form.

# If first checks for any duplicate first names.  If there are duplicate
# first names, it deambiguates the first names by adding first letters of
# the last name until the names are distinguished.

# It then:
#  (1) checks if the github user exists (bails, if not)
#  (2) creates the Student_FirstName team (if not already there)
#  (3) adds the github user to the Student_FirstName team and AllStudents team


import getpass

import sys

import argparse


from disambiguateFunctions import makeUserDict
from disambiguateFunctions import disambiguateAllFirstNames
from disambiguateFunctions import getUserList

sys.path.append("/cs/faculty/pconrad/github/github-acadwf-scripts/PyGithub");

from github import Github
from github import GithubException


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
        print(e)
        print("No such github user: ",githubUserIdString);
        return False


def createRepo(labNumber,githubUserObject,githubTeamObject, firstName,csil):

    ## REFACTOR INTO FUNCTION THAT TAKES lab00 as parameter

    desc = "Github repo for " + labNumber + " for " + firstName

    repoName =            labNumber + "_" + firstName  # name -- string


    try:  
        repo = org.create_repo(
            repoName,
            labNumber + " for CS56, S13 for " + firstName, # description 
            "http://www.cs.ucsb.edu/~" + csil, # homepage -- string
            True, # private -- bool
            True, # has_issues -- bool
            True, # has_wiki -- bool
            True, # has_downloads -- bool
            team_id=githubTeamObject,
            auto_init=True,
            gitignore_template="Java")
    except GithubException as e:
       print (e)

    
    

def processLine(lastName,firstName,githubUser,umail,csil):
    print(firstName + "\t" + lastName + "\t" + githubUser);
    
    githubUserObject = locateGithubUser(githubUser)

    if (githubUserObject == False):
        print("ERROR: could not find github user: " + githubUser);
        return

    teamName =             "Student_" + firstName  # name -- string

    githubTeamObject = find_team(org,teamName);

    if (githubTeamObject == False):
        print("ERROR: could not find team: " + teamName);
        return
    
    createRepo("lab00",githubUserObject,githubTeamObject,firstName,csil)


username = raw_input("Github Username:")
pw = getpass.getpass()

g = Github(username, pw)

org = g.get_organization("UCSB-CS56-S13")

                      
defaultInputFilename =  '../CS56-S13-data/CS56 S13 Github Userids (Responses) - Form Responses.csv'

parser = argparse.ArgumentParser(description='Disambiguate First Names.')
parser.add_argument('-i','--infileName',
                    help='input file (default: ' + defaultInputFilename+"'",
                    default=defaultInputFilename)

args = parser.parse_args()

userList = getUserList(args.infileName)

for line in userList:
    processLine(line['last'],line['first'],line['github'],line['email'],line['csil'])
        








