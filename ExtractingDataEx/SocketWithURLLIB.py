import socket
#import urllib
import urllib.request, urllib.parse, urllib.error
# exite uma urlib mais otimizada - urlib3

handle = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
#access the page with a handle like an open command.

for line in handle:
    print(line.decode().strip())
    #.decode() transforma o texto do type bytes, provavel em utf-8 para string do py
