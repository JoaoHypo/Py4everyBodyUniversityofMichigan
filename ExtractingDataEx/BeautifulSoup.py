import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the URL -") # Asking for the URL
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#print(soup)
#Retrive all of the ancher tags
tags = soup('a') #getting the anchors of the HTML and returning a list with the anchors
#this typo its called tag.
for tag in tags:
    #print(type(tag))
    print(tag.get('href',None))