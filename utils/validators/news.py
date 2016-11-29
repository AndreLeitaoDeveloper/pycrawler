import sys
import os
class NewsValidator(object):

    def attribute_news(self, noticia):
        print noticia
        new =  {}

        try:
            new['title'] = unicode(noticia.title.string)
        except AttributeError:
            new['title'] = None

        try:
            new['description'] = unicode(noticia.description.string)
        except AttributeError:
            new['description'] = None

        try:
            new['link'] = unicode(noticia.link.string)
        except AttributeError:
            new['link'] = None

        try:
            new['category'] = unicode(noticia.category.string)
        except AttributeError:
            new['category'] = None

        try:
           new['pubdate'] = unicode(noticia.pubdate.string)
        except AttributeError:
            new['pubdate'] = None

        try:
            new['creator'] = unicode(noticia.creator.string)
        except AttributeError:
            new['creator'] = None

        try:
            new['guid'] = unicode(noticia.guid.string)
        except AttributeError:
            new['guid'] = None

        return new

