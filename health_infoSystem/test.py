# -*- coding: utf-8 -*-
# @Time : 2023/3/5 11:47
# @Author : niki
import tkinter.messagebox
import ttkbootstrap as ttk
from View.login import LoginPage

root = tkinter.Tk()
style = ttk.Style("cosmo")
root.title("医疗健康档案系统")
LoginPage(root)
root.mainloop()


