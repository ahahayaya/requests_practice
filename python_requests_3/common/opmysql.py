import logging,os,pymysql
from public import config

class OperationDBInterface():
    def __init__(self,host_db='localhost',user_db='root',password='ab123456',name_db='homework',port_db=3306,link_type=0):
        """
        :param host_db: 数据库主机
        :param user_db: 登录数据库的用户
        :param password: 用户密码
        :param name_db: 使用的数据库
        :param port_db: 数据库端口号
        :param link_type: 链接类型，用于设置输出数据是元祖还是字典，默认是字典
        """
        try:
            if link_type==0:
                self.conn=pymysql.connect(host=host_db,user=user_db,passwd=password,db=name_db,port=port_db,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
                self.cur = self.conn.cursor()
            else:
                self.conn=pymysql.connect(host=host_db,user=user_db,passwd=password,db=name_db,port=port_db,charset='utf8')
                self.cur = self.conn.cursor()
        except pymysql.Error as e:
            print('创建数据库连接失败|Mysql Error %d %s'%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.scr_path+'/log/syserror.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)

    def op_sql(self,condition):
        """

        :param condition: sql语句
        :return:
        """
        try:
            self.cur.execute(condition)
            self.conn.commit()
            result = {'code':'0000','message':'执行通用操作成功','data':[]}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code':'9999','message':'执行通用操作异常','data':[]}
            print('数据库连接错误| op_sql %d %s'%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.scr_path+'/log/syserror.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result
    def select_one(self,condition):
        """

        :param condition:SQL 语句
        :return: 字典格式的单条查询结果
        """
        try:
            rows_affect = self.cur.execute(condition)
            if rows_affect>0:
                #获取一条结果
                results = self.cur.fetchone()
                result = {'code':'0000','message':'执行单条查询操作成功','data':results}
            else:
                result = {'code':'0000','message':'执行单条查询操作成功','data':[]}
            print(self.cur.fetchone())
        except pymysql.Error as e:
            self.conn.rollback()
            result ={'code':'9999','message':'执行单条查询操作异常','data':[]}
            print('数据库错误| select_one %d : %s'%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.scr_path+'/log/syserror.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result
    def select_all(self,condition):
        """

        :param condition: sql语句
        :return:
        """
        try:
            rows_affect = self.cur.execute(condition)
            if rows_affect>0:
                self.cur.scroll(0,mode='absolute')
                results = self.cur.fetchall()
                result = {'code':'0000','message':'执行批量查询操作成功','data':results}
                print(result)
            else:
                result ={'code':'0000','message':'执行批量查询操作成功','data':[]}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code':'9999','message':'执行批量查询操作异常','data':[]}
            print('数据库错误| select_all %d %s'%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.scr_path + '/log/syserror.log',level = logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result
    def insert_data(self,condition,params):
        """

        :param condition: insert sql语句
        :param params: 插入的数据形式
        :return:
        """
        try:
            results = self.cur.executemany(condition,params)
            self.conn.commit()
            result = {'code':'0000','message':'插入数据操作成功','data':results}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code':'9999','message':'插入数据操作异常','data':[]}
            print('数据库错误| insert_data %d %s'%(e.args[0],e.args[1]))
            logging.basicConfig(filename= config.scr_path+'/log/syserror.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d %(levelname)s %(message)s]')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result
    def __del__(self):
        if self.cur != None:
            self.cur.close()
        if self.conn != None:
            self.conn.close()
if __name__ == '__main__':
    test = OperationDBInterface()
    test.select_all('select * from config_total')





