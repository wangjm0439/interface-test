from flask import Flask,render_template,send_from_directory,url_for,sessions,escape,request
from flask import  make_response,abort,redirect,Response
from config.basis_config import *
from util.oper_interfacedb import Oper_sql
import os
from werkzeug.utils import secure_filename
from util.read_Excel import *
from run.req_interface.req_single import *

app = Flask(__name__)

upload_file = r"D:\work_space\python_space\interface-test\interface-test\run\uploads"#保存文件路径
#upload_file =os.path.join(os.path.abspath(os.path.dirname('.')),"run","upload")
app.config['UPLOAD_FOLDER'] = upload_file
allow_file = {'xlsx','xls'} #允许上传的文件类型
interface_sql=Oper_sql()


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
def delinterface():
    iid=request.args.get("iid")
    rid=request.args.get("rid")
    print("iid:",iid)
    print("rid:" ,rid)
    if iid !=None:
        interface_sql.del_interfaceinfo(iid)
    else:
        data=interface_sql.sel_id_interfaceifo(rid)
        parameter=data[5]
        url=data[2]
        method=data[6]
        res=req_single(url,parameter,method)
        print(res)
    return interface()







if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port="8888")

