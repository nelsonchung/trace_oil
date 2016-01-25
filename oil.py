#coding:utf-8

import requests
from pyquery import PyQuery as pq

url_oil="http://www.plus500.com/zh/Instruments/CL"

#Get html
r = requests.get(url_oil)
#print r.text 

q = pq(url_oil)
print "Oil Now: "+(q('#ctl00_ContentPlaceMain1_LabelBuyPriceBig').text())
print "Oil High:"+(q('#ctl00_ContentPlaceMain1_LabelHighPriceValue').text())
print "Oil Low: "+(q('#ctl00_ContentPlaceMain1_LabelLowPriceValue').text())
