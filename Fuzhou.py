from nturl2path import url2pathname
from wsgiref import headers
import requests
import re

url = "https://search.ccgp.gov.cn/bxsearch"
params = {
    'searchtype': '1',
    'page_index': '1',
    'bidSort': '',
    'buyerName': '',
    'projectId': '',
    'pinMu': '',
    'bidType': '7',
    'dbselect': 'bidx',
    'kw': '',
    'start_time': '2021:01:01',
    'end_time': '2021:12:31',
    'timeType': '6',
    'displayZone': '福建',
    'zoneId': '35 not 3502',
    'pppStatus': '0',
    'agentName': '',
}
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}




text = requests.get(url=url,params=params,headers=headers)
print(text.text)