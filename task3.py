
import bs4 as bs
import urllib.request
source = urllib.request.urlopen("http://www.bbc.com/news").read()
soup = bs.BeautifulSoup(source,"lxml")
print(soup.title)
for headlines in soup.find_all("h3"):
	print(headlines.text)

#!/usr/bin/python

#import urllib2
#from BeautifulSoup4 import BeatifulSoup

# Open URL, read HTML, and find title
#URLObject = urllib2.urlopen('http://yourwebpage.com')
#html = BeautifulSoup(URLObject.read())
#data = html.find('title')

# Print title
#print data.contents[0]
