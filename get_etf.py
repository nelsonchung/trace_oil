#We just get the actual(yesterday) value today
import requests
from pyquery import PyQuery as pq
from datetime import date, timedelta
import httplib, urllib

etf_number="00642U"
url_oil="http://www.moneydj.com/ETF/X/Basic/Basic0003.xdjhtm?etfid="+etf_number+".TW"

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Get html
r = requests.get(url_oil)
#r = requests.post(url_oil)
#print r.text 
#print r.text.decode('utf-8') 

#Save html
data = open('data.html', 'w')
data.write(r.text.encode('utf-8'))
data.close()

#Get value
#ctl00_ctl00_MainContent_MainContent_stable
url_pq_result = pq(url_oil)
#print "Test data: "+(url_pq_result('#ctl00_ctl00_MainContent_MainContent_stable').text())

#url_etf_value = pq(url_pq_result('#ctl00_ctl00_MainContent_MainContent_stable').text())
#td = url_etf_value('td')
td = url_pq_result('table')
market_index=8
worthvalue_index=14
split_str="("

market_value = td('td').eq(market_index).text()
market_value = market_value[0: market_value.find(split_str)]
#print market_value 
worth_value = td('td').eq(worthvalue_index).text()
worth_value = worth_value[0: worth_value.find(split_str)]
#print worth_value

#Get date
#import time
#import datetime
#t = time.time()
##data sample code
#datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
#print datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d')

#Sync information to ThingSpeak
params = urllib.urlencode({'field1': worth_value, 'field2': market_value, 'key':'9P9ETYQIZPAW0948'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
#conn = httplib.HTTPConnection("api.thingspeak.com/channels/111185")
	
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

#Print final information
yesterday = date.today() - timedelta(1)
print yesterday.strftime('%Y/%m/%d') + "  " + worth_value + "   " + market_value

