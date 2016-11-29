#!/usr/bin/env python
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib, sys, os

sys.path.append(os.path.abspath("utils/validators"))
from news import NewsValidator

sys.path.append(os.path.abspath("conf"))
from confbd import Connect
connectbd = Connect("local", "noticias")

data = connectbd.collection.find({"noticias.title": "title"}).count()

print data



def get_url(url):
    """
    This function is responsable for connection to database and define database name and collection name

    Args:
        Url (str)  : Url of crawler website

    Returns:
        takeaways  : Parse of the website
    
    """
    thisurl = url 
    #Feed HTML file into parser
    item = urllib.urlopen(thisurl).read()
    soup = BeautifulSoup(item, 'html.parser')
    takeaways = soup.findAll('item')
    return takeaways

takeaways = get_url("http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")


noticia = {}

validators = NewsValidator()

print validators.attribute_news(noticia)



for eachtakeaway in takeaways:
   
    jornal = {}
    jornal['noticias'] = {}

    try:
        title = unicode(eachtakeaway.title.string)
    except AttributeError:
        title =None

    try:
        description = unicode(eachtakeaway.description.string)
    except AttributeError:
        description =None

    try:
        link = unicode(eachtakeaway.link.string)
    except AttributeError:
        link =None

    try:
        category = unicode(eachtakeaway.category.string)
    except AttributeError:
        category = None

    try:
        pubdate = unicode(eachtakeaway.pubdate.string)
    except AttributeError:
        pubdate =None

    try:
        creator = unicode(eachtakeaway.creator.string)
    except AttributeError:
        creator =None

    try:
        guid = unicode(eachtakeaway.guid.string)
    except AttributeError:
        guid =None
    
    jornal['noticias'] = {"title":title,
             "description": description,
             "link": link,
             "category": category,
             "pubdate": pubdate,
             "creator": creator,
             "guid": guid}

exist = verify_news(title)

if exist:
    result = collection.insert_one(jornal)
else:
    error_exist("Noticia já existente")