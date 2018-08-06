import datetime,pymysql,time
import pandas as pd

def mysql_c(sql,cx=False):
    conn = pymysql.connect(host="192.168.2.33",user="admin",password="zy=*986",database="db_pldb",charset="utf8")
    if cx:
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            return "计划上传成功"
        except:
            conn.rollback()
            return "计划上传失败"
        cur.close()    
        conn.close()
    else:    
        df = pd.read_sql(sql=sql,con=conn)

        conn.close()

        return df
   
def print_qty(oneday,now):

    sql = f'''SELECT CONFIRM_PACK_DATE,OPTION_NAME,Model_Code,SUM(WO_QTY) AS QTY FROM
            po_mo,project,dt_pv_options WHERE po_mo.CONFIRM_PACK_DATE='{oneday}'  
            AND po_mo.Project_ID=project.Project_ID AND po_mo.PRODUCT_LINE_NO=dt_pv_options.BIZ_OBJECT_ID 
            GROUP BY OPTION_NAME,Model_Code '''

    sql2 = f'''SELECT CONFIRM_PACK_DATE,OPTION_NAME,Model_Code,SUM(WO_QTY) AS QTY FROM
            po_mo,project,dt_pv_options WHERE po_mo.CONFIRM_PACK_DATE='{oneday}'  
            AND po_mo.Project_ID=project.Project_ID AND po_mo.PRODUCT_LINE_NO=dt_pv_options.BIZ_OBJECT_ID 
            GROUP BY Model_Code '''            
    jieguo = mysql_c(sql)
    jieguo_l = mysql_c(sql2)
    qty = []
    qty_l = []

    if len(jieguo):  
    #转换列数据类型
        jieguo['CONFIRM_PACK_DATE'] = jieguo['CONFIRM_PACK_DATE'].astype(str)

        jieguo['QTY'] = jieguo['QTY'].astype(int)

        jieguo['QTY'] = jieguo['QTY'].astype(str)
        #写号线处理
        jieguo_l['CONFIRM_PACK_DATE'] = jieguo_l['CONFIRM_PACK_DATE'].astype(str)

        jieguo_l['QTY'] = jieguo_l['QTY'].astype(int)

        jieguo_l['QTY'] = jieguo_l['QTY'].astype(str)        

        
        for a in jieguo.index:

            jihua = list(jieguo.loc[a].values[0:])

            jihua.append(str(now))

            jihua = str(tuple(jihua))

            print(jihua)

            qty.append(jihua)


        for a in jieguo_l.index:

            jihua_l = list(jieguo_l.loc[a].values[0:])

            jihua_l.append(str(now))
            #复制包装计划到写号线

            jihua_l[1] = "L1"
            #print(jihua_l)
            jihua_l = str(tuple(jihua_l))

            qty_l.append(jihua_l) 

        qty.extend(qty_l)
        #print(qty) 
        #join针对字符串进行连接
        qt = ",".join(qty)
        #print(qt) 
        sql = f"insert into line_plan_qty(planDate,lineNo,model,planQty,createdTime) values {qt}"
        #print(sql)
        return sql
    else:
        pass
        #return None    
def up_jihua(sql):

    make = mysql_c(sql=sql,cx=True)

    print(make)

def get_date(days):

    now = datetime.datetime.now()

    now_n = now + datetime.timedelta(days=days)

    oneday = now_n.date().strftime('%Y-%m-%d')

    print(f'尝试获取：{oneday} 工单',end='\r')

    sql = print_qty(oneday,now)

    return sql,oneday

def up_yes_no():
   
    zhi = input("\n是否上传计划(Y/N):").lower()

    print(zhi)

    if zhi == "y":
        up_jihua(sql)
        print('3秒后自动退出')
        time.sleep(3)
    else:
        pass    

def now_plan():

    now = datetime.datetime.now()

    now_n = now + datetime.timedelta(days=1)
    now_n = now_n.date().strftime('%Y-%m-%d')
    now = now.date().strftime('%Y-%m-%d')
    #今日计划语句构建
    sql = f"SELECT planDate,lineNo,model,planQty,createdTime FROM line_plan_qty WHERE planDate='{now}' AND (lineNo='L1' OR lineNo='P1' OR lineNo='P2')"
    now_pl = mysql_c(sql)
    #明日计划语句构建
    sql1 = f"SELECT planDate,lineNo,model,planQty,createdTime FROM line_plan_qty WHERE planDate='{now_n}' AND (lineNo='L1' OR lineNo='P1' OR lineNo='P2')"
    tom_pl = mysql_c(sql1)
    #print(tom_pl)
    if len(now_pl):
        print('今日计划')
        print(now_pl,'\n')
    if len(tom_pl):
        print('明日计划')
        print(tom_pl,'\n') 
        print('5秒后退出')       
        time.sleep(5)
        exit()

if __name__ == "__main__":
  
    now_plan()

    i = 1
    while i < 6:

        sql,oneday = get_date(i)
        
        if sql:

            up_yes_no()

            break
        else:
            print(f"{oneday}  包装工单获取失败")
        
            print(f'尝试获取 {i+1} 天后工单',end='\r')    
            i = i + 1
    else:

        print('获取失败，请拉取sap工单。或者，让计划卖个萌。\n')   
        
        print('十秒后自动关闭窗口。。。 。。。')

        time.sleep(10)


    
        
