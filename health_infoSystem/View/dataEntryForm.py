from tkinter import *
from tkinter.messagebox import showinfo, askyesno
from model.ConnDB import  ConnDB
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class DataEntryForm(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, padding=(20, 10))
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.id = IntVar()
        self.name = StringVar()
        self.nation=StringVar()
        self.sex = StringVar()
        self.age = StringVar()
        self.tel = StringVar()
        self.address = StringVar()
        self.marriage = StringVar()
        self.drug_allergy = StringVar()
        self.medical_history = StringVar()
        self.operation_history = StringVar()
        self.smoke_history =StringVar()
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
        ttk.Label(self.root, text='基本信息项', font='SimSum -16 bold').grid(row=0, column=0, pady=10,sticky=W)

        ttk.Label(self.root, text='编   号:', font='SimSun -14').grid(row=1, column=0, pady=10)
        ttk.Entry(self.root, textvariable=self.id).grid(row=1, column=1,columnspan=2,sticky=W+E,pady=5)

        ttk.Label(self.root, text='姓   名:', font='SimSun -14').grid(row=2, column=0, pady=10)
        ttk.Entry(self.root, textvariable=self.name).grid(row=2, column=1,columnspan=2,sticky=W+E,pady=5)

        ttk.Label(self.root, text='民   族:', font='SimSun -14').grid(row=3, column=0, pady=10)
        ttk.Entry(self.root, textvariable=self.nation).grid(row=3, column=1,columnspan=2,sticky=W+E,pady=5)

        ttk.Label(self.root, text='性   别:', font='SimSun -14').grid(row=4, column=0, pady=10)
        ttk.Entry(self.root, textvariable=self.sex).grid(row=4, column=1,columnspan=2,sticky=W+E,pady=5)

        ttk.Label(self.root, text='年   龄:', font='SimSun -14').grid(row=5, column=0, pady=10)
        ttk.Entry(self.root, textvariable=self.age).grid(row=5, column=1,columnspan=2,sticky=W+E,pady=5)

        ttk.Label(self.root, text='联系方式:', font='SimSun -14').grid(row=6, column=0, pady=10)
        ttk.Entry(self.root, textvariable=self.tel).grid(row=6, column=1,columnspan=2,sticky=W+E,pady=5)

        ttk.Label(self.root, text='籍   贯:', font='SimSun -14').grid(row=1, column=3, pady=10)
        ttk.Entry(self.root, textvariable=self.address).grid(row=1, column=4, pady=10, sticky=W + E)

        ttk.Label(self.root, text='婚姻情况:', font='SimSun -14').grid(row=2, column=3, pady=10)
        ttk.Entry(self.root, textvariable=self.marriage).grid(row=2, column=4, pady=10, sticky=W + E)

        ttk.Label(self.root, text='药物过敏:', font='SimSun -14').grid(row=3, column=3, pady=10)
        ttk.Entry(self.root, textvariable=self.drug_allergy).grid(row=3, column=4, pady=10, sticky=W + E)

        ttk.Label(self.root, text='既往病史:', font='SimSun -14').grid(row=4, column=3, pady=10)
        ttk.Entry(self.root, textvariable=self.medical_history).grid(row=4, column=4, pady=10, sticky=W + E)

        ttk.Label(self.root, text='手术史:', font='SimSun -14').grid(row=5, column=3, pady=10)
        ttk.Entry(self.root, textvariable=self.operation_history).grid(row=5, column=4, pady=10, sticky=W + E)

        ttk.Label(self.root, text='吸烟况:', font='SimSun -14').grid(row=6, column=3, pady=10)
        ttk.Entry(self.root, textvariable=self.smoke_history).grid(row=6, column=4, pady=10, sticky=W + E)


### 生命体征类
        ttk.Label(self.root, text='生命体征项', font='SimSun -16  bold').grid(row=0, column=6, pady=10)

        ttk.Label(self.root, text='测量日期:', font='SimSun -14').grid(row=1, column=6, pady=10)
        ttk.Entry(self.root, textvariable=self.dt).grid(row=1, column=7, pady=10, sticky=W + E)

        ttk.Label(self.root, text='收 缩 压:', font='SimSun -14').grid(row=2, column=6, pady=10)
        ttk.Entry(self.root, textvariable=self.l_blp).grid(row=2, column=7, pady=10, sticky=W + E)

        ttk.Label(self.root, text='舒 张 压:', font='SimSun -14').grid(row=3, column=6, pady=10)
        ttk.Entry(self.root, textvariable=self.h_blp).grid(row=3, column=7, pady=10, sticky=W + E)

        ttk.Label(self.root, text='心    率:', font='SimSun -14').grid(row=4, column=6, pady=10)
        ttk.Entry(self.root, textvariable=self.hr).grid(row=4, column=7, pady=10, sticky=W + E)

        ttk.Label(self.root, text='血氧饱和度:', font='SimSun -14').grid(row=5, column=6, pady=10)
        ttk.Entry(self.root, textvariable=self.bos).grid(row=5, column=7, pady=10, sticky=W + E)

        ttk.Label(self.root, text='脉    搏:', font='SimSun -14').grid(row=1, column=8, pady=10)
        ttk.Entry(self.root, textvariable=self.pulse).grid(row=1, column=9, pady=10, sticky=W + E)

        ttk.Label(self.root, text='体    温:', font='SimSun -14').grid(row=2, column=8, pady=10)
        ttk.Entry(self.root, textvariable=self.tp).grid(row=2, column=9, pady=10, sticky=W + E)

        ttk.Label(self.root, text='身    高:', font='SimSun -14').grid(row=3, column=8, pady=10)
        ttk.Entry(self.root, textvariable=self.height).grid(row=3, column=9, pady=10, sticky=W + E)

        ttk.Label(self.root, text='体    重:', font='SimSun -14').grid(row=4, column=8, pady=10)
        ttk.Entry(self.root, textvariable=self.weight).grid(row=4, column=9, pady=10, sticky=W + E)


        ttk.Button(self.root, text='提交', command=self.datacommit, width=10, bootstyle="Primary").grid(row=10, column=1,
                                                                                                 pady=10)
        ttk.Button(self.root, text='清除', command=self.clear, width=10, bootstyle="Danger").grid(row=10, column=4, pady=10)

    def datacommit(self):
        global id,name, nation,  sex,age, tel,address, marriage,drug_allergy, medical_history, operation_history,smoke_history,l_blp,h_blp,bos,hr,pulse,dt,tp, height, weight
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
            tel = self.nation.get()
        else:
            showinfo(title='提示', message='民族不能为空！')
        if self.sex.get():
            tel = self.sex.get()
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
            showinfo(title='提示', message='药物过敏史不能为空！（没有填无）')
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
            dt= self.dt.get()
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
            bos= self.bos.get()
        else:
            showinfo(title='提示', message='血氧饱和度不能为空！')
        if self.hr.get():
            hr= self.hr.get()
        else:
            showinfo(title='提示', message='心率不能为空！')
        if self.pulse.get():
            pulse= self.pulse.get()
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
            weight= self.weight.get()
        else:
            showinfo(title='提示', message='体重不能为空！')
        # number = len(ms.ExecQuery("select id from basic_information"))
        # sql = "insert into basic_information values(N'{}',N'{}',N'{}',N'{}',{},{},N'{}',N'{}',N'{}',{},N'{}',N'{}')".format(
        sql = "insert into basic_information values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}'})".format(
            id,
            name,
            nation,
            sex,
            age,
            tel,
            address,
            marriage,
            drug_allergy,
            medical_history,
            operation_history,
            smoke_history)
        sql1="insert into vital_signs values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id,dt,l_blp,h_blp,bos,hr,pulse,tp,height,weight)

        try:
            # print(sql)
            ms.ExecNonQuery(sql, ())
            ms.ExecNonQuery(sql1,())
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
    def closePage(self):
        if askyesno('确认操作', '确定执行？'):
            self.root.destroy()

