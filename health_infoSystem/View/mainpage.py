# -*- coding: utf-8 -*-
import sys
import os
import webbrowser
import tkinter
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from View.view import *  # 菜单栏对应的各个子页面
import View.login as login


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("1600x600")
        self.root.title('医疗健康档案系统 ' + '欢迎您')
        self.createPage()

    def createPage(self):
        self.AddPatient = AddPatientFrame(self.root)  # 创建不同Frame
        self.Search = SearchFrame(self.root)
        # self.Editinfo = EditFrame(self.root)
        # self.Delete = DeleteFrame(self.root)
        self.Search.grid()  # 默认显示查询界面
        menubar = Menu(self.root)
        menubar.add_command(label='查询档案', command=self.search, font='SimSun -14')
        menubar.add_command(label='添加档案', command=self.add, font='SimSun -14')
        # menubar.add_command(label='更新', command=self.edit, font='SimSun -14')
        # menubar.add_command(label='删除', command=self.delete, font='SimSun -14')
        menubar.add_command(label='档案可视化', command=self.open, font='SimSun -14')
        menubar.add_command(label='切换账户', command=self.change, font='SimSun -14')
        self.root['menu'] = menubar  # 设置菜单栏

    def add(self):
        self.AddPatient.grid()
        self.Search.grid_forget()

    def search(self):
        self.AddPatient.grid_forget()
        self.Search.grid()

    def open(self):
        self.webbrowser=webbrowser
        webbrowser.open('E:\pyfile\外包专用\health_infoSystem\static\index.html')
    def change(self):
        if askokcancel('提示', '确定要切换账户？'):
            self.root.destroy()
            root = tkinter.Tk()
            root.title("医疗健康档案系统")
            login.LoginPage(root)
            root.mainloop()
