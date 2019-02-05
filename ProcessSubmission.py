# using sneakpeek code to handle formatting of articles into comments
# https://github.com/fterh/sneakpeek
from handler import HandlerManager

SupportedURLs = [
    "channelnewsasia.com",
    "mothership.sg",
    "ricemedia.co",
    "straitstimes.com",
    "todayonline.com",
    "zula.sg"
    ]

### format_comment
def format_comment(title=None,body=None):
    body = "> " + body.replace("\n\n", "\n\n> ")
    return "> # " + title + "\n\n" + body

### process_submission
def process_submission(submission):
    """
    @submission:    object, praw.submission : https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
    @output:        string (comment), or None 
    """
    url = submission.url
    print('qualifying submission - id {} {}'.format(submission.id, url))

    # Handle if URL is supported
    if  any( u in submission.url for u in SupportedURLs):
        print('accept submission - id {} {}'.format(submission.id, url))

        # using sneakpeek code
        handler = HandlerManager.get_handler(submission.url)
        article_data = handler.handle(submission.url)
        return format_comment(**article_data) if article_data else None

    # return None if not supported
    else:
        print('decline submission - id {} {}'.format(submission.id, submission.url))
        return None