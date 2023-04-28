from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

# Fill in with your personal access token and org URL 
personal_access_token = 'YOURPAT' #### want to pull pat from secrets
organization_url = 'https://dev.azure.com/nhsuk' #### want to pull url from secrets
project = 'nhsuk.nhsuk' #### want to pull project from secrets

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()

# Get the first page of projects
get_projects_response = core_client.get_projects()
index = 0
while get_projects_response is not None:
    for project in get_projects_response.value:
        pprint.pprint("[" + str(index) + "] " + project.name)
        index += 1
    if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
        # Get the next page of projects
        get_projects_response = core_client.get_projects(continuation_token=get_projects_response.continuation_token)
    else:
        # All projects have been retrieved
        get_projects_response = None

#class GitHubClient:
#    def __init__(self, access_token, github_repo):
#        self.g = Github(access_token)
#        self.repo = self.g.get_repo(github_repo)
#
#    def create_review(self, pull, body, event, comments):
#        '''
#            creates a review on a pull request
#            pull is the pull request number
#            body is the review body
#            acceptable events are APPROVE, REQUEST_CHANGES, COMMENT
#            comments is a list of comment objects
#            comment object is a dictionary with the following keys
#            path (str), position (int), body(str), line(int), side(str), start_line(int), start_side(str)
#        '''
#        pr = self.repo.get_pull(pull)
#        if comments:
#            pr.create_review(body=body, event=event, comments=comments)
#        else:
#            pr.create_review(body=body, event=event)
#