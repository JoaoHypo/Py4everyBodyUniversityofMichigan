import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the URL -") # Asking for the URL
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parse')

print(soup)
#Retrive all of the ancher tags
