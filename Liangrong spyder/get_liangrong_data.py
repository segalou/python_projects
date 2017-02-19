# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:19:25 2016

@author: sega.lou
"""
import requests
import re
import csv
import numpy as np
#from bs4 import BeautifulSoup

headers=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
{'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'},\
{'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'},\
{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
{'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
{'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},\
{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},\
{'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}]

#TODO 用js代码获取数据
#http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=FD&sty=SHSZHSSUM&st=0&sr=1&p=1&ps=15&js=[(x)]}&rt=49142415
#要build request header，其中cookies要从之前的page获取

def get_js_response(numofdays):
    url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=FD&sty=SHSZHSSUM&st=0&sr=1&p=1&ps=%s&js=[(x)]&rt=49142415'%numofdays
    s = requests.session()
    s = s.get(url,headers = headers[np.random.randint(0,len(headers))])    
    return s.content

def data_cleansing(data):
    data = re.split('"|,|[|]',data)
    data = [x for x in data if x != '']
    data = data[1:-1]
    
    result = []

    if len(data)%13 ==0:
        for i in range(len(data)/13):
            daily = data[13*i:13*(i+1)]
            result.append(daily)
    else:
        print 'something wrong for data parsing' 
    
    return result
'''
def parse_html(html):
    bsObj = BeautifulSoup(html)
    
    p = re.compile('defjson:{.*}')
    data = str(p.findall(bsObj.text))
    
    data = re.split(',|"',data)
    data = data[2:-1]
    data = [ x for x in data if x != '' ]
    
    result = []
    
    if len(data)%13 ==0:
        for i in range(len(data)/13):
            daily = data[13*i:13*(i+1)]
            result.append(daily)
    else:
        pass
    
    return result
'''

def export_to_csv(result):
    csvFile = open("./liangrong_data.csv","wb")
    csvFile.write('\xEF\xBB\xBF')
    writer = csv.writer(csvFile)
    writer.writerow(["交易日期 ","融资余额（上海）","融资余额（深圳）","融资余额（合计）","本日融资买入（上海）","本日融资买入（深圳）","本日融资买入（合计）","本日融券余额（上海）","本日融券余额（深圳）","本日融券余额（合计）","本日融资融券余额（上海）","本日融资融券余额（深圳）","本日融资融券余额（合计）"])
    
    try:
        for i in result:
            writer.writerow(i)
    finally:
        csvFile.close()
    
def main():
    data= get_js_response(1000)
    result = data_cleansing(data)
    export_to_csv(result)
    
if __name__=='__main__':
    main()