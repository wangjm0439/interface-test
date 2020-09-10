#!/usr/bin/env python
# encoding: utf-8
import json
import requests


def req_single(url,data,method):
    if method=='post':
        res=requests.post(url,data=json.dumps(data)).json()
    else:
        res=requests.get(url,data=json.dumps(data)).json()
    return res
