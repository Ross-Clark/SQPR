from github import Github

# Get the access token from the environment variable
class GithubClient:
    def __init__(self,access_token,github_repo):
        self.g = Github(access_token)
        self.repo = self.g.get_repo(github_repo)

    def create_review(self,pull, body, event, comments):
        '''
            creates a review on a pull request
            pull is the pull request number
            body is the review body
            acceptable events are APPROVE, REQUEST_CHANGES, COMMENT
            comments is a list of comment objects
            comment object is a dictionary with the following keys
            path (str), position (int), body(str), line(int), side(str), start_line(int), start_side(str)
        '''
        pr = self.repo.get_pull(pull)
        if comments:
            pr.create_review(body=body, event=event, comments=comments)
        else:
            pr.create_review(body=body, event=event)
