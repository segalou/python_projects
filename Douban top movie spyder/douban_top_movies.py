# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:00:29 2016

@author: sega.lou
"""

import requests
import re
import csv
import numpy as np
from bs4 import BeautifulSoup

download_url = 'https://movie.douban.com/top250'

headers=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

def get_raw_html(url):
    s = requests.session()  
    s = s.get(url,headers = headers[np.random.randint(0,3)])
    return s.content

def parse_html(html):
    bsObj = BeautifulSoup(html)
    movie_list = bsObj.find('ol',{'class':'grid_view'})
    
    movie_list_result = []    

    for movie in movie_list.findAll('li'):
        em = movie.find('em').getText()
        link = movie.find('a')['href']
        title = movie.find('span',{'class':'title'}).getText()
        title = title.encode('utf-8')
        intro = movie.find('p',{'class':''}).getText()
        rating = movie.find('span',{'class':'rating_num'}).getText()
        try:
            quote = movie.find('p',{'class':'quote'}).getText()
            quote = re.sub('\n+'," ",quote) 
            quote = quote.encode('utf-8')
        except:
            quote = ''
        p = re.compile('[0-9]{4}')
        year = p.findall(intro)[0]
        movie_list_result.append( [em,title,year,rating,link,quote] )

    next_page = bsObj.find('span',{'class':'next'}).find('a')
    if next_page:
        return movie_list_result, download_url + next_page['href']
    return movie_list_result,None

def export_to_csv(movie_list_result):
    csvFile = open("./top250movies.csv","wb")
    csvFile.write('\xEF\xBB\xBF')
    writer = csv.writer(csvFile)
    writer.writerow(['#','Movie',"Year","Rating","Link","Quote"])
    
    try:
        '''
        for page_result in movie_list_result:
            for movie in page_result:
                movie[0] = movie[0].encode('utf-8')
                movie[4] = movie[4].encode('utf-8')
        '''
        for page_result in movie_list_result:
            for movie in page_result:
                writer.writerow(movie)
    finally:
        csvFile.close()

def main():
    url = download_url
    result = []
    html = get_raw_html(url)

    while url:
        html = get_raw_html(url)
        movies, url = parse_html(html)
        result.append(movies)

    export_to_csv(result)
    print 'export done'


if __name__=='__main__':
    main()