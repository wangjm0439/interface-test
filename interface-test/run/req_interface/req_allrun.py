#!/usr/bin/env python
# encoding: utf-8
import requests
import json
from util.oper_interfacedb import Oper_sql
from util.oper_testdb import Oper_testdb
from run.req_interface.req_single import *
from util.order_status import Get_order_status

class Req_allrun:
    def __init__(self):
        self.interfacedb=Oper_sql()
        self.testdb=Oper_testdb()
        self.get_status=Get_order_status()
    def req_allrun(self):
        data=self.interfacedb.select_interfaceinfo()
        for i in range(len(data)):

            interaddr = data[i][2]
            requestparam = data[i][5]
            option = data[i][6]
            #print(interaddr,requestparam,option)
            res_data=req_single(interaddr, requestparam, option)#获取响应参数、状态码、接口响应时间
            payOrderNo = json.loads(res_data[0].replace('\n', '').replace('\t', '').replace('\\', ''))["data"][
                "payOrderNo"]
            print("payOrderNo:", payOrderNo)  # 转化为字典格式并获取订单号
            order_status = self.get_status.get_order_status(payOrderNo)  # 处理订单payOrderNo+1用于在paygw中查询订单状态
            expected = data[i][9]
            print("expected:", expected)
            print("order_status:", order_status)
            if order_status == expected:
                result = 'SUCCESS'
            else:
                result = 'FAIL'
            print("result:", result)
            self.interfacedb.insert_interfacerespond(data[i][1], data[i][2], data[i][5], res_data[0], res_data[1], res_data[2],
                                                  data[i][8], result)

            #print(data[i])

if __name__=="__main__":
    a=Req_allrun()
    a.req_allrun()
