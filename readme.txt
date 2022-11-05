SQPR

SQPR integrates sonarqube into the pull request process.
It helps you to analyse your code and automatically as a reviews PR's based on sonarqubes analysis.

SQPR will approve PR's with an 'OK' status, comment when there are issues on an 'OK' status and request changes on an non-''OK' status
SQPR also Highlights any issues within the code review using sonarqubes issue messages.

How to run:
run sqpr after analysing your project with sonarqube

example usage: sqpr.py -g <github-token> -k <sonarqube-project-key> -p <pull-request-number> -r <github-repo> -s <sonarqube-token> -u <sonarqube-url>

currently this requires cloning the project into the pipeline, however I am planning on releasing it on pypi later
