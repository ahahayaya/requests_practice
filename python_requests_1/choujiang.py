import requests
phone="13012345678"
id = 1000
form = {"mobilePhone":phone,"activityGuid":id}
url = "http://www.xxx.com/management/winningrecord/newluckDraw"
r = requests.post(url,data=form)
print(r.text)