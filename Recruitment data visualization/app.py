# -*- coding: utf-8 -*-
# @Time : 2023/5/19 18:12
# @Author : niki
import json

from flask import Flask, jsonify, request, render_template
import utils

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salary')
def salary():

    s1 = utils.get_salary1_data()
    s2 = utils.get_salary2_data()
    s3 = utils.get_salary3_data()
    return render_template('salary.html',data1 = s1 ,data2 = s2)

@app.route('/region')
def region():
    d1 = utils.get_region1_data()
    d2 = utils.get_region2_data()
    return render_template('region.html',data1 = d1,data2 = d2)

@app.route('/exp_edu')
def exp_edu():
    e1 = utils.get_edu1_data()
    e2 = utils.get_edu2_data()
    return render_template('exp_edu.html',data1 = e1,data2 = e2)

@app.route('/company')
def company():
    c1 = utils.get_company1_data()
    c2 = utils.get_company2_data()
    c3 = utils.get_company3_data()
    c4 = utils.get_company4_data()
    return render_template('company.html',data1 = c1,data2 = c2,data3 = c3,data4 = c4)

if __name__ == '__main__':
    app.run()
