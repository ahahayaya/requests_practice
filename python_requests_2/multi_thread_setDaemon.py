import threading
from datetime import *
def test():
    print('this setDaemon thread')
def thd():
    Threads = []
    for i in range(10):
        t = threading.Thread(target=test())
        Threads.append(t)
        t.setDaemon(True)
    for t in Threads:
        t.start()
thd()
print('end')
