from flask import Flask, request, jsonify, render_template
import cf_deployment_tracker
import os, json
from cloudant import Cloudant

cf_deployment_tracker.track()

app = Flask(__name__)

port = int(os.getenv('PORT', 8000))

hello = {'hello': 'world'}
@app.route('/rumr/api/v1.0/hello', methods=['GET'])
def hello_world():
    return jsonify({'test': hello})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
