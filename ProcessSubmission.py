from newspaper import Article

from Logging import LoggingHandler
Log = LoggingHandler()

# using sneakpeek code to handle formatting of articles into comments
# https://github.com/fterh/sneakpeek
from handler import HandlerManager
from comment import format_comment

def process_submission(submission):
    url = submission.url
    Log('qualifying submission - id {} {}'.format(submission.id, url))

    if "straitstimes.com" in submission.url:
        Log('accept submission - id {} {}'.format(submission.id, url))

        """

        *** To be decided ***

        article = Article(url)
        article.download()
        article.parse()

        title = article.title
        body = article.text

        # return { "url":url, "title" : title , "body" : body }

        """

        # using sneakpeek code
        handler = HandlerManager.get_handler(submission.url)
        comment_raw = handler.handle(submission.url)
        comment = format_comment(comment_raw)
        print(comment)

    else:
        Log('decline submission - id {} {}'.format(submission.id, submission.url))
        return False