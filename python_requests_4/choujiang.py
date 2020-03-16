import threading,requests
num = 3
thread_num = 5

#多用户抽奖
def choujiang():
    url = "http://www.xxx.com/choujiang"
    with open('phone.txt','r') as f:
        for phone in f:
            form_data = {'phone':phone,'activityGuid':1001}
            choujiang_response = requests.post(url=url,data=form_data)
            print(choujiang_response.text)
#多用户多次抽奖
def choujiang_num():
    global num
    for i in range(num):
        choujiang()
#多用户多次同时抽奖
def thd():
    global thread_num
    Threads = []
    for i in range(thread_num):
        t = threading.Thread(target=choujiang_num())
        Threads.append(t)
        t.setDaemon(True)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join(2)
if __name__=='__main__':
    thd()
    print('end')