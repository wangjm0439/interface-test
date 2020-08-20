#!/usr/bin/env python
# encoding: utf-8
from flask import request
from werkzeug.utils import secure_filename
import os

#f = request.files['file']
basepath = os.path.abspath(os.path.dirname('.'))  # 当前文件所在路径

print(os.path.join(basepath,"run","upload"))