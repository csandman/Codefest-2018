from flask import jsonify
from cloudant import Cloudant
import os, json

#  def get_doc(db, document):
#      doc = [doc for doc in list(map(lambda doc: doc, db)) if document in doc][0]
#      return doc[document]

def get_users(db):
    users = list(map(lambda doc: doc, db))
    return users

def get_user(db, user_email):
    return db.get_query_result({'email': {'$eq': user_email }})[0]

def put_user(db, user):
    db.create_document(user)
    return user

def put_location(db, location):
    for document in db:
        if 'properties' in document:
            document['properties'].append(location)
            document.save()
            return location
    return {}

def get_matches(db_user, db_location, user_id):
    properties = get_doc(db, 'properties')
    matches = []
    return properties
#  def update_user(db, user_id, update):
#      doc = get_doc(db)
#      user = [u for u in doc if u['id'] == user_id]
#      for key in update.keys():
#          user[key] = update[key]
#      print(user)
