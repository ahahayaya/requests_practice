import unittest,requests
class logintest(unittest.TestCase):
    def setUp(self):
        self.url = "http://xxx.com"
    def testloginsucc(self):
        data = {'username':'xxx','password':'xxx'}
        r = requests.post(self.url,data=data)
        return self.assertEqual(r.text,"登录成功")
    def testloginnull(self):
        data ={'username':'xxx','password':'xxx'}
        r = requests.post(url=self.url,data=data)
        return self.assertEqual(r.text,'账户名不能为空')
    def testloginwrong(self):
        data = {'username':'xxx','password':'xxx'}
        r = requests.post(url=self.url,data=data)
        return self.assertEqual(r.text,'账户名或密码错误')

def suite():
    testsuite = unittest.TestSuite()
    testsuite.addTest(logintest('testloginsucc'))
    testsuite.addTest(logintest('testloginnull'))
    testsuite.addTest(logintest('testlginwrong'))
    return testsuite
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
