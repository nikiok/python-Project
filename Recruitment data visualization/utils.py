import time
import pymysql
import pandas as pd

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="123456",
                           db="jobs",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_index_data():

    sql = "select * from df"
    res = query(sql)
    return res
def get_salary1_data():

    sql = "select 行业领域,平均薪水 from df group by 行业领域"
    res = query(sql)
    return res

def get_salary2_data():

    sql = "SELECT 薪水等级, COUNT(*) AS 分布数量 FROM df GROUP BY 薪水等级"
    res = query(sql)
    return res
def get_salary3_data():
    conn=get_conn()[0]
    sql="SELECT 行业领域, 平均薪水 FROM df"
    df = pd.read_sql_query(sql, conn)
    res = [group['平均薪水'].values for _, group in df.groupby('行业领域')]
    return res
def get_region1_data():

    sql = "SELECT 省份 , COUNT(标题) AS 岗位需求 FROM df group by 省份"
    res = query(sql)
    return res

def get_region2_data():

    sql = "SELECT 城市 , COUNT(标题) AS 岗位需求 FROM df group by 城市 order by 岗位需求 DESC limit 10"
    res = query(sql)
    return res

def get_edu1_data():

    sql = "SELECT 工作经验, COUNT(*) AS 数量 FROM df GROUP BY 工作经验 ORDER BY 数量"
    res = query(sql)
    return res

def get_edu2_data():

    sql = "SELECT 学历 , COUNT(标题) AS 数量 FROM df group by 学历 order by 数量 "
    res = query(sql)
    return res

def get_company1_data():
    word_li=[('五险一金', 6939),
     ('绩效奖金', 4672),
     ('年终奖金', 4476),
     ('专业培训', 3728),
     ('定期体检', 3418),
     ('餐饮补贴', 3233),
     ('员工旅游', 2603),
     ('通讯补贴', 2391),
     ('交通补贴', 2290),
     ('节日福利', 1885),
     ('弹性工作', 1839),
     ('带薪年假', 1818),
     ('周末双休', 1639),
     ('补充医疗保险', 1317),
     ('无需经验', 817),
     ('大数据', 668),
     ('免费班车', 597),
     ('六险一金', 516),
     ('出国机会', 460),
     ('下午茶', 438)]
    return word_li

def get_company2_data():
    sql = "SELECT 行业领域, count(公司名字) AS 公司数量 FROM df GROUP BY 行业领域  ORDER BY 公司数量 DESC limit 20 "
    res = query(sql)
    return res

def get_company3_data():
    sql = "SELECT 公司规模, count(公司名字) AS 公司数量 FROM df GROUP BY  公司规模 ORDER BY 公司数量 DESC limit 20 "
    res = query(sql)
    return res

def get_company4_data():
    sql = "SELECT 经营类型, count(公司名字) AS 公司数量 FROM df GROUP BY 经营类型  ORDER BY 公司数量 DESC limit 20 "
    res = query(sql)
    return res

if __name__ == "__main__":
    print(get_salary3_data())
    d = get_salary3_data()
