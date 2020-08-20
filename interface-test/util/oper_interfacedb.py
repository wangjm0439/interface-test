#!/usr/bin/env python
# encoding: utf-8
import  pymysql
from config.config import Config
import time
class Oper_sql:
    def __init__(self):
        config=Config()
        portaltest=config.interface_db()
        self.db=pymysql.connect(host=portaltest[0],port=portaltest[1],user=portaltest[2],password=portaltest[3],db=portaltest[4],charset=portaltest[5])
        self.cursor=self.db.cursor()

    def insert_interfaceinfo(self,intername,interaddr,header,param,option,author, descp, expected, account):
        '''interfaceinfo表插入数据'''
        tt=time.strftime("%Y/%m/%d %H:%M:%S")
        sql="insert into interfaceInfo(intername,interaddr,header,param,`option`,author,inputtime, descp, expected, account) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')"\
            .format(intername,interaddr,header,param,option,author,tt,descp,expected,account)
        self.cursor.execute(sql)
        self.db.commit()

    def select_interfaceinfo(self):
        sql="select * from interfaceInfo"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        #print(data)
        self.db.commit()
        return data

if __name__=="__main__":
    a=Oper_sql()
    intername="123"
    interaddr="http://10.100.30.27:8079/withdraw/send"
    header="yy"
    param="hh"
    option="tt"
    author="yy"
    descp="yy"
    expected="yy"
    account="yy"
    #a.insert_interfaceinfo(intername,interaddr,header,param,option,author, descp, expected, account)
    a.select_interfaceinfo()




