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



def printf(str,*args):
   print(str % args, end='')

sys.path.append("./PyGithub");

from github import Github
from github import GithubException

def findUser(g,githubUser):
    try:
        user = g.get_user(githubUser)
        if (user == None):
            print("No such github user: ",githubUser)
            return False
        else:
            printf(" githubUser: " + user.login + "...");
            return user
    except GithubException as e:
        print(e)
        print("No such github user: ",githubUser);
        return False

def   createTeam_Student_FirstName(org,user,firstName):

    teamName =             "Student_" + firstName  # name -- string

    # Try to create the team

    team = False   # Sentinel to see if it succeeded or failed
    try:
       team = org.create_team(teamName,
                         [],
                         "push");
       print(" team {0} created...".format(teamName),end='')
    except GithubException as e:
       if (e.data['errors'][0]['code']=='already_exists'):
          print(" team {0} already exists...".format(teamName),end='') 
       else:
          print (e)
          
       
    # If the create failed, try to find the team by name
    # This is our own function and does NOT throw an exception on failure

    if team==False:
       team = find_team(org,teamName)
     
    if team==False:
       print("ERROR: team {0} could not be created and was not found".format(
             teamName))
       return False
        
    # If the create failed (e.g. team already exists)
    # still go ahead and try to add the student to the team

    try:
       team.add_to_members(user);
       print("user {0} added to {1}...".format( user.login, teamName) , end='')
       return team
    except GithubException as e:
       print (e)
       
    return False


def processLine(g,lastName,firstName,githubUser,umail,csil):

    print(firstName + " " + lastName + "...",end='');

    user = findUser(g,githubUser)

    if (user==False):
       return

    team = createTeam_Student_FirstName(org,user,firstName)
    if (team==False):
       return
    
    # TRY ADDING STUDENT TO THE AllStudents team

    try:
        allStudentsTeam = find_team(org,"AllStudents");
        if (allStudentsTeam != False):
           allStudentsTeam.add_to_members(user);
           print("... added to AllStudents\n")

    except GithubException as e:
       print (e)

def find_team(org,teamName):

    # TODO: Consider doing some caching here
    #  to speed things up rather than getting all the
    #  teams every time.   Store them in a dictionary
    #  by team name for fast look up later.

    teams = org.get_teams();
    for team in teams:
        if team.name == teamName:
            return team
    return False



                      
defaultInputFilename =  '../CS56-S13-data/CS56 S13 Github Userids (Responses) - Form Responses.csv'

parser = argparse.ArgumentParser(description='Disambiguate First Names.')
parser.add_argument('-i','--infileName',
                    help='input file (default: ' + defaultInputFilename+"'",
                    default=defaultInputFilename)

parser.add_argument('-u','--githubUsername', 
                    help="github username, default is current OS user",
                    default=getpass.getuser())

args = parser.parse_args()

pw = getpass.getpass()
g = Github(args.githubUsername, pw)

try:
   org = g.get_organization("UCSB-CS56-S13")

   userList = getUserList(args.infileName)

   for line in userList:
      processLine(g,
                  line['last'],
                  line['first'],
                  line['github'],
                  line['email'],
                  line['csil'])

except GithubException as ghe:
   print(ghe)
   

        








