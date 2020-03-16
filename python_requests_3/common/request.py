import os,requests,logging
from common import opmysql
from public import config


class RequestInterface():
    def __new_param(self,param):
        try:
            if isinstance(param,str) and param.startswith('{'):
                new_param = eval(param)
            elif param == None:
                new_param = ''
            else:
                new_param = param
        except Exception as error:
            new_param = ''
            logging.basicConfig(filename=config.scr_path + '/log/syserror.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)
        return new_param
    def __http_post(self,interface_url,headerdata,interface_param):
        """

        :param interface_url: 接口地址
        :param headerdata: 请求头文件
        :param interface_param: 请求参数
        :return:
        """
        try:
            if interface_url !='':
                temp_interface_param = self.__new_param(interface_param)
                response = requests.post(url=interface_url,data=temp_interface_param,headers=headerdata,verify=False,timeout =10)
                if response.status == 200:
                    durime = (response.elapsed.microseconds)/1000
                    result = {'code':'0000','message':'成功','data':response.text}
                else:
                    result = {'code':'2004','message':'接口返回状态错误','data':[]}
            elif interface_url == '':
                result = {'code':'2002','message':'接口地址参数为空','data':[]}
            else:
                result = {'code':'2003','message':'接口地址错误','data':[]}
        except Exception as error:
            result = {'code':'9999','message':'系统异常','data':[]}
            logging.basicConfig(filename=config.scr_path + '/log/syserror.log', level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)
        return result

    def __http_get(self,interface_url,headerdata,interface_param):
        try:
            if interface_url != '':
                temp_interface_param = self.__new_param(interface_param)
                if interface_url.endsiwtch('?'):
                    requrl = interface_url + temp_interface_param
                else:
                    requrl = interface_param + '?' + temp_interface_param
                response = requests.get(url=requrl,headers=headerdata,verify=False,timeout=10)
                if response.status_code ==200:
                    durtime = (response.elapsed.microseconds)/1000
                    result = {'code':'0000','message':'成功','data':response.text}
                else:
                    result = {'code':'3004', 'message': '接口返回状态错误', 'data':[]}
            elif interface_url =='':
                result = {'code': '3002', 'message': '接口地址参数为空', 'data': []}
            else:
                result = {'code': '3002', 'message': '接口地址错误', 'data': []}
        except Exception as error:
            result = {'code': '9999', 'message': '系统异常', 'data': []}
            logging.basicConfig(filename=config.scr_path + '/log/syserror.log', level=logging.DEBUG,                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)
        return result
    def http_request(self,interface_url,headerdata,interface_param,request_type):
        """

        :param interface_url:
        :param headerdata:
        :param interface_param:
        :param request_type:
        :return:
        """
        try:
            if request_type =='get' or request_type == 'GET':
                result = self.__http_get(interface_url,headerdata,interface_param)
            elif request_type=='post' or request_type == 'POST':
                result = self.__http_post(interface_url,headerdata,interface_param)
            else:
                result = {'code': '10000', 'message': '请求类型错误', 'data': request_type}
        except Exception as error:
            result = {'code': '10000', 'message': '系统异常', 'data': []}
            logging.basicConfig(filename=config.scr_path + '/log/syserror.log', level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(error)
        return result








