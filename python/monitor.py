import sammonitor as samm
import os
import time

def execute(pid):
    if os.fork() != 0:
        return
    print('sub process is running')
    samm.monitorApp(pid)
    print('sub process finished')

def monitorProcess(pid):
    p = Process(target=execute)
    p.start()
    p.join()
    print('exiting main')
    exit(0)