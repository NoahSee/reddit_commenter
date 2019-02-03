import schedule
import json
import praw

from ProcessSubmission import process_submission
from FormatComment import format_comment
from Logging import LoggingHandler

### Initialise #####################################################################################

# (Log())
Log = LoggingHandler()
Log('Starting script ...')

# (secret)
with open('secret.json') as f:
    secret = json.loads(f.read())

# (db)
from MongoDB_Database import Database
db = Database(secret["MongoDB"])

# (subreddit)
reddit = praw.Reddit(**secret['Reddit'])          
subreddit = reddit.subreddit("test")

### Main Function #################################################################################

def process_subreddit(test = False):
    Log('process_subreddit called')
    if test: db.ClearSubmissionRecords()
    submission_records = db.GetSubmissionRecords()

    for submission in subreddit.new(limit=10):

        # Submission has already been processed
        if any( submission_record['submission_id'] == submission.id for submission_record in submission_records):
            Log('skip submission - id {}'.format(submission.id))

        # Submission has not been processed yet
        else:
            Log('new submission - id {}'.format(submission.id))
            db.AddSubmissionRecord( { "submission_id" : submission.id , "url" : submission.url } )
            content = process_submission(submission)
            if content:
                comment = format_comment(content)
                # submission.reply(comment)

### Execution logic ###############################################################################

process_subreddit(test=True)
schedule.every(2).minutes.do(process_subreddit)
while True:
    schedule.run_pending()