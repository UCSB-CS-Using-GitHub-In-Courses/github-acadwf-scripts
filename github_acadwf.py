import sys

# github-acadwf.py contains utility functions for 
# working with PyGithub objects to set up teams, and repositories
# and other Github objects for academic workflows.

def find_team(org,teamName,refresh=False):

    # There isn't a "lookup team by name within an org"
    # function in the API.  So we cache a dictionary of teams
    # on the first call, then use that afterwards to look up the team.
            
    if not hasattr(find_team, 'cacheTeamList') or refresh:
        find_team.cacheTeamList = org.get_teams();

    if not hasattr(find_team, 'cacheTeamDict') or refresh:
        find_team.cacheTeamDict = {}

        for team in find_team.cacheTeamList:
            find_team.cacheTeamDict[team.name]=team

    if teamName in find_team.cacheTeamDict:
        return find_team.cacheTeamDict[teamName]
    
    return False

