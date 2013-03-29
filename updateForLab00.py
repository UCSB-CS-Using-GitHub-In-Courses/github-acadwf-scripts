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
import argparse

from github_acadwf import addPyGithubToPath
from github_acadwf import addStudentsFromFileToTeams
from github_acadwf import createLabRepo
from github_acadwf import findTeam
from github_acadwf import pushFilesToRepo

addPyGithubToPath()

from github import Github
from github import GithubException
                      
defaultInputFilename =  '../CS56-S13-data/CS56 S13 Github Userids (Responses) - Form Responses.csv'

parser = argparse.ArgumentParser(description='Complete update for lab00')
parser.add_argument('-i','--infileName',
                    help='input file (default: ' + defaultInputFilename+"'",
                    default=defaultInputFilename)

parser.add_argument('-u','--githubUsername', 
                    help="github username, default is current OS user",
                    default=getpass.getuser())

parser.add_argument('-s','--scratchDirName', 
                    help="scratch directory to clone repos in while doing work",
                    default="./scratchRepos")

args = parser.parse_args()

pw = getpass.getpass()
g = Github(args.githubUsername, pw)

org= g.get_organization("UCSB-CS56-S13")

addStudentsFromFileToTeams(g,org,args.infileName)

# call findTeam with refresh=True to refresh the cache
# otherwise, the newly created teams won't be found when
# findTeam is called in createLabRepo

allStudentsTeam = findTeam(org,"AllStudents",refresh=True)

createLabRepo(g,org,args.infileName,"lab00")
pushFilesToRepo(g,org,"lab00","",args.scratchDirName)










        








