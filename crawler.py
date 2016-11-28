#!/usr/bin/env python
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from pymongo import MongoClient
import urllib

def connection_db():
    """
    This function is responsable for connection to database and define database name and collection name

    Args:

    Returns:
        client     : Connection to database
        db         : Database name
        collection : Collecion name

    """
    client = MongoClient('localhost', 27017)
    db = client.local
    collection = db.noticias
    return (client, db, collection)

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

def verify_news(title):
    """
    This function is responsable for verify if the news already exist

    Args:
        title (str)  : Title the news
    Returns:
       bool: The return value. True for success, False otherwise.
    """
    data = collection.find({"noticias.title": title}).count()

    if data == 0:
        return True
    else:
        return False

def error_exist(error):
    """
    Return error 

    Args:
        error (str)  : Text of error
    Returns:
       str: Return error
    """
    print error
    return



client, db, collection = connection_db()
takeaways = get_url("http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")


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