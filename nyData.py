# -- coding: utf-8 --
"""
Created on Sat Mar 31 20:44:36 2018

@author: Pradeep Singh Bisht
"""

from nytimesarticle import articleAPI
api = articleAPI('57ca56b88fa3479c8d5261bcccece35a')

from bs4.diagnose import diagnose
from bs4 import BeautifulSoup
import requests
import os.path

def get_text(url):
        data=""
        p=requests.get(url).content
        soup=BeautifulSoup(p)    
        paragraphs=soup.select("p.story-body-text.story-content")
        data=p
        text=""
        for paragraph in paragraphs:
            text+=paragraph.text
        text=text.encode('ascii', 'ignore')
        return str(text)
    
def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['url'] = i['web_url']
        news.append(dic)
    return(news)
    

save_path = 'nyDataFiles_articles_china'
queryTerm = 'china'

for j in range(1, 11):
    articles = api.search( q = queryTerm, page=j)
    artList = parse_articles(articles)
    
    allText = []
    for i in range(0,len(artList)):
        urlLink = artList[i]['url']
        print(urlLink)
        try:
            article1 = get_text(urlLink)
        except:
            pass
        name_of_file = 'nyText_%s_page_%d_article_%d.txt' % (queryTerm,j,i)
        completeName = os.path.join(save_path, name_of_file)
        nyText=open(completeName,'w')
        nyText.write(article1)
        nyText.close()
        
#        allText.append(article1)
#        #f = open('%s.csv' % name, 'wb')
#    
#    nyText=open('nyText_%s_%s.txt' % (queryTerm,j) ,'w')
#    for element in allText:
#        nyText.write(element+'\n')
#    
#    nyText.close()
