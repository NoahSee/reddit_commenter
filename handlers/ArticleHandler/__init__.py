from newspaper import Article
from handlers.AbstractBaseHandler import AbstractBaseHandler, HandlerError

class ArticleHandler(AbstractBaseHandler):
    @classmethod
    def handle(cls, url):
        article = Article(url)
        article.download()
        article.parse()
        return { "title" : article.title , "body" : article.text }
