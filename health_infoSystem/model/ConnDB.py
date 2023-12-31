import pymysql


class ConnDB(object):
    def __init__(self, as_dict=True):
        super(ConnDB, self).__init__()
        self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.password = "123456"
        self.charset = "utf-8"
        self.database = "healthinfosys"
        self.autocommit = True


    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.database:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                    database=self.database, autocommit=self.autocommit, charset='utf8')
        self.cur = self.conn.cursor()
        if not self.cur:
            raise (NameError, "连接数据库失败")
        else:
            return self.cur

    """
    增加一条记录
    """
    """
    执行查询语句
    """
    def ExecQuery(self, sql, args=(), restype="all"):
        """
        执行查询语句
        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        # 执行sql语句
        cur.execute(sql, args)
        # 获取数据
        if restype == "one":
            resList = cur.fetchone()  # 获取一条数据
        elif isinstance(restype, int):
            resList = cur.fetchmany(int(restype))  # 自定义获取数据
        else:
            resList = cur.fetchall()
        return resList

    """
    执行非查询语句
    """
    def ExecNonQuery(self, sql, args=()):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        # try:
        cur.execute(sql.encode("utf-8"), args)
        self.conn.commit()
        # except Exception as e:
        #     self.conn.rollback()
        #     print(str(e))
    """
    关闭数据库连接
    """
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
            return True
        raise Exception("not conn and cur")
