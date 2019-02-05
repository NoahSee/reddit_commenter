# using sneakpeek code to handle formatting of articles into comments
# https://github.com/fterh/sneakpeek
from handler import HandlerManager
from comment import format_comment

def process_submission(submission):
    url = submission.url
    print('qualifying submission - id {} {}'.format(submission.id, url))

    if "straitstimes.com" in submission.url:
        print('accept submission - id {} {}'.format(submission.id, url))

        # using sneakpeek code
        handler = HandlerManager.get_handler(submission.url)
        comment_raw = handler.handle(submission.url)

        if comment_raw:
            comment = format_comment(comment_raw)
            return comment
        else:
            return False

    else:
        print('decline submission - id {} {}'.format(submission.id, submission.url))
        return False