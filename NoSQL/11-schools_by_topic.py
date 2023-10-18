#!/usr/bin/env python3
""" Returns list of school having specific topic """

from pymongo import MongoClient
from typing import List

def schools_by_topic(mongo_collection, topic) -> List:
    """ Function returns list of schools having specific topic """
    schools = []
    query = {"topics": topic}
    results = mongo_collection.find(query)
    for school in results:
        schools.append(school)
    return schools