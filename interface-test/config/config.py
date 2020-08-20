#!/usr/bin/env python
# encoding: utf-8
from configparser import ConfigParser
import os

class Config:
    def __init__(self):
        self.cp=ConfigParser()
        #path=os.path.join(os.path.abspath(os.path.dirname('.')),'db.cfg')
        path=r"D:\work_space\python_space\interface-test\config\db.cfg"
        #print(path)
        self.cp.read(path)
    def interface_db(self):
        section=self.cp.sections()[0]
        host=self.cp.get(section,"host")
        port=self.cp.getint(section,"port")
        user=self.cp.get(section,"user")
        password=self.cp.get(section,"password")
        db=self.cp.get(section,"db")
        charset=self.cp.get(section,"charset")
        db_data=[host,port,user,password,db,charset]
        # print(db_data,type(db_data))
        return db_data


    def test_db(self):
        section = self.cp.sections()[1]
        host = self.cp.get(section, "host")
        port = self.cp.getint(section, "port")
        user = self.cp.get(section, "user")
        password = self.cp.get(section, "password")
        db = self.cp.get(section, "db")
        charset = self.cp.get(section, "charset")
        db_data = [host, port, user, password, db, charset]
        return db_data

    def uat_db(self):
        section = self.cp.sections()[2]
        host = self.cp.get(section, "host")
        port = self.cp.getint(section, "port")
        user = self.cp.get(section, "user")
        password = self.cp.get(section, "password")
        db = self.cp.get(section, "db")
        charset = self.cp.get(section, "charset")
        db_data = [host, port, user, password, db, charset]
        return db_data

    def test_ip(self):
        section = self.cp.sections()[3]
        paycore_ip = self.cp.get(section, "paycore_ip")
        paygw_ip = self.cp.get(section, "paygw_ip")
        ip_data = [paycore_ip, paygw_ip]
        return ip_data

    def uat_ip(self):
        section = self.cp.sections()[3]
        paycore_ip = self.cp.get(section, "paycore_ip")
        paygw_ip = self.cp.get(section, "paygw_ip")
        ip_data = [paycore_ip, paygw_ip]
        return ip_data

if __name__=="__main__":
   a=Config()
   print(a.interface_db())
   #print(a.test_db())
   #print(a.uat_db())
   #print(a.test_ip())
   #print(a.uat_ip())