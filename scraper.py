#-*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = ('http://www.daum.net')

contentUrl = opener.open(url).read()

soup = BeautifulSoup(contentUrl)

list = soup.findAll('a', attrs={'href': re.compile("daum")})

for link in list:
    print link.text

print len(list)
