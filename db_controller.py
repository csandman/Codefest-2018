from flask import jsonify
from cloudant import Cloudant
import os, json

def get_users(db):
    return jsonify((map(lambda doc: doc['users'], db)))
