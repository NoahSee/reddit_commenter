import json
import requests
from bs4 import BeautifulSoup

def handle_url_todayonline(url):
    """
    URL handler function
    @url: string, url of article
    @output: dictionary, with "title" and "body"
    """

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    article_id = soup.find("meta", {"name":"cXenseParse:recs:articleid"})["content"]
    TODAY_API_URL = f"https://www.todayonline.com/api/v3/article/{article_id}"
    article = json.loads(requests.get(TODAY_API_URL).content)["node"]
    title = article["title"]
    body = BeautifulSoup(article["body"], "html.parser").get_text()
    body = body.replace("\n", "\n\n")  # Markdown requires 2 \n to create a new paragraph
    return { "title" : title , "body" : body }

### Test Portion | Run HandleURLTodayOnline.py to test ###
if __name__ == "__main__":
    url = 'https://www.todayonline.com/world/trump-asks-unity-presses-hard-line-immigration'
    print(handle_url_todayonline(url))