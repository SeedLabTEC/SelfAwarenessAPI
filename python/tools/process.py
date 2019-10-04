from flask import Flask, jsonify
import subprocess
from subprocess import check_output
import os, sys, stat
from threading import Thread
import ctypes
libc = ctypes.cdll.LoadLibrary('libc.so.6') 
cpu = ctypes.CDLL('libraries/libCpuUsage.so')  
SYS_gettid = 186
class process(Thread):
    threadId = 0
    memory = 0
    state = 0
    name= ""
    appId = 0 
    def __init__(self,filename):
        Thread.__init__(self)
        self.threadId = 0
        self.memory = 0
        self.state = 0
        self.appId = 0
        self.name = filename
        print("New Process")
    def getThreadId(self):
        self.threadId = libc.syscall(SYS_gettid)
        self.appId = self.threadId+1
    def setPermissions(self):
        os.chmod("./files/"+self.name,0o777)

    def stopApp(self,pid):
        tmp=subprocess.call("kill -STOP "+str(pid))
        print("Result: ",tmp)
    
    def analizeCpu(self):
        #cpu.getCpuUsage.argtypes(ctypes.c_int) 
        returnVale = cpu.getCpuUsage(self.appId)
        print(returnVale)

    def runSelectedApp(self):       
        self.getThreadId()
        print('pid',self.appId)
        self.setPermissions()
        tmp=subprocess.call("./files/"+self.name)
        print("Result: ",tmp)

    def getPid(self,filename):
        return map(int,check_output(["pidof",filename]).split())


    def run(self):
        self.runSelectedApp()

#setPermissions('testapp')