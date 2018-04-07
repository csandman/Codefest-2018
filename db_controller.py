from flask import jsonify
from cloudant import Cloudant
import os, json

def get_doc(db):
    return list(map(lambda doc: doc['users'], db))[0]

def get_users(db):
    doc = get_doc(db)
    return jsonify({ 'users': doc})

def get_user(db, user_id):
    doc = get_doc(db)
    return jsonify({ 'users': [u for u in doc if u['_id'] == user_id] })

def put_user(db, user):
    data = {'users': user}
    #  db.create_document(data)
    return user

#  def update_user(db, user_id, update):
#      doc = get_doc(db)
#      user = [u for u in doc if u['id'] == user_id]
#      for key in update.keys():
#          user[key] = update[key]
#      print(user)
