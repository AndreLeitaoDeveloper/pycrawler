#!/usr/bin/env python
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib, sys, os

from utils.validators.news import NewsValidator
from utils.requests.news import get_url
from conf.confbd import Connect

#sys.path.append(os.path.abspath("pycrawler/controller/"))
#from news import NewsController
from controllers.news import NewsController

connectbd = Connect("local", "noticias")
#data = connectbd.collection.find({"noticias.title": "title"}).count()

takeaways_content = get_url("http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")

noticia = {}

validators = NewsValidator()

takeaways = validators.attribute_news(takeaways_content)

new_controller = NewsController()

for takeaway in takeaways:
  
    exist = new_controller.verify_news(takeaway['title'])

    if exist:
        result = connectbd.collection.insert_one(takeaway)
    else:
        new_controller.error_exist("Noticia já existente")