import requests,json,unittest,hashlib
from datetime import *
class port_time(unittest.TestCase):
    def setUp(self):
        url = 'http://www.xxx.com/query'
    def test_login(self):
        password = hashlib.md5(b"123456").hexdigest()
        form_data = {'username':'xxx','password':password}
        login_response = requests.post(self.url,data=form_data)
        self.assertEqual(login_response.text['flag'],'success')
    def test_product(self):
        form_data = {'serverid':1333002,'product_type':0,'product_stafe':1}
        product_response= requests.post(url=self.url,data=form_data)
        self.assertEqual(product_response.text['total'],9)

    def suite(self):
        suite = unittest.makeSuite(port_time('test'))
        return suite
if __name__=='__main__':
    p_t = port_time()
    runner = unittest.TextTestRunner()
    runner.run(p_t.suite())
