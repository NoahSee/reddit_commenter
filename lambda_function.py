### Lambda CloudWatch Logs using print
from __future__ import print_function

### Python Libraries
import os
import sys
import json

# External Libraries
import praw

# https://stackoverflow.com/questions/49399140/module-import-error-when-executing-a-lambda-python-function
if 'LAMBDA_TASK_ROOT' in os.environ:
    sys.path.append(f"{os.environ['LAMBDA_TASK_ROOT']}/lib")
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

### Internal Libraries
from ProcessSubmission import process_submission

### Initialise #################################################################

print('Starting script ...')

# (secret)
with open('secret.json') as f:
    secret = json.loads(f.read())

# (db)
from MongoDB_Database import Database
db = Database(secret["MongoDB"])

# (subreddit)
reddit = praw.Reddit(**secret['Reddit'])          
subreddit = reddit.subreddit("singapore")

### Main Function ##############################################################

def process_subreddit(test = False):

    print('START process_subreddit')

    if test: db.ClearSubmissionRecords()
    submission_records = db.GetSubmissionRecords()

    for submission in subreddit.new(limit=5):
        
        # Submission has already been processed
        if any( submission_record['id'] == submission.id for submission_record in submission_records):
            print('skip - id {} {}'.format(submission.id, submission.title))

        # Submission has not been processed yet
        else:
            
            print('new - id {} {}'.format(submission.id, submission.title))
            
            db.AddSubmissionRecord( {
                "id" : submission.id ,
                "url" : submission.url,
                "title" : submission.title,
                "created_utc" : submission.created_utc
            } )
            
            comment = process_submission(submission)

            if comment:

                print('COMMENTING - id {}'.format(submission.id))

                try:
                    submission.reply(comment)
                except Exception as e:
                    print(e)

### Execution logic ############################################################

def lambda_handler(event, context):
    process_subreddit(test=False)
    return 'Done'