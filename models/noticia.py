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
