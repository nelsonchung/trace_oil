
import requests
from pyquery import PyQuery as pq

etf_number="00642U"
url_oil="http://www.moneydj.com/ETF/X/Basic/Basic0003.xdjhtm?etfid="+etf_number+".TW"

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Get html
r = requests.get(url_oil)
#r = requests.post(url_oil)
#print r.text 
print r.text.decode('utf-8') 

data = open('data.html', 'w')
data.write(r.text.encode('utf-8'))
data.close()

#ctl00_ctl00_MainContent_MainContent_stable
url_pq_result = pq(url_oil)
print "Test data: "+(url_pq_result('#ctl00_ctl00_MainContent_MainContent_stable').text())

#url_etf_value = pq(url_pq_result('#ctl00_ctl00_MainContent_MainContent_stable').text())
#td = url_etf_value('td')
td = url_pq_result('table')
for i in td:
        print url_pq_result(i).text()
