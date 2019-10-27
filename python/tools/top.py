from subprocess import call
import os, sys, stat

def runTop(filepath):
    os.chmod(filepath,0o777)
    rc = call(filepath)
    return rc

def assign(data):
    data = data.split()
    dataJson = {
        'pid':data[0],
        'user':data[1],
        'pr':data[2],
        'ni':data[3],
        'virt':data[4],
        'res':data[5],
        'shr':data[6],
        's':data[7],
        'cpu':data[8],
        'mem':data[9],
        'time':data[10],
        'command':data[11]

    }
    return dataJson

def fileRefactor(filepath):
    result = []
    with open(filepath, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            result.append(assign(i))
        f.close()
    return result

def deleteFile(filepath):
    os.remove(filepath)



