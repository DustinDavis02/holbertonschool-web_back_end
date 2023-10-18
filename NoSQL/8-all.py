#!/usr/bin/env python3
""" List all documents in MongoDB """

from typing import List

def list_all(mongo_collection) -> List:
    """ Function lists all documents in MongoDB """
    documents = []
    collection = mongo_collection.find()
    for doc in collection:
        documents.append(doc)
    return documents
