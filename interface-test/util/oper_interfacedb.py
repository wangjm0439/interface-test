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
        '''查询展示interfaceinfo'''
        sql="select * from interfaceInfo"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        #print(len(data))
        self.db.commit()
        return data

    def del_interfaceinfo(self,id):
        '''删除'''
        sql="delete from interfaceInfo where id='{0}'".format(id)
        self.cursor.execute(sql)
        self.db.commit()

    def sel_id_interfaceinfo(self,id):
        sql="select * from interfaceInfo where id='{0}'".format(id)
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        #print(data[0])
        return data[0]
    def sel_interfacerespond(self):
        sql="SELECT * FROM interfacerespond"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        self.db.commit()
        #print(data)
        return data

    def insert_interfacerespond(self,intername,interaddr,requestparam,respondbody,code,respondtime,descp,result):
        tt = time.strftime("%Y/%m/%d %H:%M:%S")
        #print(tt)
        sql="insert into interfacerespond (intername,interaddr,requestparam,respondbody,`code`,respondtime,inputtime,descp,result) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')"\
            .format(intername,interaddr,requestparam,respondbody,code,respondtime,tt,descp,result)
        self.cursor.execute(sql)
        self.db.commit()

    def update_interfaceinfo(self,id,intername,descp,interaddr,header,param,option,author,expected,account):
        '''编辑窗口更新数据'''
        sql="update  interfaceinfo set intername='{1}',descp='{2}',interaddr='{3}',header='{4}',param='{5}',`option`='{6}',author='{7}',expected='{8}',account='{9}'  where id='{0}'".format(id,id,intername,descp,interaddr,header,param,option,author,expected,account)
        self.cursor.execute(sql)
        self.db.commit()
        #print("data:",data)


if __name__=="__main__":
    a=Oper_sql()
    #a.del_interfaceinfo(23)
    #a.sel_id_interfaceifo(29)
    #a.insert_interfacerespond("aa","aa","aa","aa","aa","0","aa","aa")
    #a.sel_edit_interfaceinfo(4)
    #a.update_interfaceinfo(5,"aa","aa","aa","aa","aa","aa","0","aa","aa")
    a.select_interfaceinfo()



