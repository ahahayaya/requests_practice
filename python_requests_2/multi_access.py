import threading
from datetime import *
def test():
    print(datetime.now())
def thd():
    Threads = []
    for i in range(10):
        t = threading.Thread(target=test())
        Threads.append(t)
    for t in Threads:
        t.start()
if __name__ =='__main__':
    thd()