#!/usr/bin/python

# createLabRepoForEachStudent

#
#  REFACTOR THIS TO DO WHAT THE LINE ABOVE SAYS...
#

# This script reads all the users from the CSV file created
# by the Google Form, and for each it:
#  (1) checks if the github user exists (bails, if not)
#  (2) creates the lab00_LastName repo (if not already there)
#  (3) creates the Student_LastName team (if not already there)
#        and puts the lab00_LastName repo on that team
#  (4) adds the github user to the Student_LastName team and AllStudents team


# TODO: make more user-friendly
#       refactor into sensible functions
#       factor out so that this ONLY does the all students team,
#       and maybe also the Student_LastName team, but not the repos.
#       Note that the Student_LastName team is push by default.

import getpass
import csv

import sys
sys.path.append("/cs/faculty/pconrad/github/github-acadwf-scripts/PyGithub");


from github import Github
from github import GithubException


filename =  '../CS56-S13-data/CS56 S13 Github Userids (Responses) - Form Responses.csv'


username = raw_input("Github Username:")
pw = getpass.getpass()

g = Github(username, pw)

org = g.get_organization("UCSB-CS56-S13")

def processLine(lastName,firstName,githubUser,umail,csil):
    print(firstName + "\t" + lastName + "\t" + githubUser);

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



    desc = "Github repo for lab00 for " + firstName + " " + lastName + " <" + umail + ">"

    repoName =             "lab00_" + lastName  # name -- string
    teamName =             "Student_" + lastName  # name -- string

    try:  
        repo = org.create_repo(
            repoName,
            "lab00 for CS56 for " + firstName + " " + lastName, # description 
            "http://www.cs.ucsb.edu/~" + csil, # homepage -- string
            True, # private -- bool
            True, # has_issues -- bool
            True, # has_wiki -- bool
            True, # has_downloads -- bool
            auto_init=True,
            gitignore_template="Java")
    except GithubException as e:
       print (e)

    repo = org.get_repo(repoName);
    
    #  NotSet, # team_id -- github.Team.Team
    #  True, # auto_init -- bool
    #  "Java") # gitignore_template -- string
    
    # CREATE THE Student_LastName team,
    #   add the repo we just created,
    #   and add the student's github userid to that team.

    team = False   # Sentinel to see if it succeeded or failed
    try:
        team = org.create_team(teamName,
                     [repo],
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

with open(filename,'rb') as f:
    csvFile = csv.DictReader(f,delimiter=',', quotechar='"')
    for line in csvFile:
        processLine(line["Last Name"],
                    line["First Name"],
                    line["github userid"],
                    line["Umail address"],
                    line["CSIL userid"])






