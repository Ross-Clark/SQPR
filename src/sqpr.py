from ghclient import GithubClient
from sqclient import SonarqubeClient
import argparse

def main(args):
    # get status and issues from SonarQube
    sqc = SonarqubeClient(args['sonarqube_url'] , args['sonarqube_token'], args['project_key'])

    # Check PR status
    issues = sqc.get_pull_request_issues(args['pull_request_number'])
    number_of_issues=len(list(issues))
    status = sqc.get_pull_request_status(args['pull_request_number'])
    ghc = GithubClient(access_token=args['github_token'], github_repo=args['repo'])
    sonarqube_url = sqc.get_sonarqube_pull_request_url(args['sonarqube_url'],args['pull_request_number'])

    if(status=="OK"):
        # post ok message
        comments = []
        if number_of_issues > 0:
            # ok with comments based on issues
            body = """Quality Gate passed, some issues found 🙂
                see the issues in more detail at [Sonarqube]({})""".format(sonarqube_url)

            comments = generate_comment_list(issues)
            ghc.create_review(pull=int(args['pull_request_number']), body=body, event="COMMENT", comments=comments)
        else:
            # no issues
            ghc.create_review(pull=int(args['pull_request_number']), body="No issues found 😀", event="COMMENT", comments=comments)

    else:
        # post fail and issues

        body = """Quality Gate Failed 🤨
        see the issues in more detail at [Sonarqube]({})""".format(sonarqube_url)

        if number_of_issues > 0:
            comments = generate_comment_list(issues)
            ghc.create_review(pull=int(args['pull_request_number']), body=body, event="REQUEST_CHANGES", comments=comments)
        else:
            ghc.create_review(pull=int(args['pull_request_number']), body=body, event="REQUEST_CHANGES", comments=comments)

def generate_comment_list(issues):
    comments = []
    for issue in issues:
        comments.append(generate_comment(issue))
    return comments

def generate_comment(issue):
    path = issue.get('component').split(':')[1]
    message = issue.get('message')
    line = issue.get('line')
    if line:
        comment = {
            "path": path,
            "body": message,
            "line": line,
        }
    else:
        comment = {
            "path": path,
            "body": message,
        }
    return comment

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sonarqube Github Pull Request Integration')
    parser.add_argument('-g','--github-token', help='Github Access Token', required=True)
    parser.add_argument('-k','--project-key', help='Sonarqube project key', required=True)
    parser.add_argument('-p','--pull-request-number', help='PR Number in Github', required=True)
    parser.add_argument('-r','--repo', help='Github Repository Url', required=True)
    parser.add_argument('-s','--sonarqube-token', help='Sonarqube Access Token', required=True)
    parser.add_argument('-u','--sonarqube-url', help='Sonarqube URL', required=True)
    
    args = vars(parser.parse_args())

    main(args)


# general example usage sqpr.py -g <github-token> -k <sonarqube-project-key> -p <pull-request-number> -r <github-repo-url> -s <sonarqube-token> -u <sonarqube-url>
