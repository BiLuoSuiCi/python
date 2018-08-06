import pymysql
import datetime
import pandas as pd


def pd_sql(sql):

    con = pymysql.connect(host="192.168.2.33",user="admin",password="zy=*986",database="db_pldb",charset="utf8")

    df = pd.read_sql(sql=sql,con=con)

    con.close()

    return df
    
sql = "SELECT Work_Order,Plan_Qty,GET_QTY,PUT_QTY,market FROM work_orders WHERE FSTATUS='13030010' AND order_nature='2'"    

print(pd_sql(sql))