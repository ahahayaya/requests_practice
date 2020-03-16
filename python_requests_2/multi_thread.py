import threading
from datetime import *
def qtest():
    print(datetime.now())
def looptest():
    for i in range(20):
        qtest()
def thd():
    Threads =[]
    for i in range(25):
        t = threading.Thread(target=looptest())
        Threads.append(t)
    for t in Threads:
        t.start()
thd()