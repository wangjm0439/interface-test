#!/usr/bin/env python
# encoding: utf-8
import pymysql
from config.config import Config

class Oper_testdb:
    def __init__(self):
        config = Config()
        testdb = config.test_db()
        self.db = pymysql.connect(host=testdb[0], port=testdb[1], user=testdb[2], password=testdb[3],db=testdb[4], charset=testdb[5])
        self.cursor = self.db.cursor()

    def paygw_sel_deduct_trans(self,payOrderNo):
        '''代扣订单状态查询'''
        sql="SELECT t.resp_code FROM paygw.deduct_trans t where t.channel_trans_no= '{0}'".format(payOrderNo)
        self.cursor.execute(sql)
        data=self.cursor.fetchone()[0]#获取单个值
        self.db.commit()
        print(data)
        return data

    def paygw_sel_withdraw(self,payOrderNo):
        '''提现订单状态查询'''
        sql="select c.resp_code from paycore.bank_card_order a,paycore.bank_card_detail b,paygw.depute_trans c where a.capital_order_no='{0}' and a.card_order_no=b.card_order_no and b.gw_trans_no=c.trans_no"\
            .format(payOrderNo)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()[0]  # 获取单个值
        self.db.commit()
        print(data)
        return data
    def paygw_sel_depute_trans(self,payOrderNo):
        '''查询代付订单状态'''
        sql = "SELECT t.resp_code FROM paygw.depute_trans t where t.channel_trans_no= '{0}'".format(payOrderNo)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()[0]  # 获取单个值
        self.db.commit()
        #print(data)
        return data


if __name__=="__main__":
    a=Oper_testdb()
    #a.paygw_sel_deduct_trans("022020091113544800000021")
    #a.paygw_sel_withdraw("082020091117041100000008")
    a.paygw_sel_depute_trans("012020091118020000000007")




        
    


