import requests,hashlib,json
from datetime import *
username = '13012345678'
password = 'xxxx'
url = 'http://www.xxx.com/ajax/user_login'
form_data = {'username':username,'password':password}
login_response = requests.post(url=url,data=form_data)
assert login_response.text == 'success'
c = login_response.cookies

#下单接口
def make_order():
    global c
    url = "http://www.xxx.com/ajax/create_order"
    form_data = {'restaurant_id':111,'menu_items_total':'12.00','menu_items_data':"['id':1111,'p':'2','q':'4']",'delivery_fee':'3.00'}
    make_response = requests.post(url=url,data=form_data,cookies=c)
    res = make_response.text
    id = json.load(res)['order_id']
    assert id !=''
    return id
#处理订单
def place_order(id):
    global c,username
    time = datetime.now()+timedelta(hours=1)
    url ="htpp://www.xxx.com/ajax/place_order"
    form_data = {'order_id':id,'customer_name':'xxx','mobile_number':username,'delivery_address':'xxx'}
    place_response = requests.post(url=url,data=form_data,cookies=c)
    res = place_response.text
    assert res =='success'
    print('订餐成功')
#是否需要验证码，res为False不要验证码，res返回True需要验证码
def ask_sms():
    global c,username
    url = "http://www.xxx.com/ajax/is_order_need"
    form_data = {'mobile':username}
    ask_response = requests.post(url=url,data=form_data,cookies=c)
    res = ask_response.text
    return res

#请求发送短信到手机
def request_sms():
    global c,username
    url = "http://www.xxx.com/ajax/common_sms_code"
    form_data = {'mobile':username}
    sms_response = requests.post(url=url,data=form_data,cookies=c)
    res = sms_response.text
    assert res == 'True'
#获取验证码
def get_sms():
    global username
    url = 'http://www.xxx.com/manager/login.action'
    form_data = {'user':'admin','pwd':000}
    login_response = requests.post(url=url,data=form_data)
    cookie = login_response.cookies
    url2= 'http://www.xxx.com/manager/smsmanager'
    form_data2 = {'phone':username}
    code_response = requests.post(url=url2,data=form_data2,cookies=cookie)
    code = code_response.text
    assert code !=''
    return code
#输入验证码请求
def validate_sms(code):
    global c,username
    url = 'http://www.xxx.com/ajax/validate_sms_code'
    form_data = {'mobile':username,'sms_code':code}
    validate_response = requests.post(url=url,data=form_data,cookies=c)
    res = validate_response.text
    assert code == 'True'

#订单验证码处理
def sms():
    result = ask_sms()
    if result == "{'status':'ok','need_sms':False}":
        return
    else:
        request_sms()
        code = get_sms()
        validate_sms(code)
if __name__ == '__main__':
    id = make_order()
    sms()
    place_order(id)
