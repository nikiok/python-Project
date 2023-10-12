# -*- coding: utf-8 -*-
# @Time : 2023/3/5 21:43
# @Author : niki
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *

tk = Tk()
var=IntVar()
#标签控件，显示文本和位图，展示在第一行
Label(tk,text="First").grid(row=0,column=0,sticky=E)#靠右
Label(tk,text="Second").grid(row=1,column=0,sticky=E)#第二行，靠左

#输入控件
Entry(tk).grid(row=0,column=1)
Entry(tk).grid(row=1,column=1)

button=Checkbutton(tk,text="Precerve aspect",variable=var)
button.grid(sticky=W)

#主事件循环
mainloop()