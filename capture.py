import urllib
import urllib2
import time
import requests
from bs4 import BeautifulSoup

global picnum

for x in range(0,1):
	print("SMILE!!!") # Text displayed out
	urllib2.urlopen("http://10.5.5.9/bacpac/SH?t=hellofaceface&p=%01") # captures image - Takes few seconds to complete
	time.sleep(5) # sleep for number of seconds in brackets
	print("Copy")
#	urllib.urlretrieve("http://10.5.5.9:8080/DCIM/100GOPRO/GOPR0047.jpg","GOPR0047.jpg")
	#time.sleep(10)
	#print("Delete")
	#urllib2.urlopen("http://10.5.5.9/camera/DL?t=hellofaceface")


#Lists the contents of the pictures directory

url = 'http://10.5.5.9:8080/DCIM/100GOPRO'
soup = BeautifulSoup(requests.get(url).text)

for link in soup.find_all('a'):
	last = link.get('href')
#	print last




print last # prints name of last photo in folder

#Downloads the last photo to the pi root folder
f = urllib2.urlopen("http://10.5.5.9:8080/DCIM/100GOPRO/%s"%last)
with open(last,"wb") as code:
	code.write(f.read())


