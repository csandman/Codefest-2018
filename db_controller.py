from flask import jsonify
from cloudant import Cloudant
import os, json
import algorithm1 as alg

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

def update_user(db, user):
    #  __import__('pprint').pprint((get_user(db, user['email'])))
    for doc in db:
        if user['email'] == doc['email']:
            doc.delete()
            put_user(db, user)
            return user
    return {'error': 'user not found'}

def put_location(db, location):
    db.create_document(location)
    return location

def get_locations(db_location):
    return list(map(lambda doc: doc, db_location))

def get_matches(db_user, db_location, user_id):
    
    #  primary_user = get_user(db_user, user_id)
    users = get_users(db_user)
    locations = get_locations()


    #  properties = alg.final_comp(primary_user, users)

    #  __import__('pprint').pprint(properties)

    __import__('pprint').pprint(users)
    __import__('pprint').pprint(locations)

    return {'users': users, 'locations': locations }
#  def update_user(db, user_id, update):
#      doc = get_doc(db)
#      user = [u for u in doc if u['id'] == user_id]
#      for key in update.keys():
#          user[key] = update[key]
#      print(user)
