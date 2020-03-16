import json,os,logging
from common import opmysql
from public import config
operation_db = opmysql.OperationDBInterface()
class compareparam():
    def __init__(self,params_interface):
        self.params_interface = params_interface
        self.id_class = params_interface['id']
        self.result_list_response = []
        self.params_to_compare = params_interface['params_to_compare']
