#-*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib
import mechanize
from bs4 import BeautifulSoup

def login(URL, userid, userpwd):
	# Browser
	br = mechanize.Browser()

	# # Enable cookie support for urllib2
	# cj = mechanize.LWPCookieJar()
	# br.set_cookiejar(cj)

	# # Browser options
	# br.set_handle_equiv(True)
	# # br.set_handle_gzip(True)
	# br.set_handle_redirect(True)
	# br.set_handle_referer(True)
	# br.set_handle_robots(False)

	# br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time=1 )

	# br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geocko/2008071615 Fedora/3.0.1.fc9 Firefox/3.0.1')]

	auth = {                                                                       
	    'userid': userid
	    , 'userpwd': userpwd
	}

	data = urllib.urlencode(auth)
	request = mechanize.Request(URL+'/Main/MemberLogInOut/Login')
	br.open(request, data=data)                             
	response = br.open(URL+'/Work/')
	
	print response.read()
	
	soup = BeautifulSoup(response)
	response.close()
	
	cardlist = []
	table = soup.find('table', {'class':'ui-jqgrid-btable'}).find('tbody').find_all('tr',{'class':'ui-widget-content jqgrow ui-row-ltr'})
	for card in table:
		cardlist.append(card.find('td',{'aria-describedby':'grid_list_empname'}).get_text().encode('UTF-8'))
	print cardlist[randint(0,len(cardlist)-1)]

if __name__ == "__main__":
	# try:
		# login(ACCOUNT['LOGIN'][0], ACCOUNT['LOGIN'][1])
		login("http://110.45.186.46:8889", "hdkwon","dlsth1501hd")

	# except Exception, e:
		# raise e


