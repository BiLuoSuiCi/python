import datetime,pymysql,time


class mysql_cz():
    '''数据库操作'''
    def __init__(self):
        self.conn = pymysql.connect(host="192.168.2.33",user="admin",password="zy=*986",database="db_pldb",charset="utf8")
        self.cur =self.conn.cursor()

    def select_sql(self,sql):
        '''数据库查询'''

        self.cur.execute(sql)

        return self.cur.fetchall()

    def insert_sql(self,sql):
        '''数据插入'''
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('数据更新成功')
        except:
            self.conn.rollback()
            print('数据库操作失败。执行回滚操作')

    def close(self):
        '''关闭数据库连接'''
        self.cur.close()
        self.conn.close()


def p_cx(c):

    sql1 = f'''SELECT date_format(CONFIRM_PACK_DATE, '%Y-%m-%d'),OPTION_NAME,Model_Code,CAST(SUM(WO_QTY) AS CHAR) AS QTY,date_format(CREATED_TIME, '%Y-%m-%d %H:%i:%s') 
          FROM po_mo,project,dt_pv_options 
          WHERE po_mo.CONFIRM_PACK_DATE{c}'{now}'  
          AND po_mo.Project_ID=project.Project_ID AND po_mo.PRODUCT_LINE_NO=dt_pv_options.BIZ_OBJECT_ID 
          GROUP BY OPTION_NAME,Model_Code,CONFIRM_PACK_DATE ORDER BY CONFIRM_PACK_DATE '''

    sql2 = f'''SELECT date_format(CONFIRM_PACK_DATE, '%Y-%m-%d'),'L1',Model_Code,CAST(SUM(WO_QTY) AS CHAR) AS QTY,date_format(CREATED_TIME, '%Y-%m-%d %H:%i:%s') 
          FROM po_mo,project,dt_pv_options 
          WHERE po_mo.CONFIRM_PACK_DATE{c}'{now}'  
          AND po_mo.Project_ID=project.Project_ID AND po_mo.PRODUCT_LINE_NO=dt_pv_options.BIZ_OBJECT_ID 
          GROUP BY Model_Code,CONFIRM_PACK_DATE ORDER BY CONFIRM_PACK_DATE '''

    return sql1,sql2

def in_sql(r):
    '''构建插入数据语句'''
    return f"insert into line_plan_qty(planDate,lineNo,model,planQty,createdTime) values {r}"

def o_o(sql1,sql2):
    '''获取计划。上传计划'''

    p = ',\n'.join([str(x) for x in cx.select_sql(sql1)]) 

    l = ',\n'.join([str(x) for x in cx.select_sql(sql2)])

    if p:

        ll = p +',\n'+ l

        cx.insert_sql(in_sql(ll))

        cx.close()

        print(ll)

        time.sleep(20)
    else:
        print('计划不存在，请提醒相关负责人。')

        time.sleep(20)
    
 
if __name__ == '__main__':

    #获取当前时间
    now = datetime.datetime.now()

    now_n = now + datetime.timedelta(days=1)

    now = now.date().strftime('%Y-%m-%d')
    #下一天时间
    nextday = now_n.date().strftime('%Y-%m-%d')

    sql = f'''SELECT date_format(planDate, '%Y-%m-%d'),lineNo,model,planQty,date_format(createdTime, '%Y-%m-%d %H:%i:%s') 
              FROM line_plan_qty 
              WHERE planDate='{now}' AND (lineNo='L1' OR lineNo='P1' OR lineNo='P2') '''

    sql3 = f'''SELECT date_format(planDate, '%Y-%m-%d'),lineNo,model,planQty,date_format(createdTime, '%Y-%m-%d %H:%i:%s') 
              FROM line_plan_qty 
              WHERE planDate='{nextday}' AND (lineNo='L1' OR lineNo='P1' OR lineNo='P2') '''    

    cx = mysql_cz()

    b = cx.select_sql(sql)

    nextb = cx.select_sql(sql3)
    #明天工单如果存在，则退出。延时退出
    if nextb:

        c = [str(x) for x in nextb]

        c = ',\n'.join(c)

        b = [str(x) for x in b]

        b = ',\n'.join(b)

        cx.close()

        print('今日计划')
        print(' 计划生产时间   线体    型号    数量        创建日期')
        print(b)
        print('明天计划')
        print(c)

        time.sleep(20)

        exit()

    #明天计划不存在，则尝试获取包装工单。
    if b:

        sql1,sql2 = p_cx('>')

        o_o(sql1,sql2)

    else:

        sql1,sql2 = p_cx('>=')

        o_o(sql1,sql2)

    try:
        cx.close()
    except:
        print('数据库连接已关闭')    


