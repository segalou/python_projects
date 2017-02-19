# -*- coding: utf-8 -*-
"""
Updated on Sat Dec 10 10:09:15 2016
1. TODO need a status code logic to determine if the site is successully loaded
2. TODO currently using bs4 to parse, may try re for next update since not every img has ['src'] or ['original']
@author: sega_lou
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 09:58:03 2016

@author: sega.lou
"""

import cookielib
import requests
from bs4 import BeautifulSoup
import re

def get_html(target_url):
    
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
    headers = {'User-Agent': agent}
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename='cookies')

    try:
        session.cookies.load(ignore_discard=True)
    except:
        print("Cookie 未能加载")
    
    try:
        r = session.get(target_url, headers=headers)
        if r.status_code == 200:
            print "target URL is sucessfully loaded"
    except:
        print "loading failed"
    html = r.content#.decode('utf-8')
    session.cookies.save()
    return html
    

    #bsObj = BeautifulSoup(r.text,"lxml")
    #return bsObj

def parse_target_url(target_url):
    if target_url[-1] == "/":
        target_url = target_url[:-1]
    x = target_url.split("//")
    x = x[1]
    x = x.split(".")
    return x #return a list with url split by .

def filter(img_url_str):
    try:
        if "icon" not in img_url_str and "avatar" not in img_url_str and img_url_str is not None:
            return True #good url, left for furthur process
    except:
        return False #give up

def fix_img_url(target_img,target_url): #in some case, the url does not contain the main domain part.
    url = parse_target_url(target_url)
    if target_img.find(url[0]) <0 and target_img.find(url[1])<0:
        if target_img.find("http")<0:
            target_img = target_url+target_img
            return target_img
    else:
        return target_img

def parse(html,target_url):
    result = []
    reg1 = re.compile('img .*=(?:\'|\")(.*?(?:jpg|gif|png))')
    reg2 = re.compile('(?:src|original|data-original)=(?:\"|\')(.*?(?:jpeg|jpg|gif|png))')
    imgtmp1= re.findall(reg1,html)
    imgtmp2 = re.findall(reg2,html)
    img_list = set(imgtmp1+imgtmp2)
    for img in img_list:
        if filter(img):
            target_img = fix_img_url(img,target_url)
            if target_img not in result and target_img is not None:
                result.append(target_img)
    return result
        
'''
    img_list = bsObj.findAll("img")
    for img in img_list:
        try:        
            target_img = img['src']
        except:
            try: 
                target_img = img['original']
            except:
                try:
                    target_img = img['data-original']
                except:
                    print "=========parsing alert========="                    
                    print img
                    print "=========parsing alert========="   
                    target_img = ""
        if filter(target_img):
            target_img = fix_img_url(target_img,target_url)
            if target_img not in result and target_img != "":
                result.append(target_img)
    return result
'''

def fun():
    #target_url = "http://aio.it168.com/"
    #target_url = "http://www.wycwfw.com"
    #target_url = "http://www.xinkuanxiu.com"
    #target_url = "http://www.xtnjl.com"
    #target_url = "http://www.yangyang33.com"
    #target_url = "http://www.yy.com"
    #target_url = "http://www.zaisucheng.com"
    #target_url = "http://www.zf71.com"
    #target_url = "http://www.zgg35.com"
    #target_url = "http://club.autohome.com.cn"
    #target_url = "http://gameid.5173.com"
    #target_url = "http://henbt.com/"
    target_url = "http://hd.huya.com"
    source_code = get_html(target_url)
    #print source_code
    result = parse(source_code,target_url)
    for i in result:
        print i
    
if __name__ == "__main__":
    fun()
 
    
