# reddit_commenter

WIP

Deployment

ASW Cloud9 (Deployment testing)

For installing packages, set Active Directory to:
- [environment\RedditCommenter\Redditcommenter]

The following is necessary because of the active directory in lambda is different.
For running script, set Active Directory to:
- [environment\RedditCommenter]
- python3 RedditCommenter/lambda_handler.py

To install packages on Cloud9, run the following in the bash terminal
- pip-3.6 install praw -t .
- pip-3.6 install tldextract -t .
- pip-3.6 install newspaper3k -t .
- pip-3.6 install bs4 -t .
- pip-3.6 install pymongo -t .
- pip-3.6 install dnspython -t .

AWS Lambda

Trigger
- Cloudwatch Events > "rate(5 minutes)"

Test
- Amazon Cloudwatch > Runs once, no args
