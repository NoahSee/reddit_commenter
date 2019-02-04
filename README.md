# reddit_commenter

WIP

Deployment

ASW Cloud9 (Deployment testing)

To install packages on Cloud9, run the following in the bash terminal
- sudo pip-3.6 install praw -t .
- sudo pip-3.6 install tldextract -t .
- sudo pip-3.6 install newspaper3k -t .
- sudo pip-3.6 install bs4 -t .
- sudo pip-3.6 install pymongo -t .
- sudo pip-3.6 install dnspython -t .

AWS Lambda

Trigger
- Cloudwatch Events > "rate(5 minutes)"

Test
- Amazon Cloudwatch > Runs once, no args
