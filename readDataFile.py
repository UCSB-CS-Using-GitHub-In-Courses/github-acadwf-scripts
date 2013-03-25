#!/usr/bin/python3

import csv

filename =  '../CS56-S13-data/CS56 S13 Github Userids (Responses) - Form Responses.csv'

def processLine(lastName,githubUser):
    print("Last Name: ",lastName,end='');
    print(" github userid:: ",githubUser);
   

with open(filename,'r',newline='') as f:
    csvFile = csv.DictReader(f,delimiter=',', quotechar='"')
    for line in csvFile:
        processLine(line["Last Name"],line["github userid"])

