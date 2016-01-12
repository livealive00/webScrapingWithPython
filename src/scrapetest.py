from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getTitle(url):

    try:
        html = urlopen(url)
        if html is None:
            print("URL is not found")
            return None

    except HTTPError as e:
        print("HTTP ERROR")
        print(e)
        return None

    except URLError as e:
        print("URL ERROR")
        print(e)
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title =bsObj.body.h1
    except AttributeError as e:
        return None

    return title

title = getTitle("http://pythonscraping.com/exercises/exercise1.html")

print(title)