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

sys.path.append("./PyGithub");

from github import Github
from github import GithubException

def processLine(lastName,firstName,githubUser,umail,csil):
    print(firstName + "\t" + lastName + "\t" + githubUser);

    ### TODO: Factor out into a function 
    
    try:
        user = g.get_user(githubUser)
        if (user == None):
            print("No such github user: ",githubUser)
            return
        else:
            print("Found user: " + user.login);
    except GithubException as e:
        print(e)
        print("No such github user: ",githubUser);
        return

    ### FACTOR OUT INTO FUNCTION of LINE in userList

    teamName =             "Student_" + firstName  # name -- string

    # CREATE THE Student_FirstName team,
    #   and add the student's github userid to that team.

    team = False   # Sentinel to see if it succeeded or failed
    try:
        team = org.create_team(teamName,
                     [],
                     "push");
        team.add_to_members(user);
    except GithubException as e:
       print (e)
       
    
    # If the create failed (e.g. team already exists)
    # still go ahead and try to add the student to the team

    try:
        if (team==False):
            team = find_team(org,teamName);
            if (team != False):
                team.add_to_members(user);
    except GithubException as e:
        print (e)
            
    # TRY ADDING STUDENT TO THE AllStudents team

    try:
        allStudentsTeam = find_team(org,"AllStudents");
        if (allStudentsTeam != False):
            allStudentsTeam.add_to_members(user);
    except GithubException as e:
       print (e)


def find_team(org,teamName):

    teams = org.get_teams();
    for team in teams:
        if team.name == teamName:
            return team
    return False




pw = getpass.getpass()

g = Github(args.githubUsername, pw)

org = g.get_organization("UCSB-CS56-S13")

                      
defaultInputFilename =  '../CS56-S13-data/CS56 S13 Github Userids (Responses) - Form Responses.csv'

parser = argparse.ArgumentParser(description='Disambiguate First Names.')
parser.add_argument('-i','--infileName',
                    help='input file (default: ' + defaultInputFilename+"'",
                    default=defaultInputFilename)

parser.add_argument('-u','--githubUsername', 
                    help="github username, default is current OS user",
                    default=getpass.getuser())

args = parser.parse_args()

userList = getUserList(args.infileName)

for line in userList:
    processLine(line['last'],line['first'],line['github'],line['email'],line['csil'])
        








