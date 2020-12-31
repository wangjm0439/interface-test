#!/usr/bin/env python
# encoding: utf-8
from flask import request
from werkzeug.utils import secure_filename
import os
import json

#f = request.files['file']
basepath = os.path.abspath(os.path.dirname('.'))  # 当前文件所在路径

print(os.getcwd())
a=(29, '通联-提现', 'url', '', '2020/08/21 17:59:16', 'data', 'post', '丁旭', '单笔代付-交易成功', '200', '{"username":"Demo001","passwd":"Test123456!"}')
b="http://10.100.30.27:8092/inner/paycore/acctBalanceQry"
c="acctBalanceQry"
if c in b:
    print("正确")
d=('{"header":{"channelCode":"paycore","channelTransNo":"20200709000000022000","channelDateTime":"20200709173404","transCode":"acctBalanceQry","success":"true","errorCode":"","errorMsg":""},"body":{"bizStatus":"SUCCESS","respCode":"G000","respMsg":"交易成功","acctNo":"200604000008016001","rptDate":"","hisBalance":"","balance":"-297020316.44"}}', 200, 0.23525)
print(json.loads(d[0])["body"]["respCode"])