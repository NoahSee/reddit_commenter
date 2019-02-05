# reddit_commenter

Posts articles linked in r/singapore as comments.

Initial code obtained from
https://github.com/fterh/sneakpeek

## Mongo DB Atlas

#### Database Name
MyDatabase

#### Collection
SubmissionRecords

#### Doccument
id, title, url, created_utc

## AWS Lambda

#### Layer
Allows external libraries to be used in AWS Lambda.
- package.zip is used to create the layer.
- includes dependencies for the following external libraries:
  - newspaper
  - bs4
  - praw
  - tldextract
  - pymongo

#### Handler
Calls function in .py file when triggered.
- lambda_function.lambda_handler

#### Trigger
Runs script every 5 minutes.
- Cloudwatch Events as "every_5_minutes"

#### Test
Runs script once manually.
- Amazon Cloudwatch as "RunOnce"
