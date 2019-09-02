from flask import Flask, jsonify
import subprocess
import os, sys, stat
class process:
    id = 0
    memory = 0
    def __init__(self):
        self.id = 0
        self.memory = 0
        print("New Process")
def setPermissions(filename):
    os.chmod("./files/"+filename,0o777)

def runProcess(filename):
    setPermissions(filename)
    tmp=subprocess.call("./files/"+filename)
    print("Result: ",tmp)

#setPermissions('testapp')