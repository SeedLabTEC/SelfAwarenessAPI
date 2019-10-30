import sys
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db
import os
import flask
from flask import  request, abort, jsonify, send_from_directory
import json
from tools import top
#from tools import process
import time
from flask_cors import CORS
from includes import monitor


app = flask.Flask(__name__)
CORS(app)

global monitors 
monitors =  []
#Fetch the service account key JSON file contents
#cred = credentials.Certificate('adminsdk.json')
#UPLOAD_DIRECTORY = "files"

"""firebase_admin.initialize_app(options={
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

@app.route('/Memory/<id>')
def readMemory(id):
    tem = process(id)
    tem.id = id
    tem.memory = 200
    print("test: "+tem.id)
    tem = json.dumps(tem.__dict__)
    return tem

@app.route("/app/<filename>", methods=["POST"])
def post_file(filename):
    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories directories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)
    #setPermissions(filename)
    # Return 201 CREATED
    return "", 201

@app.route("/runapp/<filename>", methods=["POST"])
def runApp(filename):
    app = process.process(filename)
    app.start()
    time.sleep(0.2)
    app.analizeCpu()
    return {'pid':app.appId,'ppid':os.getpid()}, 201"""

@app.route("/top", methods=["GET"])
def getTop():
    path="tools/scripts/getTop.sh"
    toppath = "top.txt"
    top.runTop(path)
    result = top.fileRefactor(toppath)
    top.deleteFile(toppath)
    return {'result':result}, 201


@app.route("/monitorApp/<int:pid>", methods=["POST"])
def monitorApp(pid):
    global monitors
    pid=  monitor.startProcess(pid)
    print(pid)
    return {'result':pid}, 201

@app.route("/getPidData/<int:pid>", methods=["GET"])
def getPidData(pid):
    result = monitor.getPidInfo(pid)
    return result, 201

@app.route("/getPidHistory/<int:pid>", methods=["GET"])
def getPidHistory(pid):
    result = monitor.getPidHistoryInfo(pid)
    return result, 201

@app.route("/endMonitors", methods=["POST"])
def endMonitors():
    monitor.endAllMonitors()
    return {'result':True}, 201


@app.route("/endProcess/<int:pid>", methods=["POST"])
def endProcess(pid):
    monitor.endProcess(pid)
    return {'result':True}, 201


@app.route("/killMonitor/<int:pid>", methods=["POST"])
def killMonitor(pid):
    res = monitor.killMonitor(pid)
    return {'result':res}, 201