import unittest,requests
class logintest(unittest.TestCase):
    def setUp(self):
        self.url = "https://passport.baidu.com/"
    def testlogin1(self):
        form = {'username':'13012345678','password':111111}
        r = requests.post(self.url,data=form)
        self.assertEqual(r.text,'登录成功')
    def testlogin2(self):
        form = {'username':'13012345678','password':''}
        r = requests.post(self.url,data=form)
        self.assertEqual(r.text,'密码不能为空')
    def testlogin3(self):
        form = {'username':'13012345678','password':'222'}
        r = requests.post(self.url,data=form)
        self.assertEqual(r.text,'账户名或密码错误')
    def testlogin4(self):
        form = {'username':' ','password':'222'}
        r = requests.post(self.url,data=form)
        self.assertEqual(r.text,'账户名不能为空')
# 把logintest类中所有以test开头的函数都加入到用例集
def suite():
    logintestcase = unittest.makeSuite(logintest,'test')
    return logintestcase
if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())



