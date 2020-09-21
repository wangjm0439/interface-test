#!/usr/bin/env python
# encoding: utf-8
import json
import requests
import random

def req_single(url,data,method):
    if isinstance(data,str):
        data=eval(data)
        #print(type(data))
    data["outBizNo"]=random.randint(10000000,999999999)
    if method=='post':
        res1=requests.post(url,data=json.dumps(data)) #请求参数必须为json格式否则不能成功请求，字典格式请求失败未报错
        code=res1.status_code
        res=res1.text
        res_time=res1.elapsed.total_seconds()
        #print(res_time)
    else:
        res1=requests.get(url,data=json.dumps(data)).text
        code = res1.status_code
        res = res1.text
        res_time = res1.elapsed.total_seconds()
    #print("响应结果:",res)
    return res,code,res_time #同时返回3个参数，返回参数是一个tuple

if __name__=="__main__":
    data= {
    "cardHolderName":"通联提现",
    "cardNo":"622484848393030244",
    "bizOrderNo":"202001021627301269414101",
    "certNo":"110101199607280175",
    "bizDate":"20200624",

    "certType":"01",
    "cityCode":"510100",
    "epFlag":"P",
    "notifyKey":"paycore.xwzf.depute",

    "outBizNo":"",
    "productCode":"tx001",
    "productLine":"xw0201",
    "provinceCode":"510000",
    "bankCode":"0102",
    "bankName":"招商银行",
    "remark":"代付123",
    "sceneCode":"01",
    "systemId":"xwzf",
    "transAmount":1,
    "uuid":"",
    "payCardNo":"1234"
}
    url="http://10.100.30.27:8079/withdraw/send"
    method="post"
    req_single(url, data, method)
    print(isinstance(data,str))

