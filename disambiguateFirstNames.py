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


import argparse


import getpass
import csv

import sys
sys.path.append("/cs/faculty/pconrad/github/github-acadwf-scripts/PyGithub");


from github import Github
from github import GithubException

defaultInputFilename =  '../CS56-S13-data/CS56 S13 Github Userids (Responses) - Form Responses.csv'

parser = argparse.ArgumentParser(description='Disambiguate First Names.')
parser.add_argument('-i','--infileName',help='input file',
                    default=defaultInputFilename)


args = parser.parse_args()

print("args.infileName=",args.infileName)

