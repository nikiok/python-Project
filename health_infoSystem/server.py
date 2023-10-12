# -*- coding: utf-8 -*-
# @Time : 2023/3/7 17:17
# @Author : niki

import webbrowser
from flask import Flask, render_template
import pymysql

app = Flask(__name__,template_folder='E:\pyfile\外包专用/health_infoSystem/templates',static_folder="E:\pyfile\外包专用\health_infoSystem/static")
@app.route("/")
@app.route('/index')
def my_echart():
      conn = pymysql.connect(host="localhost", user='root', password='123456', db='healthinfosys')#建立数据库连接
      cur = conn.cursor()
      sql = "select ID,name,nation,sex,age,tel,address,drug_allergy,medical_history,operation_history,smoke_history,h_blp,bos,hr,pulse,tp,height,weight " \
      "from basic_information left join vital_signs on basic_information.ID = vital_signs.v_ID "
      cur.execute(sql)#执行单条sql语句
      result = cur.fetchall()#接收全部的返回结果行
      data=list(result)
      basic_info=data[0]
      vitual_info=data[1]
      cur.close()#关闭指针对象
      conn.close()#关闭连接对象
      return render_template('index.html')#先引入bar.html，同时根据后面传入的参数，对html进行修改渲染
if __name__ == '__main__':
    app.run(debug=True)#启用调试模式
