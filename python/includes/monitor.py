import sammonitor as samm
import os
import time
from multiprocessing import Process

def monitorProcess(pid):
    if os.fork() != 0:
        return
    samm.monitorApp(pid)

def startProcess(pid):
    p = Process(target=monitorProcess,args=(pid,))
    p.start()
    print('exiting main')
    return True


def jsonFormat(array):
    jsonResult = {
        "pid":array[0],
        "memBytes":array[1],
        "memPercen":array[2],
        "cpuPercen":array[3],
        "powerPercen":array[4],
        "timestamp":array[5]
    }
    return jsonResult

def processFile(pid,isAll):
    name = ""
    path = "results/"
    if(isAll):
        name = path+str(pid)+"all.txt"
    else:
        name = path+str(pid)+".txt"
    file = open(name,"r")
    results = []
    for line in file:
        fields = line.split(":")
        print(fields)
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
    
