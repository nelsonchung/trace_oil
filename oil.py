#coding:utf-8

import requests
from pyquery import PyQuery as pq
#from yahoo_finance import Share
from grs import Stock

url_oil="http://www.plus500.com/zh/Instruments/CL"

#Get html
r = requests.get(url_oil)
#print r.text 

q = pq(url_oil)
print "Oil Now: "+(q('#ctl00_ContentPlaceMain1_LabelBuyPriceBig').text())
print "Oil High:"+(q('#ctl00_ContentPlaceMain1_LabelHighPriceValue').text())
print "Oil Low: "+(q('#ctl00_ContentPlaceMain1_LabelLowPriceValue').text())



#yahoo = Share('YHOO')
#print yahoo.get_open()
#print yahoo.get_price()
#print yahoo.get_trade_datetime()
#yahoo.refresh()

stock = Stock('00642U')
print stock.moving_average(5)

