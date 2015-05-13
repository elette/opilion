#-*- coding: utf-8 -*-

import urllib2, re, string
#enter_point ='http://' +  raw_input('enter url: ') # enter point
enter_point ='http://' + 'www.daum.net'
db_name = 'base.txt' # input data base name

def uniq(seq):
        set = {}
        map(set.__setitem__, seq, [])
        return set.keys()

def geturls(url):
        items = []
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'iBot ;)')
        content = urllib2.urlopen(request).read()
        items = re.findall('href="http://.*?"', content)
        urls = []
        for item in items:
                item = item.replace('href=','')
                item = item.replace('"','')
                urls.append(item)
        return urls

db = open(db_name,'w')
allurls = uniq(geturls(enter_point))

for url in allurls:
        urls = geturls(url)
        for u in urls: allurls.append(u)
        allurls = uniq(allurls)
        db.write(string.join(urls,'\n'))
        print url+' ['+str(len(allurls))+']'
db.write('\n\n')
db.close()
