import re
import requests
import textwrap
from bs4 import BeautifulSoup

def handle_url_ricemedia(url):
    """
    URL handler function
    @url: string, url of article
    @output: dictionary, with "title" and "body"
    """
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    # https://stackoverflow.com/a/24618186
    # We only want article text, not inline scripts or inline jss
    for script in soup(["script", "style"]):
        script.extract()

    # Plant markers to denote the start and end of the article
    start_marker = "EXTRACT_START"
    end_marker = "EXTRACT_END"
    soup.find(name="div", class_="post-date").insert(0, start_marker)
    soup.find(name="span", class_="author-name").append(end_marker)

    unwrapped_body = re.search(f"{start_marker}(.+?){end_marker}", soup.text).group(1)
    article_body = "\n".join(textwrap.wrap(unwrapped_body, 80))
    article_body = article_body.replace("\n", "\n\n")  # Markdown requires 2 \n to create a new paragraph
    article_title = soup.find(name="h2", class_="post-title").text

    return { "title" : article_title , "body" :  article_body.replace("\xa0", " ") }

### Test Portion | Run HandleURLRiceMedia.py to test ###
if __name__ == "__main__":
    url = 'http://ricemedia.co/culture-life-the-politics-of-the-50-ang-bao/'
    print(handle_url_ricemedia(url))        