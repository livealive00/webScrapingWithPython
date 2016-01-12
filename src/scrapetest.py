from urllib.request import urlopen

# first app
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())