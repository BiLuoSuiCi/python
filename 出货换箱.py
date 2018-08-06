import pymysql
import win32com.client as com

def mysql_select(sql):

    conn = pymysql.connect(host="192.168.2.55",user="admin",password="zy=*986",database="chuhuo",charset="utf8")

    cur = conn.cursor()

    cur.execute(sql)
    #查询结果返回的为一个元组
    txt = cur.fetchall()

    conn.close()

    return txt


def f(x):
    
    return x[1]+'\n'

    
sql = "SELECT PLAN,BOX_NO FROM plan_ch WHERE PLAN='4620180713001'"

jieguo = mysql_select(sql)

boxs = tuple(map(f,jieguo))

boxstxt = ''.join(boxs)
print(len(boxs),boxstxt)   