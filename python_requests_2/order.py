import datetime
import hashlib
import json
import unittest,requests
from datetime import timedelta

username = 'xxx'
password = hashlib.md5(b"123456").hexdigest()
url = "http://xxx.com"
form_data = {'username':username,"password":password}
login_response = requests.post(url,data=form_data)
assert login_response.text =='登录成功'
c = login_response.cookies

def make_order():
    global c
    url = "http://www.xxx.ajax/create_order"
    form_data = {'resturant_id':111,'menu_items_toall':'12.00','menu_items_data':"[{'id':111,'p':'2','q':6}]",'delivery_fee':'3.00'}
    make_response = requests.post(url,data=form_data,cookies=c)
    id = json.loads(make_response.text)['order_id']
    assert id !=""
    return id
def place_order(id):
    global c
    global username
    time = datetime.now()+timedelta(hours=1)
    url = 'http://www.xxx.com/ajax/place_order/'
    form_data = {'order_id':id,'customer_name':'xxx','mobile_number':username,'deliver_address':'xxxx','preorder':'yes','preorder_time':time,'pay_type':'cash'}
    place_response = requests.post(url=url,data=form_data,cookies=c)
    assert place_response.text == "success"
    print('订餐成功')

def sms():
    result = ask_sms()
    if result == '{"status":"ok","need_sms":"False"}':
        return
    else:
        request_sms()
        code = get_sms()
        validate_sms(code)
def ask_sms():
    global c,username
    url = 'http://www.xxx.com/ajax/is_order_need'
    form_data = {'mobile':username}
    ask_response = requests.post(url=url,data=form_data,cookies=c)
    res =ask_response.text
    return res
def request_sms():
    global c,username
    url = "http://www.xxx.com/ajax/common_sms_code"
    form_data = {'mobile':username}
    sms_response = requests.post(url=url,data=form_data,cookies=c)
    res = sms_response.text
    assert res =='True'

def get_sms():
    global username
    url1= "http://www.xxx.com/manager/login.action"
    form_data = {'user':'admin','pwd':0000}
    login_response = requests.post(url=url1,data=form_data)
    cookie = login_response.cookies
    url2 = "http://www.xxx.com/manager/smsmanager"
    form_data2 = {'phone':username}
    code_response = requests.post(url=url2,data=form_data2,cookies=cookie)
    code = code_response.text
    assert code != ""
    return code

def validate_sms(code):
    global c,username
    url = "http://www.xxx.com/ajax/validate_sms_code/"
    form_data = {'mobile':username,'sms_code':code}
    validate_response = requests.post(url=url,data=form_data,cookies=c)
    res = validate_response.text
    assert code == 'True'

