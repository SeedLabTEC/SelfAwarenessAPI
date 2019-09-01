import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import flask

app = flask.Flask(__name__)

#Fetch the service account key JSON file contents
cred = credentials.Certificate('adminsdk.json')

firebase_admin.initialize_app(options={
    'databaseURL': 'https://self-awareness-70035.firebaseio.com/'
})

DatabaseRefPower = db.reference('self-awareness-power')

@app.route('/Power', methods=['POST'])
def create():
    req = flask.request.json
    obj = DatabaseRefPower.push(req)
    return flask.jsonify({'id': obj.key}), 201

@app.route('/Power/<id>')
def read(id):
    return flask.jsonify(EnsureObject(id))

@app.route('/Power/<id>', methods=['PUT'])
def update(id):
    EnsureObject(id)
    req = flask.request.json
    DatabaseRefPower.child(id).update(req)
    return flask.jsonify({'success': True})

@app.route('/Power/<id>', methods=['DELETE'])
def delete(id):
    EnsureObject(id)
    DatabaseRefPower.child(id).delete()
    return flask.jsonify({'success': True})

def EnsureObject(id):
    test = DatabaseRefPower.child(id).get()
    if not test:
        flask.abort(404)
    return test
