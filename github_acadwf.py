# github-acadwf.py contains utility functions for 
# working with PyGithub objects to set up teams, and repositories
# and other Github objects for academic workflows.

from __future__ import print_function
import sys

def populateRepo(repo,protoDir,scratchDir):
    import subprocess
    callList = ["./populateRepo.sh",repo.name,repo.ssh_url,protoDir,scratchDir]
    print ("Calling " + " ".join(callList))
    subprocess.call(callList)

def pushFilesToRepo(g,org,lab,firstName,scratchDirName):

    addPyGithubToPath()
    from github import GithubException

    import os

    protoDirName = lab + "_prototype"
    
    # check to see if protoDirName exists.  If not, bail
    
    if (not os.path.isdir(protoDirName)):
        raise Exception(protoDirName + " does not exist.")

    if (not os.path.isdir(scratchDirName)):
        raise Exception(scratchDirName + " does not exist.")

    protoDirName = os.path.abspath(protoDirName)
    scratchDirName = os.path.abspath(scratchDirName)

    if (firstName!=""):
        try:
            repoName = (lab + "_" + firstName)
            repo = org.get_repo(repoName)
            populateRepo(repo,protoDirName,scratchDirName)
        except GithubException as ghe:
            print("Could not find repo " + repoName + ":" + str(ghe))
            
    else:
            
        # User wants to update ALL repos that start with labxx_
        
        repos = org.get_repos()
        for repo in repos:
            if (repo.name.startswith(lab+"_")):
                populateRepo(repo,protoDirName,scratchDirName)
            







def addPyGithubToPath():
    pathToPyGithub="./PyGithub";
    if not pathToPyGithub in sys.path:
        sys.path.append("./PyGithub")


def addStudentsFromFileToTeams(g,org,infileName):
    
    addPyGithubToPath()
    from disambiguateFunctions import getUserList
    
    userList = getUserList(infileName)
    
    for line in userList:
        result = addStudentToTeams(g,org,
                          line['last'],
                          line['first'],
                          line['github'],
                          line['umail'],
                          line['csil'])

def updateStudentsFromFileForLab(g,org,infileName,lab,scratchDirName,firstName=''):

    """
    firstName='' means updateAllStudents
    """

    addPyGithubToPath()
    from disambiguateFunctions import getUserList
    
    userList = getUserList(infileName)

    for line in userList:
        
        if ( firstName=="" or line['first']==firstName ):
        
            result = addStudentToTeams(g,org,
                                       line['last'],
                                       line['first'],
                                       line['github'],
                                       line['email'],
                                       line['csil'])
            
            result = createLabRepoForThisUser(g,org,lab,
                                              line['last'],line['first'],line['github'],
                                              line['email'],line['csil'])
            
            if (result):
                pushFilesToRepo(g,org,lab,line['first'],scratchDirName)
                
        

def updateAllStudentsFromFileForLab(g,org,infileName,lab,scratchDirName):

    
    addPyGithubToPath()
    from disambiguateFunctions import getUserList
    
    userList = getUserList(infileName)

    for line in userList:
        
        result = addStudentToTeams(g,org,
                                       line['last'],
                          line['first'],
                          line['github'],
                          line['email'],
                          line['csil'])

        result = createLabRepoForThisUser(g,org,lab,
                                 line['last'],line['first'],line['github'],
                                 line['email'],line['csil'])
        
        if (result):
            pushFilesToRepo(g,org,lab,line['first'],scratchDirName)


def addUserToTeam(team,user,quiet=False):
    "A wrapper for team.add_to_members(user).  Returns true on success"

    addPyGithubToPath()
    from github import GithubException

    try:
       team.add_to_members(user);
       if not quiet:
           print(
           "user {0} added to {1}...".format( user.login, team.name) , end='')
       return True
    except GithubException as e:
       print (e)
       
    return False


def addStudentToTeams(g,org,lastName,firstName,githubUser,umail,csil):
    """
    return True if new, False if everthing already existed.
    Only creates team and adds if wasn't already on the teams
    """

    print("addStudentToTeams: {0} {1} (github: {2})...".format(
            firstName,lastName,githubUser),end='')

    studentTeam = getStudentFirstNameTeam(org, firstName)
    if (studentTeam != False):
        print("Team {0} exists...".format(studentTeam.name),end='')
    else:
        studentTeam = createTeamStudentFirstNameTeam(org,firstName)
        from types import NoneType
        if type(studentTeam)==NoneType:
            print("Error creating student first name team for {0}".format(firstName))
            sys.exit(1)
    

    studentGithubUser = findUser(g,githubUser)
    if (studentGithubUser == False):
        print ("github user {0} for {1} {2} does not exist".format(githubUser,firstName,lastName))
        return False       

    result = addUserToTeam(studentTeam,studentGithubUser,quiet=False)

    if (result):
        result = addUserToTeam(
            getAllStudentsTeam(org),studentGithubUser,quiet=False)
    
    return result
               
def  getStudentFirstNameTeam(org,firstName):
    return findTeam(org,formatStudentTeamName(firstName))

def  getAllStudentsTeam(org):
    return findTeam(org,"AllStudents")

    


def createStudentFirstNameTeamAndAddStudent(g,org,
                                       lastName,firstName,
                                       githubUser,umail,csil):
    addPyGithubToPath()
    from github import GithubException

    print(firstName + " " + lastName + "...",end='');

    user = findUser(g,githubUser)

    if (user==False):
       return

    team = createTeamStudentFirstNameTeam(org,firstName)
    if (team==False):
       return

def addStudentToAllStudentsTeam(g,
                                org,
                                lastName,
                                firstName,
                                githubUser,
                                umail,csil):

    addPyGithubToPath()
    from github import GithubException

    user = findUser(g,githubUser)

    if (user==False):
       return
    
    # TRY ADDING STUDENT TO THE AllStudents team

    try:
        allStudentsTeam = findTeam(org,"AllStudents");
        if (allStudentsTeam != False):
           allStudentsTeam.add_to_members(user);
           print("... {0}({1}) added to AllStudents\n".format(firstName,githubuser))

    except GithubException as e:
       print (e)

def createLabRepo(g,org,infileName,lab):

    from disambiguateFunctions import getUserList

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
        return False

    teamName = formatStudentTeamName(firstName)

    githubTeamObject = findTeam(org,teamName);

    if (githubTeamObject == False):
        print("ERROR: could not find team: " + teamName)
        print("RUN THE addStudentsToTeams script first!")
        return False
    
    return createRepoForOrg(org,lab,
                            githubUserObject,githubTeamObject,firstName,csil)

    

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
        return True
    except GithubException as e:
       if 'errors' in e.data and 'message' in e.data['errors'][0] and e.data['errors'][0]['message']=='name already exists on this account':
           print(" repo {0} already exists".format(repoName))
       else:
           print (e)

    return False

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

def formatStudentTeamName(firstName):
       return "Student_" + firstName  # name -- string


def createTeamStudentFirstNameTeam(org,firstName,quiet=False):
    "Only creates the team---doesn't add the student as a member"

    addPyGithubToPath()
    from github import GithubException

    teamName = formatStudentTeamName(firstName)

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

