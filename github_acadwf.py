# github-acadwf.py contains utility functions for 
# working with PyGithub objects to set up teams, and repositories
# and other Github objects for academic workflows.

from __future__ import print_function
import sys

def addPyGithubToPath():
    pathToPyGithub="./PyGithub";
    if not pathToPyGithub in sys.path:
        sys.path.append("./PyGithub")

def addStudentsFromFileToTeams(g,orgName,infileName):
    
    addPyGithubToPath()
    from github import GithubException
    from disambiguateFunctions import getUserList
    
    try:
        org = g.get_organization(orgName)
        
        userList = getUserList(infileName)
        
        for line in userList:
            addStudentToTeams(g,
                              org,
                              line['last'],
                              line['first'],
                              line['github'],
                              line['email'],
                              line['csil'])
            
    except GithubException as ghe:
        print(ghe)
   

def addStudentToTeams(g,org,lastName,firstName,githubUser,umail,csil):

    addPyGithubToPath()
    from github import GithubException

    print(firstName + " " + lastName + "...",end='');

    user = findUser(g,githubUser)

    if (user==False):
       return

    team = createTeam_Student_FirstName(org,user,firstName)
    if (team==False):
       return
    
    # TRY ADDING STUDENT TO THE AllStudents team

    try:
        allStudentsTeam = findTeam(org,"AllStudents");
        if (allStudentsTeam != False):
           allStudentsTeam.add_to_members(user);
           print("... added to AllStudents\n")

    except GithubException as e:
       print (e)

def createLabRepo(g,orgName,infileName,lab):

    from disambiguateFunctions import getUserList

    org = g.get_organization(orgName)

    userList = getUserList(infileName)

    for line in userList:
        createLabRepoForThisUser(g,
                                 org,
                                 lab,
                                 line['last'],
                                 line['first'],
                                 line['github'],
                                 line['email'],
                                 line['csil'])
        

def createLabRepoForThisUser(g,
                             org,
                             lab,
                             lastName,firstName,githubUser,umail,csil):
   

    print(firstName + "\t" + lastName + "\t" + githubUser);
    
    githubUserObject = findUser(g,githubUser)

    if (githubUserObject == False):
        print("ERROR: could not find github user: " + githubUser);
        return

    teamName =             "Student_" + firstName  # name -- string

    githubTeamObject = findTeam(org,teamName);

    if (githubTeamObject == False):
        print("ERROR: could not find team: " + teamName)
        print("RUN THE addStudentsToTeams script first!")
        return
    
    createRepoForOrg(org,lab,githubUserObject,githubTeamObject,firstName,csil)


def createRepoForOrg(org,labNumber,githubUserObject,githubTeamObject, firstName,csil):

    addPyGithubToPath()
    from github import GithubException


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



def findUser(g,githubUser,quiet=False):
    "wraps the get_user method of the Github object"

    addPyGithubToPath()
    from github import GithubException

    try:
        user = g.get_user(githubUser)
        if (user == None):
            if not quiet:
                print("No such github user: ",githubUser)
            return False
        else:
            if not quiet:
                print(" githubUser: " + user.login + "...",end='');
            return user
    except GithubException as e:
        print(e)
        if not quiet:
            print("No such github user: ",githubUser);
        return False

def   createTeam_Student_FirstName(org,user,firstName,quiet=False):

    addPyGithubToPath()
    from github import GithubException

    teamName =             "Student_" + firstName  # name -- string

    # Try to create the team

    team = False   # Sentinel to see if it succeeded or failed
    try:
       team = org.create_team(teamName,
                         [],
                         "push");
       if not quiet:
           print(" team {0} created...".format(teamName),end='')
    except GithubException as e:
       if (e.data['errors'][0]['code']=='already_exists'):
          if not quiet:
              print(" team {0} already exists...".format(teamName),
                         end='') 
       else:
          print (e)
          
       
    # If the create failed, try to find the team by name
    # This is our own function and does NOT throw an exception on failure

    if team==False:
       team = findTeam(org,teamName)
     
    if team==False:
       if not quiet:
           print(
           "ERROR: team {0} could not be created and was not found".format(
               teamName))
       return False
        
    # If the create failed (e.g. team already exists)
    # still go ahead and try to add the student to the team

    try:
       team.add_to_members(user);
       if not quiet:
           print(
           "user {0} added to {1}...".format( user.login, teamName) , end='')
       return team
    except GithubException as e:
       print (e)
       
    return False

def findTeam(org,teamName,refresh=False):

    # There isn't a "lookup team by name within an org"
    # function in the API.  So we cache a dictionary of teams
    # on the first call, then use that afterwards to look up the team.
            
    if not hasattr(findTeam, 'cacheTeamList') or refresh:
        findTeam.cacheTeamList = org.get_teams();

    if not hasattr(findTeam, 'cacheTeamDict') or refresh:
        findTeam.cacheTeamDict = {}

        for team in findTeam.cacheTeamList:
            findTeam.cacheTeamDict[team.name]=team

    if teamName in findTeam.cacheTeamDict:
        return findTeam.cacheTeamDict[teamName]
    
    return False

