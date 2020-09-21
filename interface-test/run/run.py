from flask import Flask,render_template,send_from_directory,url_for,sessions,escape,request
from flask import  make_response,abort,redirect,Response
from config.basis_config import *
from util.oper_interfacedb import Oper_sql
import os
from werkzeug.utils import secure_filename
from util.read_Excel import *
from run.req_interface.req_single import *
from util.order_status import *
from run.req_interface.req_allrun import Req_allrun
import requests
import json

app = Flask(__name__)

upload_file = r"D:\work_space\python_space\interface-test\interface-test\run\uploads"#保存文件路径
#upload_file =os.path.join(os.path.abspath(os.path.dirname('.')),"run","upload")
app.config['UPLOAD_FOLDER'] = upload_file
allow_file = {'xlsx','xls'} #允许上传的文件类型
interface_sql=Oper_sql()
get_status=Get_order_status()
req_allrun=Req_allrun()


@app.route('/',methods=['GET'])
def index():
    result=(name,bug_url,saying)
    return render_template("index.html",result=(result,))
@app.route('/interfaceList',methods=['GET'])
def interface():
    data=interface_sql.select_interfaceinfo()
    return render_template('interfacelist.html',result=(data,))

#文件类型判断
def allow_file_type(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allow_file

@app.route('/uploadfile/',methods=['POST',"GET"])
def upload():
    if request.method == 'POST':
        file=request.files["myf"]#前端页面对应的name属性值
        if file and allow_file_type(file.filename): #and 判断是否有上传的文件，并且文件类型为xls或xlsx
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            read_excel()
            return "<html><p>导入成功</p><a href='interfaceList'>返回待请求接口列表</a></html>"
    return render_template('error.html', result=())

@app.route('/downloadfile',methods=['GET'])
def download_file():
    return send_from_directory(r'D:\work_space\python_space\interface-test\interface-test\util\excel',filename='interfacedata.xlsx',as_attachment=True)

@app.route('/delinterface',methods=['GET','POST'])
#'''删除和执行单条测试用例'''
def delinterface():
    iid=request.args.get("iid")
    rid=request.args.get("rid")
    #print("iid:",iid)
    #print("rid:",rid)
    if iid != None:
        interface_sql.del_interfaceinfo(iid)
        return "<html><p>删除完成</p><a href='interfaceList'>返回待请求接口列表</a></html>"
    else:
        #执行单个用例
        data = interface_sql.sel_id_interfaceinfo(rid)
        parameter = data[5]
        url = data[2]
        method = data[6]
        res_data=req_single(url,parameter,method)#响应数据、响应码、响应时间
        print(res_data)
        payOrderNo=json.loads(res_data[0].replace('\n','').replace('\t','').replace('\\',''))["data"]["payOrderNo"]
        print("payOrderNo:",payOrderNo)#转化为字典格式并获取订单号
        order_status=get_status.get_order_status(payOrderNo)#处理订单payOrderNo+1用于在paygw中查询订单状态
        expected=data[9]
        print("expected:",expected)
        print("order_status:",order_status)
        if order_status==expected:
            result='SUCCESS'
        else:
            result='FAIL'
        print("result:",result)
        interface_sql.insert_interfacerespond(data[1],data[2],data[5],res_data[0],res_data[1],res_data[2],data[8],result)
        return "<html><p>执行成功</p><a href='interfaceRespondList'>返回请求结果接口列表</a></html>"

@app.route("/interfaceRespondList",methods=["GET","POST"])
def interfaceRespondList():
    data=interface_sql.sel_interfacerespond()
    return render_template("interfacerespondlist.html",result=(data,))

@app.route("/mytest",methods=["GET","POST"])
def edit_page():
    #编辑弹窗数据展示
    if request.method=="POST":
        data=json.loads(request.get_data())
        #print(type(data),data)
        editId=data["editId"]
        editId_data=interface_sql.sel_id_interfaceinfo(editId)
        print(editId_data)
        return json.dumps({"msg":"ok","code":200,"data":editId_data})

@app.route("/updateInterface",methods=["GET","POST"])
def updateInterface():
    '''编辑修改请求接口'''
    if request.method=='POST':
        try:
            id=request.form["iid"]
            intername=request.form["imode"]
            #print(intername)
            descp=request.form["idesc"]
            interaddr=request.form["iaddr"]
            header=request.form["iheader"]
            param = request.form["iparam"]
            option = request.form["ioption"]
            author = request.form["iauthor"]
            expected = request.form["iresult"]
            account = request.form["iuserpwd"]
            interface_sql.update_interfaceinfo(id,intername,descp,interaddr,header,param,option,author,expected,account)

        except:
            print("修改失败")
    return interface()

@app.route("/addInterface",methods=["GET","POST"])
def addInterface():
    '''新增接口请求'''
    if request.method=='POST':
        try:
            intername = request.form["imode"]
            print(intername)
            descp = request.form["idesc"]
            interaddr = request.form["iaddr"]
            header = request.form["iheader"]
            param = request.form["iparam"]
            option = request.form["ioption"]
            author = request.form["iauthor"]
            expected = request.form["iresult"]
            account = request.form["iuserpwd"]
            print(account)
            interface_sql.insert_interfaceinfo(intername, interaddr, header, param, option, author, descp, expected,
                                              account)
            return "<html><p>添加成功</p><a href='interfaceList'>返回请求接口列表</a></html>"
        except:
            return "<html><p>添加失败</p><a href='interfaceList'>返回请求接口列表</a></html>"

    return interface()

@app.route("/runtest",methods=["GET","POST"])
def runtest():
    req_allrun.req_allrun()
    return "<html><p>全部执行完成</p><a href='interfaceRespondList'>返回请求结果接口列表</a></html>"



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port="8888")

