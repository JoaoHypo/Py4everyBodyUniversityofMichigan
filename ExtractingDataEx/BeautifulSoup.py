import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignoring SSL errors:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL -") # Asking for the URL
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#print(soup)
#Retrive all of the ancher tags
tags = soup('a') #getting the anchors of the HTML and returning a list with the anchors
#this typo its called tag.
for tag in tags:
    #print(type(tag))
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)