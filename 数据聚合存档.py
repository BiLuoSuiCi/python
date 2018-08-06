import pymysql
import pandas as pd


def select_sql(sql):

    con = pymysql.connect(host="192.168.2.33",user="admin",password="zy=*986",database="db_pldb",charset="utf8")

    df = pd.read_sql(sql=sql,con=con)

    con.close()

    return df
def insert_sql(qt):

    sql1 = f"insert into qty_p(Model_Code,PUT_QUT,GET_QTY) values {qt}"

    con = pymysql.connect(host="192.168.2.55",user="admin",password="zy=*986",database="chuhuo",charset="utf8")

    cur = con.cursor()

    cur.execute(sql1)

    con.commit()

    cur.close()

    con.close()        

sql = "SELECT Model_Code,SUM(PUT_QTY) AS P,SUM(GET_QTY) AS G FROM work_orders WHERE FSTATUS='13030010' AND order_nature='2' GROUP BY Model_Code"    

a = select_sql(sql)

a[['P','G']] = a[['P','G']].astype(int)
#a = [str(x) for x in a]
#a = ",".join(a)
#insert_sql(a)
s

for i in a.index:
    aa = a.loc[i].values[0:]
    aa = tuple(aa)
    print(aa)

#print(a.index)