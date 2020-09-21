#!/usr/bin/env python
# encoding: utf-8
#由于异步返回结果，只能通过订单号在数据库查询出最终交易状态来判断，接口请求的最终结果
import json
import time
from util.oper_testdb import Oper_testdb

class Get_order_status:
    def __init__(self):
        self.testdb=Oper_testdb()
    def get_order_status(self,payOrderNo):
        time.sleep(8)
        if int(payOrderNo[1:2])==8:
            #提现订单查询订单状态
            order_status=self.testdb.paygw_sel_withdraw(payOrderNo)
        else:
            payOrderNo1=int(payOrderNo)+1
            channel_tran_no=(len(payOrderNo)-len(str(payOrderNo1)))*"0" + str(payOrderNo1)
            #print(channel_tran_no)
            try:
                order_status=self.testdb.paygw_sel_depute_trans(channel_tran_no)
            except:
                order_status=self.testdb.paygw_sel_deduct_trans(channel_tran_no)

        return order_status
if __name__=="__main__":
    a=Get_order_status()
    a.get_order_status("022020091615463100000102")
