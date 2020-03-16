import threading
from datetime import *
THREAD_NUM=2
ONE_WORKER_NUM =2
def test():
	print(datetime.now())
def working():
	global ONE_WORK_NUM
	for i in range(0,ONE_WORK_NUM):
		test()
def thd():
	global THREAD_NUM
	Threads=[]
	for i in range(0,THREAD_NUM):
		t = threading.Thread(target=working,name="T"+str(i))
		t.setDaemon(True)
		Threads.append(t)
	for t in Threads:
		t.start()
	for t in Threads:
		t.join(2)
if __name__=="__main__":
	thd()
	print("end")