import threading
from datetime import *
from time import sleep


def test():
    sleep(1)
    x = 0
    while(x==0):
        print(datetime.now())
def thd():
    Threads = []
    for i in range(20):
        t = threading.Thread(target=test())
        Threads.append(t)
        t.setDaemon(True)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join(2)
if __name__ == '__main__':
    thd()
    print('end')