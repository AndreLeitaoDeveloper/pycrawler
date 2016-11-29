#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath("../utils/validators"))
from news import NewsValidator

class Noticia(NewsValidator):
    """ 

    Class Noticia 

    """

    def __init__(self, noticia):
        """
        Construtor
        """
        self.category = noticia['category']
        self.description = noticia['description']
        self.pubdate = noticia['pubdate']
        self.creator = noticia['creator']
        self.title = noticia['title']
        self.link = noticia['link']
        self.guid = noticia['guid']


    def _to_json(self):
        """
        This function is responsable for connection to database and define database name and collection name

        Args:
            self (obj) : Object class Noticia
            noticia (str)  : Content website

        Returns:
            takeaways  : Parse of the website
        
        """
        for eachtakeaway in self.noticia:

            jornal = {}
            jornal['noticias'] = {}
            
            jornal['noticias'] = {"title":title,
                     "description": description,
                     "link": link,
                     "category": category,
                     "pubdate": pubdate,
                     "creator": creator,
                     "guid": guid}
        return jornal['noticias']
