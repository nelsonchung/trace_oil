#coding:utf-8

import requests
from pyquery import PyQuery as pq
#from yahoo_finance import Share
#from grs import Stock
import httplib, urllib

url_oil="http://www.plus500.com/zh/Instruments/CL"

#Get html
r = requests.get(url_oil)
#print r.text 

q = pq(url_oil)
#print "Oil Now: "+(q('#ctl00_ContentPlaceMain1_LabelBuyPriceBig').text())
#print "Oil High:"+(q('#ctl00_ContentPlaceMain1_LabelHighPriceValue').text())
#print "Oil Low: "+(q('#ctl00_ContentPlaceMain1_LabelLowPriceValue').text())
oil_price = q('#ctl00_ContentPlaceMain1_LabelBuyPriceBig').text()
print oil_price


#Sync information to ThingSpeak
params = urllib.urlencode({'field1': oil_price, 'key':'0EX26G182NC5OW3O'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
	
try:
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	print worth_value
	print market_value
	print strftime("%a, %d %b %Y %H:%M:%S", localtime())
	print response.status, response.reason
	data = response.read()
	conn.close()
except:
	print "connection failed"	


#yahoo = Share('YHOO')
#print yahoo.get_open()
#print yahoo.get_price()
#print yahoo.get_trade_datetime()
#yahoo.refresh()

#stock = Stock('00642U')
#print stock.moving_average(5)

