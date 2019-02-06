from URLHandlers.HandleURLDefault import handle_url_default
from URLHandlers.HandleURLStraitsTimes import handle_url_straitstimes
from URLHandlers.HandleURLRiceMedia import handle_url_ricemedia
from URLHandlers.HandleURLTodayOnline import handle_url_todayonline

url_handlers = {
    "channelnewsasia.com"   : handle_url_default,
    "mothership.sg"         : handle_url_default,
    "ricemedia.co"          : handle_url_ricemedia,
    "straitstimes.com"      : handle_url_straitstimes,
    "todayonline.com"       : handle_url_todayonline,
    "zula.sg"               : handle_url_default
}

### handle_url takes in a url and uses it to call handle, returns dict or None
def handle_url(url):
    for url_handler in url_handlers:
        if url_handler in url:
            return url_handlers[url_handler](url)
    return None

### format_comment takes in dict and returns a string
def format_comment(title=None,body=None):
    body = "> " + body.replace("\n\n", "\n\n> ")
    return "> # " + title + "\n\n" + body

### process_submission
def process_submission(submission):
    """
    @submission:    object, praw.submission : https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
    @output:        string (comment), or None 
    """
    print('processing - id {} {}'.format(submission.id, submission.url))
    article_data = handle_url(submission.url)
    return format_comment(**article_data) if article_data else None