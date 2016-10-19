import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
i=0
while i < 7:
    for tag in tags:
        if tags[17] == tag:
            name = tag.contents[0]
            url = tag.get('href',None)
            html = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(html,'html.parser')
            tags = soup('a')
        else:
            continue
    i=i+1
print (name)