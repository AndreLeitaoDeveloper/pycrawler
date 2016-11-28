#!/usr/bin/env python
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from pymongo import MongoClient
import urllib

client = MongoClient('localhost', 27017)
db = client.local
collection = db.noticias

thisurl = "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
#Feed HTML file into parser
item = urllib.urlopen(thisurl).read()
soup = BeautifulSoup(item, 'html.parser')
takeaways = soup.findAll('item')


for eachtakeaway in takeaways:
   
    jornal = {}
    jornal['noticias'] = {}
    try:
        category = str(eachtakeaway.category.string)
    except AttributeError:
        category = None
    
    
    print category
    jornal['noticias'] = {"title": unicode(eachtakeaway.title),
             "description": unicode(eachtakeaway.description),
             "link": unicode(eachtakeaway.link),
             "category": unicode(eachtakeaway.category),
             "pubdate": unicode(eachtakeaway.pubdate),
             "creator": unicode(eachtakeaway.creator),
             "guid": unicode(eachtakeaway.guid)}

collection = collection.insert_one(jornal)



