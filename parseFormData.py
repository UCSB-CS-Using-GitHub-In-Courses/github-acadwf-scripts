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


from string import maketrans

import argparse


import getpass
import csv

import sys
sys.path.append("/cs/faculty/pconrad/github/github-acadwf-scripts/PyGithub");


from github import Github
from github import GithubException

from disambiguateFunctions import makeUserDict
from disambiguateFunctions import disambiguateAllFirstNames

def convertUserList(csvFile):
    userList = []
    for line in csvFile:
        userList.append(makeUserDict(line["First Name"],
                                     line["Last Name"],
                                     line["github userid"],
                                     line["Umail address"],
                                     line["CSIL userid"]))
    

    for user in userList:
        user["first"] = user["first"].translate(maketrans(" ","_"));

    return userList
        

                      
defaultInputFilename =  '../CS56-S13-data/CS56 S13 Github Userids (Responses) - Form Responses.csv'

parser = argparse.ArgumentParser(description='Disambiguate First Names.')
parser.add_argument('-i','--infileName',
                    help='input file (default: ' + defaultInputFilename+"'",
                    default=defaultInputFilename)

args = parser.parse_args()

with open(args.infileName,'r') as f:
    csvFile = csv.DictReader(f,delimiter=',', quotechar='"')
    
    userList = convertUserList(csvFile)

    newUserList = disambiguateAllFirstNames(userList)
    
    for line in userList:
        print(line)
        
        

