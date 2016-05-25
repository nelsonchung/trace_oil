#coding:utf-8

import requests
from pyquery import PyQuery as pq
#from yahoo_finance import Share
#from grs import Stock
import httplib, urllib

#url_golden="http://www.gck99.com.tw/gold.aspx"
url_golden="http://www.goldlegend.com/"

#Get html
r = requests.get(url_golden)
#print r.text 

#test
data = open('test.html', 'w')
data.write(r.text)
data.close()

#q = pq(golden)
#oil_price = q('#ctl00_ContentPlaceMain1_LabelBuyPriceBig').text()
#print oil_price


##Sync information to ThingSpeak
#params = urllib.urlencode({'field3': oil_price, 'key':'9P9ETYQIZPAW0948'})
#headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
#conn = httplib.HTTPConnection("api.thingspeak.com:80")
	
#try:
#	conn.request("POST", "/update", params, headers)
#	response = conn.getresponse()
##print oil_price
##print response.status, response.reason
##print strftime("%a, %d %b %Y %H:%M:%S", localtime())
#	data = response.read()
#	conn.close()
#except:
#	conn.close()
##print "connection failed"	
