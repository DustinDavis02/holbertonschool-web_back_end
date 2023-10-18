#!/usr/bin/env python3
""" Inserts new document in MongoDB based on kwargs """

from pymongo import MongoClient
from bson.objectid import ObjectId

def insert_school(mongo_collection, **kwargs):
    """ Function inserts new document in MongoDB based on kwargs """
    document = kwargs
    result = mongo_collection.insert_one(document)
    return result.inserted_id
