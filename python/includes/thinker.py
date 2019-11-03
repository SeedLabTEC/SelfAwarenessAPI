import json
from decimal import Decimal
import os
import time
import signal
from multiprocessing import Process
from subprocess import call

global logpath
global pathToAnalisys
pathToAnalisys = "./includes/SAMMonitor "
logpath = "/usr/SAM/Model/"
global myPid
myPid = 0

def getpid():
    global myPid
    return myPid


def analisysProcess(pid):
    global myPid
    global pathToAnalisys
    if os.fork() != 0:
        return
    myPid = os.getpid()
    print("pid", myPid)
    print("ppid", os.getppid())
    os.system(pathToAnalisys+str(pid))


def startProcess(pid):
    p = Process(target=analisysProcess,args=(pid,))
    p.start()
    print('exiting main')
    return os.getpid()



def createJson(config):
    memParams = config["cpu"]
    cpuParams = config["mem"]
    powerParams = config["power"]
    pid = config["pid"]
    jsonTem = {
        "upperPower":float(powerParams[1]),
        "lowerPower": float(powerParams[0]),
        "upperFreq": 800,
        "lowerFreq": 700,
        "upperCores":4.0,
        "lowerCores":1.0,
        "upperCPU": float(cpuParams[1]),
        "lowerCPU": float(cpuParams[0]),
        "upperMem": float(memParams[1]),
        "lowerMem": float(memParams[0]),
        "pid":int(pid)
    }
    return jsonTem

def defineParameters(config):
    global logpath
    #data = json.load(config)
    jsonValue = createJson(config)
    f = open(logpath+str(config["pid"])+".json", "w")
    if(f is None):
        return False
    f.write(str(jsonValue))
    f.close()
    print(config)
    return True



