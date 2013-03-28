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

from __future__ import print_function

import getpass

import sys

import argparse


from disambiguateFunctions import makeUserDict
from disambiguateFunctions import disambiguateAllFirstNames
from disambiguateFunctions import getUserList

sys.path.append("./PyGithub");

from github import Github
from github import GithubException

from find_team import find_team

#def find_team(org,teamName):
#
#    teams = org.get_teams();
#    for team in teams:
#        if team.name == teamName:
#            return team
#    return False



def locateGithubUser(githubUserIdString):
    ## REFACTOR THIS INTO FUNCTION common to both this and other scripts

    try:
        user = g.get_user(githubUserIdString)
        if (user == None):
            print("No such github user: ",githubUserIdString)
            return False
        else:
            print(" found user: " + user.login,end='');
            return user

    except GithubException as e:
        print("No such github user: ",githubUserIdString);
        return False


def createRepo(labNumber,githubUserObject,githubTeamObject, firstName,csil):

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
        print(" Created repo "+repoName)
    except GithubException as e:
       if e.data['errors'][0]['message']=='name already exists on this account':
           print(" repo {0} already exists".format(repoName))
       else:
           print (e)


def processLine(lab,lastName,firstName,githubUser,umail,csil):
    print(firstName + "\t" + lastName + "\t" + githubUser);
    
    githubUserObject = locateGithubUser(githubUser)

    if (githubUserObject == False):
        print("ERROR: could not find github user: " + githubUser);
        return

    teamName =             "Student_" + firstName  # name -- string

    githubTeamObject = find_team(org,teamName);

    if (githubTeamObject == False):
        print("ERROR: could not find team: " + teamName)
        print("RUN THE addStudentsToTeams script first!")
        return
    
    createRepo(lab,githubUserObject,githubTeamObject,firstName,csil)
                      
defaultInputFilename =  '../CS56-S13-data/CS56 S13 Github Userids (Responses) - Form Responses.csv'

parser = argparse.ArgumentParser(description='Disambiguate First Names.')
parser.add_argument('lab',metavar='labxx',  
                    help="which lab (e.g. lab00, lab01, etc.)")
parser.add_argument('-i','--infileName',
                    help='input file (default: ' + defaultInputFilename+"'",
                    default=defaultInputFilename)
parser.add_argument('-u','--githubUsername', 
                    help="github username, default is current OS user",
                    default=getpass.getuser())

args = parser.parse_args()


pw = getpass.getpass()
g = Github(args.githubUsername, pw)

org = g.get_organization("UCSB-CS56-S13")

lab = args.lab

userList = getUserList(args.infileName)

for line in userList:
    processLine(lab,
                line['last'],
                line['first'],
                line['github'],
                line['email'],
                line['csil'])
        








