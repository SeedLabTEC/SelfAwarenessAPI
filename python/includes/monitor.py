import sammonitor as samm
import os
import time
import signal
from multiprocessing import Process
from subprocess import call

global myPid
myPid = 0
global logpath
logpath = "/var/log/SAM/results/"
def getpid():
    global myPid
    return myPid


def monitorProcess(pid):
    global myPid
    if os.fork() != 0:
        return
    myPid = os.getpid()
    print("pid", myPid)
    print("ppid", os.getppid())
    saveMonitorData(os.getpid(),pid)
    samm.monitorApp(pid)


def startProcess(pid):
    p = Process(target=monitorProcess,args=(pid,))
    p.start()
    print('exiting main')
    return os.getpid()

def analisysProcess(pid):
    global myPid
    if os.fork() != 0:
        return
    myPid = os.getpid()
    print("pid", myPid)
    print("ppid", os.getppid())
    saveAnalisysData(os.getpid(),pid)
    rc = call("./includes/SAMMonitor")
    print(rc)

def initAnalisys(pid):
    p = Process(target=monitorProcess,args=(pid,))
    p.start()
    print('exiting main')
    return os.getpid()


def jsonFormat(array):
    jsonResult = {
        "pid":array[0],
        "memBytes":array[1],
        "memPercen":array[2],
        "cpuPercen":array[3],
        "powerPercen":array[5],
        "processor":array[4],
        "timestamp":array[6],
        "flag":array[7].replace('\n', '')
    }
    return jsonResult

def processFile(pid,isAll):
    global logpath
    name = ""
    if(isAll):
        name = logpath+str(pid)+"all.txt"
    else:
        name = logpath+str(pid)+".txt"
    file = open(name,"r")
    results = []
    for line in file:
        fields = line.split(":")
        #print(fields)
        results.append(jsonFormat(fields))   
    file.close()
    return results

def getPidInfo(pid):
    print("get info")
    return processFile(pid,False)[0]
    

def getPidHistoryInfo(pid):
    print("get hitory info")
    return  {
        "result":processFile(pid,True)
    }


def readMonitors():
    file = open(logpath+"monitorHistory.txt","r")
    results = []
    for line in file:
        data = line
        data = data.replace('\n','')
        fields = data.split(":")
        results.append(fields)   
    file.close()
    return results

def killMonitor(pid):
    file = open(logpath+"monitorHistory.txt","r")
    for line in file:
        data = line
        data = data.replace('\n','')
        fields = data.split(":")
        if(int(fields[0])==pid):
            endProcess(int(fields[1]))
            return True  
    file.close()
    return False


def endAllMonitors():
    monitors = readMonitors()
    for monitor in monitors:    
        try:
            print("Killing ",monitor[1])
            os.kill(int(monitor[1]), signal.SIGKILL)
            os.remove(logpath+"monitorHistory.txt")
        except:
            print("No such process "+monitor[1])

def endAllProcess():
    monitors = readMonitors()
    for monitor in monitors:    
        try:
            print("Killing ",monitor[0])
            os.kill(int(monitor[0]), signal.SIGKILL)
            os.remove(logpath+"monitorHistory.txt")
        except:
            print("No such process "+monitor[1])

def endProcess(pid):
     os.kill(pid, signal.SIGKILL)

def saveMonitorData(pidMonitor,pidTask):
    f = open(logpath+"monitorHistory.txt", "a")
    f.write(str(pidTask)+":"+str(pidMonitor)+"\n")
    f.close()


