import json
from decimal import Decimal
import os
import time
import signal
from multiprocessing import Process
from subprocess import call

global logpathModel
global logpath
global pathToAnalisys
pathToAnalisys = "./includes/SAMMonitor "
logpathModel = "/usr/SAM/Model/"
logpath = "/var/log/SAM/results/"
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
    saveAnalisysData(os.getpid(),pid)
    os.system(pathToAnalisys+str(pid))


def startProcess(pid):
    p = Process(target=analisysProcess,args=(pid,))
    p.start()
    print('exiting main')
    return os.getpid()

def addParamter(data,element):
    data = data + str(element)+':'
    return data

def createJson(config):
    data = ""
    memParams = config["mem"]
    cpuParams = config["cpu"]
    powerParams = config["power"]
    pid = config["pid"]
    data = addParamter(data,pid)
    data = addParamter(data,powerParams[1])
    data = addParamter(data,powerParams[0])
    data = addParamter(data,"0")
    data = addParamter(data,"0")
    data = addParamter(data,"0")
    data = addParamter(data,"0")
    data = addParamter(data,cpuParams[1])
    data = addParamter(data,cpuParams[0])
    data = addParamter(data,memParams[1])
    data = addParamter(data,memParams[0])
    data = addParamter(data,"\n")
    return data

    ###pid:1515,upperPower:20,lowerPower: 10,upperFreq: 900,lowerFreq: 600,upperCores:4,lowerCores:1,upperCPU: 20,lowerCPU: 10,upperMem: 20,lowerMem: 10

def defineParameters(config):
    global logpathModel
    #data = json.load(config)
    jsonValue = createJson(config)
    f = open(logpathModel+str(config["pid"])+".txt", "w")
    if(f is None):
        return False
    f.write(str(jsonValue))
    f.close()
    print(config)
    return True


def saveAnalisysData(pidAnalisys,pidTask):
    global logpath
    f = open(logpath+"analisysHistory.txt", "a")
    f.write(str(pidTask)+":"+str(pidAnalisys)+"\n")
    f.close()