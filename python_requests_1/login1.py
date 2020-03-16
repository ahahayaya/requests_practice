import requests,unittest,HTMLTestRunner
class logintest(unittest.TestCase):
    def testlogin1(self):
        url = "https://passport.baidu.com/"
        form ={'username':'13012345678','password':'123456'}
        r = requests.post(url,data = form)
        self.assertEqual(r.text,"登录成功")
    def testlogin2(self):
        url  = "https://passport.baidu.com/"
        form ={'username':'13012345678','password':111111}
        r = requests.post(url,data=form)
        self.assertEqual(r.text,'密码不能为空')
    def testlogin3(self):
        url = "https://passport.baidu.com/"
        form = {'username':'13312345678','password':000000}
        r = requests.post(url,data=form)
        self.assertEqual(r.text,'账号或密码错误')
def suite():
    logintestcase = unittest.TestSuite()
    logintestcase.addTest(logintest('testlogin1'))
    logintestcase.addTest(logintest('testlogin2'))
    logintestcase.addTest(logintest('testlogin3'))
    logintestcase.addTest(logintest('testlogin4'))
    return logintestcase
if __name__ == "__main__":
    with open('resp1.html','wb') as f:
     runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='详情')
    runner.run(suite())