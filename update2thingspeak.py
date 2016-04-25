import httplib, urllib
from time import localtime, strftime
import time

def doit():
    params = urllib.urlencode({'field1': worth_value, 'field2': market_value, 'field3': oil_price, 'key':'9P9ETYQIZPAW0948'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print worth_value
		print market_value
		print oil_price 
		print strftime("%a, %d %b %Y %H:%M:%S", localtime())
		print response.status, response.reason
		data = response.read()
		conn.close()
	except:
		print "connection failed"	

#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
	while True:
		doit()
