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

def get_locations(db_location, db_user):
    locations = list(map(lambda doc: doc, db_location))
    for location in locations:
        location['name'] = get_user(db_user, location['email'])[0]['name']

    return locations

def get_matches(db_user, db_location, user_id):

    primary_user = get_user(db_user, user_id)
    users = get_users(db_user)

    scores = alg.final_comp(primary_user, users)
    
    #test_user_data = alg.clean_json(primary_user[0])
    #test2 = alg.make_compa
    #locations = get_locations()
    __import__('pprint').pprint(scores)

    #  properties = alg.final_comp(primary_user, users)

    #  __import__('pprint').pprint(properties)

    #__import__('pprint').pprint(users)
    #__import__('pprint').pprint(primary_user)
    #__import__('pprint').pprint(scores)

#return {'users': users, 'locations': locations }
    return scores
#  def update_user(db, user_id, update):
#      doc = get_doc(db)
#      user = [u for u in doc if u['id'] == user_id]
#      for key in update.keys():
#          user[key] = update[key]
#      print(user)
