#!/usr/bin/env python
# encoding: utf-8
from flask import request
from werkzeug.utils import secure_filename
import os

#f = request.files['file']
basepath = os.path.abspath(os.path.dirname('.'))  # 当前文件所在路径

print(os.getcwd())
a=(29, '通联-提现', 'url', '', '2020/08/21 17:59:16', 'data', 'post', '丁旭', '单笔代付-交易成功', '200', '{"username":"Demo001","passwd":"Test123456!"}')