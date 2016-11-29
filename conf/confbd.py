#!/usr/bin/env python
from pymongo import MongoClient

class Connect(object):
    """docstring for Connect"""
    def __init__(self, dbname, dbcollection):
        self.dbname = dbname
        self.dbcollection = dbcollection
        client = MongoClient('localhost', 27017)
        self.db = getattr(client, dbname)
        self._collection = getattr(self.db, dbcollection)

    @property
    def collection(self):
        return self._collection