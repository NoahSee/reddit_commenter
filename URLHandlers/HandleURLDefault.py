from newspaper import Article

def handle_url_default(url): 
    """
    URL handler function
    @url: string, url of article
    @output: dictionary, with "title" and "body"
    """
    article = Article(url)
    article.download()
    article.parse()
    return { "title" : article.title , "body" : article.text }

### Test Portion | Run HandleURLDefault.py to test ###
if __name__ == "__main__":
    url = 'https://www.straitstimes.com/singapore/popiah-kings-son-ben-goi-had-wanted-to-celebrate-childs-first-birthday-this-week'
    print(handle_url_default(url))