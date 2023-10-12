# -*- coding: utf-8 -*-
import webbrowser
from tkinter import *
from tkinter.messagebox import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from model.ConnDB import *
from View.dataEntryForm import DataEntryForm

class AddPatientFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.id = IntVar()
        self.name = StringVar()
        self.nation = StringVar()
        self.sex = StringVar()
        self.age = StringVar()
        self.tel = StringVar()
        self.address = StringVar()
        self.marriage = StringVar()
        self.drug_allergy = StringVar()
        self.medical_history = StringVar()
        self.operation_history = StringVar()
        self.smoke_history = StringVar()
        self.dt = StringVar()
        self.l_blp = StringVar()
        self.h_blp = StringVar()
        self.bos = StringVar()
        self.hr = StringVar()
        self.pulse = StringVar()
        self.tp = StringVar()
        self.height = StringVar()
        self.weight = StringVar()
        self.createPage()

    def createPage(self):
        ### 基本信息类
        ttk.Label(self, text='基本信息项', font='SimSum -16 bold').grid(row=0, column=0, pady=10, sticky=W)
        ttk.Label(self, text='编   号:', font='SimSun -14').grid(row=1, column=0, pady=10)
        ttk.Label(self, text='姓   名:', font='SimSun -14').grid(row=2, column=0, pady=10)
        ttk.Label(self, text='民   族:', font='SimSun -14').grid(row=3, column=0, pady=10)
        ttk.Label(self, text='性   别:', font='SimSun -14').grid(row=4, column=0, pady=10)
        ttk.Label(self, text='年   龄:', font='SimSun -14').grid(row=5, column=0, pady=10)
        ttk.Label(self, text='联系方式:', font='SimSun -14').grid(row=6, column=0, pady=10)

        ttk.Label(self, text='籍   贯:', font='SimSun -14').grid(row=1, column=3, pady=10)
        ttk.Label(self, text='婚姻情况:', font='SimSun -14').grid(row=2, column=3, pady=10)
        ttk.Label(self, text='药物过敏:', font='SimSun -14').grid(row=3, column=3, pady=10)
        ttk.Label(self, text='既往病史:', font='SimSun -14').grid(row=4, column=3, pady=10)
        ttk.Label(self, text='手术史:', font='SimSun -14').grid(row=5, column=3, pady=10)
        ttk.Label(self, text='吸烟况:', font='SimSun -14').grid(row=6, column=3, pady=10)

        ttk.Entry(self, textvariable=self.id).grid(row=1, column=1, columnspan=2, sticky=W + E, pady=5)
        ttk.Entry(self, textvariable=self.name).grid(row=2, column=1, columnspan=2, sticky=W + E, pady=5)
        ttk.Entry(self, textvariable=self.nation).grid(row=3, column=1, columnspan=2, sticky=W + E, pady=5)
        ttk.Entry(self, textvariable=self.sex).grid(row=4, column=1, columnspan=2, sticky=W + E, pady=5)
        ttk.Entry(self, textvariable=self.age).grid(row=5, column=1, columnspan=2, sticky=W + E, pady=5)
        ttk.Entry(self, textvariable=self.tel).grid(row=6, column=1, columnspan=2, sticky=W + E, pady=5)

        ttk.Entry(self, textvariable=self.address).grid(row=1, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.marriage).grid(row=2, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.drug_allergy).grid(row=3, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.medical_history).grid(row=4, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.operation_history).grid(row=5, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.smoke_history).grid(row=6, column=4, pady=10, sticky=W + E)
        ### 生命体征类
        ttk.Label(self, text='生命体征项', font='SimSun -16  bold').grid(row=0, column=6, pady=10)
        ttk.Label(self, text='测量日期:', font='SimSun -14').grid(row=1, column=6, pady=10)
        ttk.Label(self, text='收 缩 压:', font='SimSun -14').grid(row=2, column=6, pady=10)
        ttk.Label(self, text='舒 张 压:', font='SimSun -14').grid(row=3, column=6, pady=10)
        ttk.Label(self, text='心    率:', font='SimSun -14').grid(row=4, column=6, pady=10)
        ttk.Label(self, text='血氧饱和度:', font='SimSun -14').grid(row=5, column=6, pady=10)

        ttk.Label(self, text='脉    搏:', font='SimSun -14').grid(row=1, column=8, pady=10)
        ttk.Label(self, text='体    温:', font='SimSun -14').grid(row=2, column=8, pady=10)
        ttk.Label(self, text='身    高:', font='SimSun -14').grid(row=3, column=8, pady=10)
        ttk.Label(self, text='体    重:', font='SimSun -14').grid(row=4, column=8, pady=10)

        ttk.Entry(self, textvariable=self.dt).grid(row=1, column=7, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.l_blp).grid(row=2, column=7, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.h_blp).grid(row=3, column=7, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.hr).grid(row=4, column=7, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.bos).grid(row=5, column=7, pady=10, sticky=W + E)

        ttk.Entry(self, textvariable=self.pulse).grid(row=1, column=9, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.tp).grid(row=2, column=9, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.height).grid(row=3, column=9, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.weight).grid(row=4, column=9, pady=10, sticky=W + E)



        ttk.Button(self, text='提交', command=self.datacommit, width=10, bootstyle="Primary").grid(row=10, column=1,
                                                                                                      pady=10)
        ttk.Button(self, text='清除', command=self.clear, width=10, bootstyle="Danger").grid(row=10, column=4,
                                                                                                pady=10)

    def datacommit(self):
        global id, name, nation, sex, age, tel, address, marriage, drug_allergy, medical_history, operation_history, smoke_history, l_blp, h_blp, bos, hr, pulse, dt, tp, height, weight
        ms = ConnDB()
        if self.id.get():
            id = self.id.get()
        else:
            showinfo(title='提示', message='编号不能为空！')
        if self.name.get():
            name = self.name.get()
        else:
            showinfo(title='提示', message='姓名不能为空！')
        if self.nation.get():
            nation = self.nation.get()
        else:
            showinfo(title='提示', message='民族不能为空！')
        if self.sex.get():
            sex = self.sex.get()
        else:
            showinfo(title='提示', message='性别不能为空！')
        if self.age.get():
            age = self.age.get()
        else:
            showinfo(title='提示', message='年龄不能为空！')
        if self.tel.get():
            tel = self.tel.get()
        else:
            showinfo(title='提示', message='联系方式不能为空！')
        if self.address.get():
            address = self.address.get()
        else:
            showinfo(title='提示', message='籍贯不能为空！')
        if self.marriage.get():
            marriage = self.marriage.get()
        else:
            showinfo(title='提示', message='婚姻情况不能为空！')
        if self.drug_allergy.get():
            drug_allergy = self.drug_allergy.get()
        else:
            showinfo(title='提示', message='药物过敏不能为空！（没有填无）')
        if self.medical_history.get():
            medical_history = self.medical_history.get()
        else:
            showinfo(title='提示', message='既往病历不能为空！（没有填无）')
        if self.operation_history.get():
            operation_history = self.operation_history.get()
        else:
            showinfo(title='提示', message='手术史不能为空！（没有填无）')
        if self.smoke_history.get():
            smoke_history = self.smoke_history.get()
        else:
            showinfo(title='提示', message='吸烟史不能为空！（没有填无）')
        if self.dt.get():
            dt = self.dt.get()
        else:
            showinfo(title='提示', message='测量日期不能为空！')
        if self.l_blp.get():
            l_blp = self.l_blp.get()
        else:
            showinfo(title='提示', message='收缩压不能为空！')
        if self.h_blp.get():
            h_blp = self.h_blp.get()
        else:
            showinfo(title='提示', message='舒张压不能为空！')
        if self.bos.get():
            bos = self.bos.get()
        else:
            showinfo(title='提示', message='血氧饱和度不能为空！')
        if self.hr.get():
            hr = self.hr.get()
        else:
            showinfo(title='提示', message='心率不能为空！')
        if self.pulse.get():
            pulse = self.pulse.get()
        else:
            showinfo(title='提示', message='脉搏不能为空！')
        if self.tp.get():
            tp = self.tp.get()
        else:
            showinfo(title='提示', message='体温不能为空！')
        if self.height.get():
            height = self.height.get()
        else:
            showinfo(title='提示', message='身高不能为空！')
        if self.weight.get():
            weight = self.weight.get()
        else:
            showinfo(title='提示', message='体重不能为空！')
        # number = len(ms.ExecQuery("select id from basic_information"))
        # sql = "insert into basic_information values(N'{}',N'{}',N'{}',N'{}',{},{},N'{}',N'{}',N'{}',{},N'{}',N'{}')".format(
        sql = "insert into basic_information values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id,name, nation,sex, age,tel,
                                                                                                                          address, marriage,drug_allergy,
                                                                                                                          medical_history, operation_history,smoke_history)
        sql1 = "insert into vital_signs values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, dt, l_blp,
                                                                                                          h_blp, bos,
                                                                                                          hr, pulse, tp,
                                                                                                          height,weight)

        try:
            # print(sql)
            ms.ExecNonQuery(sql, ())
            ms.ExecNonQuery(sql1, ())
            showinfo(title='提示', message='添加成功！')
            self.clear()

        except Exception as e:
            showinfo(title='提示', message='出错了！请重试！')
            print(str(e))
        ms.close()

    def clear(self):
        self.id.set('')
        self.name.set('')
        self.nation.set('')
        self.sex.set('')
        self.age.set('')
        self.tel.set('')
        self.address.set('')
        self.marriage.set('')
        self.drug_allergy.set('')
        self.medical_history.set('')
        self.operation_history.set('')
        self.smoke_history.set('')
        self.dt.set('')
        self.l_blp.set('')
        self.h_blp.set('')
        self.bos.set('')
        self.hr.set('')
        self.pulse.set('')
        self.tp.set('')
        self.height.set('')
        self.weight.set('')

class SearchFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.id = IntVar()
        self.name = StringVar()
        self.nation=StringVar()
        self.way = StringVar()
        self.index =StringVar()
        self.tel = StringVar()
        self.age = StringVar()
        self.sex = StringVar()
        self.height = StringVar()
        self.weight = StringVar()
        self.address = StringVar()
        self.marriage = StringVar()
        self.drug_allergy = StringVar()
        self.medical_history = StringVar()
        self.operation_history = StringVar()
        self.smoke_history=StringVar()
        self.dt = StringVar()
        self.l_blp = StringVar()
        self.h_blp=StringVar()
        self.bos = StringVar()
        self.hr = StringVar()
        self.pulse = StringVar()
        self.tp=StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='查询档案', font='SimSum -16 bold').grid(row=0, column=0, pady=10)
        Button(self, text="显示全部档案", command=self.displayall, font='SimSun -14').grid(row=1, column=4, padx=5, pady=10,
                                                                                     sticky=W + E + N + S)
        Label(self, text='查询方式', font='SimSun -14').grid(row=1, column=0, padx=5, pady=10, sticky=W)
        combobox = ttk.Combobox(self, textvariable=self.way, font='SimSun -14')
        combobox.grid(row=1, column=1, padx=5, pady=10, sticky=W + E + N + S)
        # 设置下拉菜单中的值
        combobox['value'] = ("编号", "姓名")
        combobox['state'] = "readonly"  # 设定下拉框状态，readonly表示只读，不可更改内容
        combobox.current(0)
        Entry(self, text=self.index).grid(row=1, column=2, padx=5, pady=10, sticky=W + E + N + S)
        Button(self, text='查询', command=lambda: self.search(self.way.get(), self.index.get()), font='SimSun -14') \
            .grid(row=1, column=3, padx=5, pady=10, sticky=W + E + N + S)
        Label(self, text='上一次查询记录:', font='SimSun -14').grid(row=4, column=0, padx=5, pady=10, sticky=N)

    def displayall(self):
        ms = ConnDB(as_dict=False)
        sql = "select ID,name,nation,sex,age,tel,address,drug_allergy,medical_history,operation_history,smoke_history,h_blp,bos,hr,pulse,tp,height,weight " \
              "from basic_information left join vital_signs on basic_information.ID = vital_signs.v_ID "
        result = ms.ExecQuery(sql, ())
        ms.close()
        # 定义列
        columns = ("编号", "姓名","民族", "性别","年龄", "联系方式","籍贯", "药物过敏", "既往病史", "手术史","吸烟史", "收缩压","舒张压", "血氧", "心率", "脉搏","体温","身高", "体重" )
        tree = ttk.Treeview(self, show='headings', columns=columns)
        tree.grid(row=4, column=1, columnspan=1000, sticky=W + E + N + S)
        # 设置列，不显示
        tree.column("编号", width=80, anchor="center")
        tree.column("姓名", width=80, anchor="center")
        tree.column("民族", width=80, anchor="center")
        tree.column("性别", width=80, anchor="center")
        tree.column("年龄", width=100, anchor="center")
        tree.column("联系方式", width=100, anchor="center")
        tree.column("籍贯", width=80, anchor="center")
        tree.column("药物过敏", width=200, anchor="center")
        tree.column("既往病史", width=80, anchor="center")
        tree.column("手术史", width=80, anchor="center")
        tree.column("吸烟史", width=80, anchor="center")
        tree.column("收缩压", width=80, anchor="center")
        tree.column("舒张压", width=80, anchor="center")
        tree.column("血氧", width=80, anchor="center")
        tree.column("心率", width=80, anchor="center")
        tree.column("脉搏", width=80, anchor="center")
        tree.column("体温", width=80, anchor="center")
        tree.column("身高", width=80, anchor="center")
        tree.column("体重", width=80, anchor="center")


        # 显示表头
        tree.heading("编号", text="编号")
        tree.heading("姓名", text="姓名")
        tree.heading("民族", text="民族")
        tree.heading("性别", text="性别")
        tree.heading("年龄", text="年龄")
        tree.heading("联系方式", text="联系方式")
        tree.heading("籍贯", text="籍贯")
        tree.heading("药物过敏", text="药物过敏")
        tree.heading("既往病史", text="既往病史")
        tree.heading("手术史", text="手术史")
        tree.heading("吸烟史", text="吸烟史")
        tree.heading("收缩压", text="收缩压")
        tree.heading("舒张压", text="舒张压")
        tree.heading("血氧", text="血氧")
        tree.heading("心率", text="心率")
        tree.heading("脉搏", text="脉搏")
        tree.heading("体温", text="体温")
        tree.heading("身高", text="身高")
        tree.heading("体重", text="体重")


        # 添加数据
        i = 0
        for data in result:
            # for j in range(0, len(data)):
            #     if type(result[i][j]) == int:
            #         continue
            #     # print(chardet.detect(data[j]))
            #     data[j].encode('utf-8')
            tree.insert("", i, text=str(i), values=data)
            i += 1


    def search(self, way, index):
        ms = ConnDB(as_dict=False)
        if way == '编号':

            sql = "select ID,name,nation,sex,age,tel,address,drug_allergy,medical_history,operation_history,smoke_history,l_blp,h_blp,bos,hr,pulse,tp,height,weight " \
                  "from basic_information left join vital_signs on basic_information.ID = vital_signs.v_ID "\
                  "where ID=%s "
            if index.isdigit():
                result = ms.ExecQuery(sql, (index,))
                ms.close()
                if len(result):
                    # 定义列
                    columns = (
                    "编号", "姓名", "民族", "性别", "年龄", "联系方式", "籍贯", "药物过敏", "既往病史", "手术史", "吸烟史", "收缩压", "舒张压", "血氧", "心率",
                    "脉搏", "体温", "身高", "体重")
                    tree = ttk.Treeview(self, show='headings', columns=columns)
                    tree.grid(row=4, column=1, columnspan=1000, sticky=W + E + N + S)
                    # 设置列，不显示
                    tree.column("编号", width=80, anchor="center")
                    tree.column("姓名", width=80, anchor="center")
                    tree.column("民族", width=80, anchor="center")
                    tree.column("性别", width=80, anchor="center")
                    tree.column("年龄", width=100, anchor="center")
                    tree.column("联系方式", width=100, anchor="center")
                    tree.column("籍贯", width=80, anchor="center")
                    tree.column("药物过敏", width=200, anchor="center")
                    tree.column("既往病史", width=80, anchor="center")
                    tree.column("手术史", width=80, anchor="center")
                    tree.column("吸烟史", width=80, anchor="center")
                    tree.column("收缩压", width=80, anchor="center")
                    tree.column("舒张压", width=80, anchor="center")
                    tree.column("血氧", width=80, anchor="center")
                    tree.column("心率", width=80, anchor="center")
                    tree.column("脉搏", width=80, anchor="center")
                    tree.column("体温", width=80, anchor="center")
                    tree.column("身高", width=80, anchor="center")
                    tree.column("体重", width=80, anchor="center")

                    # 显示表头
                    tree.heading("编号", text="编号")
                    tree.heading("姓名", text="姓名")
                    tree.heading("民族", text="民族")
                    tree.heading("性别", text="性别")
                    tree.heading("年龄", text="年龄")
                    tree.heading("联系方式", text="联系方式")
                    tree.heading("籍贯", text="籍贯")
                    tree.heading("药物过敏", text="药物过敏")
                    tree.heading("既往病史", text="既往病史")
                    tree.heading("手术史", text="手术史")
                    tree.heading("吸烟史", text="吸烟史")
                    tree.heading("收缩压", text="收缩压")
                    tree.heading("舒张压", text="舒张压")
                    tree.heading("血氧", text="血氧")
                    tree.heading("心率", text="心率")
                    tree.heading("脉搏", text="脉搏")
                    tree.heading("体温", text="体温")
                    tree.heading("身高", text="身高")
                    tree.heading("体重", text="体重")
                    # 添加数据
                    for i in range(0, len(result)):
                        # for j in range(0, len(result[i])):
                        #     if type(result[i][j]) == int:
                        #         continue
                        #     # print(chardet.detect(result[i][j]))
                        #     result[i][j].encode('utf-8')
                        tree.insert("", i, text=str(i), values=result[i])

                else:
                    showinfo('提示', '该编号的病例不存在！')
            else:
                showinfo(title='提示', message='请输入正确编号！')
        elif way == '姓名':
            sql = "select ID,name,nation,sex,age,tel,address,drug_allergy,medical_history,operation_history,smoke_history,l_blp,h_blp,bos,hr,pulse,tp,height,weight " \
                  "from basic_information left join vital_signs on basic_information.ID = vital_signs.v_ID "\
                  "where name=N'%s' " % index
            result = ms.ExecQuery(sql, ())
            ms.close()
            if len(result):
                columns = (
                    "编号", "姓名", "民族", "性别", "年龄", "联系方式", "籍贯", "药物过敏", "既往病史", "手术史", "吸烟史", "收缩压", "舒张压", "血氧", "心率",
                    "脉搏", "体温", "身高", "体重")
                tree = ttk.Treeview(self, show='headings', columns=columns)
                tree.grid(row=4, column=1, columnspan=1000, sticky=W + E + N + S)
                # 设置列，不显示
                tree.column("编号", width=80, anchor="center")
                tree.column("姓名", width=80, anchor="center")
                tree.column("民族", width=80, anchor="center")
                tree.column("性别", width=80, anchor="center")
                tree.column("年龄", width=100, anchor="center")
                tree.column("联系方式", width=100, anchor="center")
                tree.column("籍贯", width=80, anchor="center")
                tree.column("药物过敏", width=200, anchor="center")
                tree.column("既往病史", width=80, anchor="center")
                tree.column("手术史", width=80, anchor="center")
                tree.column("吸烟史", width=80, anchor="center")
                tree.column("收缩压", width=80, anchor="center")
                tree.column("舒张压", width=80, anchor="center")
                tree.column("血氧", width=80, anchor="center")
                tree.column("心率", width=80, anchor="center")
                tree.column("脉搏", width=80, anchor="center")
                tree.column("体温", width=80, anchor="center")
                tree.column("身高", width=80, anchor="center")
                tree.column("体重", width=80, anchor="center")

                # 显示表头
                tree.heading("编号", text="编号")
                tree.heading("姓名", text="姓名")
                tree.heading("民族", text="民族")
                tree.heading("性别", text="性别")
                tree.heading("年龄", text="年龄")
                tree.heading("联系方式", text="联系方式")
                tree.heading("籍贯", text="籍贯")
                tree.heading("药物过敏", text="药物过敏")
                tree.heading("既往病史", text="既往病史")
                tree.heading("手术史", text="手术史")
                tree.heading("吸烟史", text="吸烟史")
                tree.heading("收缩压", text="收缩压")
                tree.heading("舒张压", text="舒张压")
                tree.heading("血氧", text="血氧")
                tree.heading("心率", text="心率")
                tree.heading("脉搏", text="脉搏")
                tree.heading("体温", text="体温")
                tree.heading("身高", text="身高")
                tree.heading("体重", text="体重")
                # 添加数据
                for i in range(0, len(result)):
                    # for j in range(0, len(result[i])):
                    #     if type(result[i][j]) == int:
                    #         continue
                    #     # print(chardet.detect(result[i][j]))
                    #     result[i][j].encode('utf-8')
                    tree.insert("", i, text=str(i), values=result[i])
            else:
                showinfo('提示', '该姓名的病例不存在！')




#
# # # class EditFrame(Frame):  # 继承Frame类
# #     def __init__(self, master=None):
# #         Frame.__init__(self, master)
# #         self.root = master  # 定义内部变量root
# #         self.number = StringVar()
# #         self.userName = StringVar()
# #         self.sex = StringVar()
# #         self.age = StringVar()
# #         self.birth = StringVar()
# #         self.tel = StringVar()
# #         self.email = StringVar()
# #         self.address = StringVar()
# #         self.major = StringVar()
# #         self.r = IntVar()
# #         self.index = StringVar()
# #         self.way = StringVar()
# #         self.oldusername = StringVar()
# #         self.oldsex = StringVar()
# #         self.oldage = StringVar()
# #         self.oldbirth = StringVar()
# #         self.oldtel = StringVar()
# #         self.oldemail = StringVar()
# #         self.oldaddress = StringVar()
# #         self.oldmajor = StringVar()
# #         self.createPage()
# #
# #     def createPage(self):
# #         Label(self, text='更新病例信息', font='SimSun -16 bold').grid(row=0, column=0, pady=10)
# #         Label(self, text='编号').grid(row=1, column=0, padx=5, pady=10)
# #         Entry(self, textvariable=self.number).grid(row=1, column=1, padx=5, pady=10)
# #         Button(self, text='查询', command=lambda: self.search(self.number.get()), font='SimSun -14', width=10).grid(row=1,
# #                                                                                                                   column=2,
# #                                                                                                                   padx=5,
# #                                                                                                                   pady=10)
# #         Label(self, text='姓   名:', font='SimSun -14').grid(row=2, column=0, pady=10)
# #         Label(self, text='性   别:', font='SimSun -14').grid(row=3, column=0, pady=10)
# #         Label(self, text='年   龄:', font='SimSun -14').grid(row=4, column=0, pady=10)
# #         Label(self, text='出生日期:', font='SimSun -14').grid(row=5, column=0, pady=10)
# #         Label(self, text='联系方式:', font='SimSun -14').grid(row=2, column=2, pady=10)
# #         Label(self, text='邮   箱:', font='SimSun -14').grid(row=3, column=2, pady=10)
# #         Label(self, text='地   址:', font='SimSun -14').grid(row=4, column=2, pady=10)
# #         Label(self, text='专   业:', font='SimSun -14').grid(row=5, column=2, pady=10)
# #         Entry(self, textvariable=self.userName).grid(row=2, column=1, pady=10)
# #         Entry(self, textvariable=self.sex).grid(row=3, column=1, pady=10)
# #         Entry(self, textvariable=self.age).grid(row=4, column=1, pady=10)
# #         Entry(self, textvariable=self.birth).grid(row=5, column=1, pady=10)
# #         Entry(self, textvariable=self.tel).grid(row=2, column=3, pady=10)
# #         Entry(self, textvariable=self.email).grid(row=3, column=3, pady=10)
# #         Entry(self, textvariable=self.address).grid(row=4, column=3, pady=10)
# #         Entry(self, textvariable=self.major).grid(row=5, column=3, pady=10)
# #         Button(self, text='更新', command=lambda: self.updateinfo(self.number.get()), font='SimSun -14', width=10).grid(
# #             row=6, column=1, pady=10)
# #         Button(self, text='撤销', command=lambda: self.repeal(self.number.get()), font='SimSun -14', width=10).grid(row=6,
# #                                                                                                                   column=2,
# #                                                                                                                   pady=10)
# #
# #     def search(self, number):
# #         if number:
# #             db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema',
# #                                  charset='utf8')
# #             cur = db.cursor()
# #             numberexists = 0
# #             sql = "select number from {}"
# #             sql = sql.format(self.tablename)
# #             cur.execute(sql)
# #             numberdata = cur.fetchall()
# #             for i in range(0, len(numberdata)):
# #                 if numberdata[i][0] == number:
# #                     numberexists = 1
# #                     break
# #                 else:
# #                     i += 1
# #             if numberexists:
# #                 sql = "select * from {} where number = '{}'"
# #                 sql = sql.format(self.tablename, number)
# #                 cur.execute(sql)
# #                 contactsdata = cur.fetchall()
# #                 db.close()
# #                 self.oldusername = contactsdata[0][1]
# #                 self.oldsex = contactsdata[0][2]
# #                 self.oldage = contactsdata[0][3]
# #                 self.oldbirth = contactsdata[0][4]
# #                 self.oldtel = contactsdata[0][5]
# #                 self.oldemail = contactsdata[0][6]
# #                 self.oldaddress = contactsdata[0][7]
# #                 self.oldmajor = contactsdata[0][8]
# #
# #                 self.userName.set(contactsdata[0][1])
# #                 self.sex.set(contactsdata[0][2])
# #                 self.age.set(contactsdata[0][3])
# #                 self.birth.set(contactsdata[0][4])
# #                 self.tel.set(contactsdata[0][5])
# #                 self.email.set(contactsdata[0][6])
# #                 self.address.set(contactsdata[0][7])
# #                 self.major.set(contactsdata[0][8])
# #             else:
# #                 showinfo('提示', '该学号的学生不存在！')
# #                 self.number.set('')
# #         else:
# #             showinfo('提示', '学号不能为空！')
# #
# #     def updateinfo(self, number):
# #         newusername = self.userName.get()
# #         newsex = self.sex.get()
# #         newage = self.age.get()
# #         newbirth = self.birth.get()
# #         newtel = self.tel.get()
# #         newemail = self.email.get()
# #         newaddress = self.address.get()
# #         newmajor = self.major.get()
# #         # 提交到数据库
# #         db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema', charset='utf8')
# #         cur = db.cursor()
# #         sql = "update {} set userName = '{}',sex = '{}'," \
# #               "age = '{}',birth = '{}',tel='{}',email = '{}',address = '{}',major = '{}' where number = '{}'"
# #         sql = sql.format(self.tablename, newusername, newsex, newage, newbirth, newtel, newemail, newaddress, newmajor,
# #                          number)
# #         try:
# #             cur.execute(sql)
# #             db.commit()
# #             db.close()
# #             showinfo('提示', '数据更新成功!')
# #         except:
# #             showinfo('提示', '数据更新失败！')
# #
# #     def repeal(self, number):
# #         db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema', charset='utf8')
# #         cur = db.cursor()
# #         sql = "update {} set userName = '{}',sex = '{}'," \
# #               "age = '{}',birth = '{}',tel='{}',email = '{}',address = '{}',major = '{}' where number = '{}'"
# #         sql = sql.format(self.tablename, self.oldusername, self.oldsex, self.oldage, self.oldbirth,
# #                          self.oldtel, self.oldemail, self.oldaddress, self.oldmajor, number)
# #         try:
# #             cur.execute(sql)
# #             db.commit()
# #             db.close()
# #             showinfo('提示', '撤销成功!')
# #         except:
# #             showinfo('提示', '撤销失败！')
# #
# #
# # class DeleteFrame(Frame):  # 继承Frame类
# #     def __init__(self, master=None):
# #         Frame.__init__(self, master)
# #         self.root = master  # 定义内部变量root
# #         self.number = StringVar()
# #         self.userName = StringVar()
# #         self.sex = StringVar()
# #         self.age = StringVar()
# #         self.birth = StringVar()
# #         self.tel = StringVar()
# #         self.email = StringVar()
# #         self.address = StringVar()
# #         self.major = StringVar()
# #         self.r = IntVar()
# #         self.index = StringVar()
# #         self.way = StringVar()
# #         f = open('user.txt', 'r', encoding='utf-8')
# #         self.tablename = f.read()
# #         f.close()
# #         self.oldusername = StringVar()
# #         self.oldsex = StringVar()
# #         self.oldage = StringVar()
# #         self.oldbirth = StringVar()
# #         self.oldtel = StringVar()
# #         self.oldemail = StringVar()
# #         self.oldaddress = StringVar()
# #         self.oldmajor = StringVar()
# #         self.createPage()
# #
# #     def createPage(self):
# #         Label(self, text='删除学生信息', font='SimSun -16 bold').grid(row=0, column=0, pady=10)
# #         Label(self, text='学号').grid(row=1, column=0, padx=5, pady=10)
# #         Entry(self, textvariable=self.number).grid(row=1, column=1, padx=5, pady=10)
# #         Button(self, text='查询', command=lambda: self.search(self.number.get()), font='SimSun -14', width=10).grid(row=1,
# #                                                                                                                   column=2,
# #                                                                                                                   padx=5,
# #                                                                                                                   pady=10)
# #         Label(self, text='姓   名:', font='SimSun -14').grid(row=2, column=0, pady=10)
# #         Label(self, text='性   别:', font='SimSun -14').grid(row=3, column=0, pady=10)
# #         Label(self, text='年   龄:', font='SimSun -14').grid(row=4, column=0, pady=10)
# #         Label(self, text='出生日期:', font='SimSun -14').grid(row=5, column=0, pady=10)
# #         Label(self, text='联系方式:', font='SimSun -14').grid(row=2, column=2, pady=10)
# #         Label(self, text='邮   箱:', font='SimSun -14').grid(row=3, column=2, pady=10)
# #         Label(self, text='地   址:', font='SimSun -14').grid(row=4, column=2, pady=10)
# #         Label(self, text='专   业:', font='SimSun -14').grid(row=5, column=2, pady=10)
# #         Entry(self, textvariable=self.userName).grid(row=2, column=1, pady=10)
# #         Entry(self, textvariable=self.sex).grid(row=3, column=1, pady=10)
# #         Entry(self, textvariable=self.age).grid(row=4, column=1, pady=10)
# #         Entry(self, textvariable=self.birth).grid(row=5, column=1, pady=10)
# #         Entry(self, textvariable=self.tel).grid(row=2, column=3, pady=10)
# #         Entry(self, textvariable=self.email).grid(row=3, column=3, pady=10)
# #         Entry(self, textvariable=self.address).grid(row=4, column=3, pady=10)
# #         Entry(self, textvariable=self.major).grid(row=5, column=3, pady=10)
# #         Button(self, text='删除', command=lambda: self.delete(self.number.get()), font='SimSun -14', width=10).grid(row=6,
# #                                                                                                                   column=1,
# #                                                                                                                   pady=10)
# #         Button(self, text='撤销', command=lambda: self.repeal(self.number.get()), font='SimSun -14', width=10).grid(row=6,
# #                                                                                                                   column=2,
# #                                                                                                                   pady=10)
# #
# #     def search(self, number):
# #         if number:
# #             db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema',
# #                                  charset='utf8')
# #             cur = db.cursor()
# #             numberexists = 0
# #             sql = "select number from {}"
# #             sql = sql.format(self.tablename)
# #             cur.execute(sql)
# #             numberdata = cur.fetchall()
# #             for i in range(0, len(numberdata)):
# #                 if numberdata[i][0] == number:
# #                     numberexists = 1
# #                     break
# #                 else:
# #                     i += 1
# #             if numberexists:
# #                 sql = "select * from {} where number = '{}'"
# #                 sql = sql.format(self.tablename, number)
# #                 cur.execute(sql)
# #                 contactsdata = cur.fetchall()
# #                 db.close()
# #                 self.oldusername = contactsdata[0][1]
# #                 self.oldsex = contactsdata[0][2]
# #                 self.oldage = contactsdata[0][3]
# #                 self.oldbirth = contactsdata[0][4]
# #                 self.oldtel = contactsdata[0][5]
# #                 self.oldemail = contactsdata[0][6]
# #                 self.oldaddress = contactsdata[0][7]
# #                 self.oldmajor = contactsdata[0][8]
# #
# #                 self.userName.set(contactsdata[0][1])
# #                 self.sex.set(contactsdata[0][2])
# #                 self.age.set(contactsdata[0][3])
# #                 self.birth.set(contactsdata[0][4])
# #                 self.tel.set(contactsdata[0][5])
# #                 self.email.set(contactsdata[0][6])
# #                 self.address.set(contactsdata[0][7])
# #                 self.major.set(contactsdata[0][8])
# #             else:
# #                 showinfo('提示', '该学号的学生不存在！')
# #                 self.number.set('')
# #         else:
# #             showinfo('提示', '学号不能为空！')
# #
# #     def delete(self, number):
# #         db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema', charset='utf8')
# #         cur = db.cursor()
# #         sql = "delete from {} where number = '{}'"
# #         sql = sql.format(self.tablename, number)
# #         try:
# #             cur.execute(sql)
# #             db.commit()
# #             db.close()
# #             showinfo('提示', '删除成功！')
# #             self.number.set('')
# #             self.userName.set('')
# #             self.sex.set('')
# #             self.age.set('')
# #             self.birth.set('')
# #             self.tel.set('')
# #             self.email.set('')
# #             self.address.set('')
# #             self.major.set('')
# #         except:
# #             showinfo('提示', '删除失败！')
# #
# #     def repeal(self, number):
# #         db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema', charset='utf8')
# #         cur = db.cursor()
# #         sql = "update {} set userName = '{}',sex = '{}'," \
# #               "age = '{}',birth = '{}',tel='{}',email = '{}',address = '{}',major = '{}' where number = '{}'"
# #         sql = sql.format(self.tablename, self.oldusername, self.oldsex, self.oldage, self.oldbirth,
# #                          self.oldtel, self.oldemail, self.oldaddress, self.oldmajor, number)
# #         try:
# #             cur.execute(sql)
# #             db.commit()
# #             db.close()
# #             showinfo('提示', '撤销成功!')
# #         except:
# #             showinfo('提示', '撤销失败！')
#
#
# # class CopyFrame(Frame):  # 继承Frame类
# #     def __init__(self, master=None):
# #         Frame.__init__(self, master)
# #         self.root = master  # 定义内部变量root
# #         f = open('user.txt', 'r', encoding='utf-8')
# #         self.tablename = f.read()
# #         f.close()
# #         self.createPage()
# #
# #     def createPage(self):
# #         Label(self, text='数据备份与恢复', font='SimSun -16 bold').grid(row=0, column=0, padx=5, pady=10, sticky=W)
# #         Button(self, text='备份数据', command=self.backups, font='SimSun -14').grid(
# #             row=1, column=0, padx=5, pady=10, sticky=W)
# #         Button(self, text='恢复数据', command=self.renew, font='SimSun -14').grid(
# #             row=1, column=1, padx=5, pady=10, sticky=W)
# #
# #     def backups(self):
# #         # 追加mysql的bin目录到环境变量
# #         # sys.path.append('C:\Users\HP\AppData\Bin')
# #         # 如果不存在backup文件，新建一个
# #         if not os.path.exists('backup'):
# #             os.mkdir('backup')
# #         # 切换到新建的文件夹中
# #         os.chdir('backup')
# #         # def tuplesql(command,server,user,passwd,db,table,filename):
# #         #   return (mysqlcomm,dbserver,dbuser,dbpasswd,dbname,dbtable,exportfile)
# #         # 定义一系列参数
# #         mysqlcomm = 'mysqldump'
# #         dbserver = 'locolhost'
# #         dbuser = 'root'
# #         dbpasswd = 'woyangni0109'
# #         dbname = 'new_schema'
# #         dbtable = str(self.tablename)
# #         exportfile = 'backups.sql'
# #         # 定义sql的格式
# #         sqlfromat = "%s -h%s -u%s -p%s %s %s >%s"
# #         # 生成相应的sql语句
# #         sql = (sqlfromat % (mysqlcomm, dbserver, dbuser, dbpasswd, dbname, dbtable, exportfile))
# #
# #         # 判断是否已经有相应的sql文件生成；如果有，就按时间重命名该文件
# #         if os.path.exists(r'backups.sql'):
# #             os.rename('backups.sql', 'backups' + str(time.time()) + '.sql')
# #         # 执行sql并获取语句，os.system和subprocess.Popen执行该sql无效果，不知道是怎么回事，后续会继续关注
# #         result = os.popen(sql)
# #         # 对sql执行进行判断
# #         if result:
# #             showinfo(title='提示', message='数据备份成功！')
# #         else:
# #             showinfo(title='提示', message='数据备份失败！')
# #
# #     def renew(self):
# #         # 简单的恢复关键代码其实就下面这一行mysqldump换为mysql 用户名 密码 你要恢复到的数据库名 < sql文件
# #         try:
# #             os.system("mysql -uroot -pwoyangni0109 new_schema < /backup/backups.sql")
# #             showinfo(title='提示', message='数据恢复成功！')
# #         except Exception as e:
# #             showinfo(title='提示', message='数据恢复失败！\n' + str(e))
