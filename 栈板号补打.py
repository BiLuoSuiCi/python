import pymysql
import pandas as pd

def plan_cx(boxn):
    sql = f"SELECT PLAN,BOX_NO FROM plan_ch WHERE PLAN in (SELECT PLAN FROM plan_ch WHERE BOX_NO='{boxn}' OR PLAN='{boxn}')"
    print(sql)
   
    conn = pymysql.connect(host="192.168.2.55",user="admin",password="zy=*986",database="chuhuo",charset="utf8")

    df = pd.read_sql(sql,conn)

    conn.close()
    if len(df):
        return tuple(df['BOX_NO']),list(set(df['PLAN']))[0]
    else:
        return None,None
print(plan_cx('46201808060005'))