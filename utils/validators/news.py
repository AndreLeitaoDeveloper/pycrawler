class NewsValidator(object):

    def attribute_news(self, noticia):
        result = []


        for eachtakeaway in noticia:
            new = {}
            try:
                new['title'] = unicode(eachtakeaway.title.string)
            except AttributeError:
                new['title'] = None

            try:
                new['description'] = unicode(eachtakeaway.description.string)
            except AttributeError:
                new['description'] = None

            try:
                new['link'] = unicode(eachtakeaway.link.string)
            except AttributeError:
                new['link'] = None

            try:
                new['category'] = unicode(eachtakeaway.category.string)
            except AttributeError:
                new['category'] = None

            try:
               new['pubdate'] = unicode(eachtakeaway.pubdate.string)
            except AttributeError:
                new['pubdate'] = None

            try:
                new['creator'] = unicode(eachtakeaway.creator.string)
            except AttributeError:
                new['creator'] = None

            try:
                new['guid'] = unicode(eachtakeaway.guid.string)
            except AttributeError:
                new['guid'] = None

            result.append({"title":new['title'],
             "description": new['description'],
             "link": new['link'],
             "category": new['category'],
             "pubdate": new['pubdate'],
             "creator": new['creator'],
             "guid": new['guid']})

        return result
        