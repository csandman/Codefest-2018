from flask import Flask, request, jsonify, render_template
import cf_deployment_tracker
import os, json
from cloudant import Cloudant

cf_deployment_tracker.track()

app = Flask(__name__)

port = int(os.getenv('PORT', 8000))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
