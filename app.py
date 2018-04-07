from flask import Flask, request, jsonify, render_template
import cf_deployment_tracker
import os, json
from cloudant import Cloudant
import db_controller

cf_deployment_tracker.track()

app = Flask(__name__)

db_name = 'rumr'
client = None
db = None

port = int(os.getenv('PORT', 8000))

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found vcap services')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local vcap_services')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

@app.route('/rumr/api/users', methods=['GET'])
def get_users():
    if client:
        return db_controller.get_users(db)
    else:
        print('No database')
        return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
