from sonarqube import SonarQubeClient

class SonarqubeClient:
    def __init__(self, url, token, projectKey):
        self.client = SonarQubeClient(sonarqube_url=url, token=token)
        self.projectKey = projectKey

    def get_pull_request_status(self, pull_request):
        '''
            returns the status of a pull request
            pull_request is the pull request number
        '''
        projectstatus = self.client.qualitygates.get_project_qualitygates_status(projectKey=self.projectKey,pullRequest=pull_request)
        return projectstatus.get("projectStatus").get("status")

    def get_pull_request_issues(self, pull_request):
        '''
            returns the issues of a pull request
            pull_request is the pull request number
        '''
        issues = list(self.client.issues.search_issues(componentKeys=self.projectKey, pullRequest=pull_request))
        return issues

    def get_sonarqube_pull_request_url(self,url, pull_request):
        '''
            returns the sonarqube url of a pull request
            pull_request is the pull request number
        '''
        url = "{}/dashboard?id={}&pullRequest={}".format(url, self.projectKey, pull_request)
        return url