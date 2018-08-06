import pymysql
import pandas as pd 
#import os
#import xlrd
import datetime



def sql_lianjie(sql1,rq):

    conn = pymysql.connect(host="192.168.2.33",user="admin",password="zy=*986",database="db_pldb",charset="utf8")
    #查询使用带中文的语句需使用charset='utf8'
#查询语句一    
    df = pd.read_sql(sql=sql1,con=conn)

    conn.close()
    #print(df)
    sl = len(df)
    print('开始导出清单。共{}条数据'.format(sl))

    df.to_excel(r'D:\python\chuhuo\it5625({}pcs出货IMEI清单){}.xls'.format(sl,rq),index=False)

    print('清单导出完成。开始整理装箱清单。')

    #取箱号唯一值
    df.drop_duplicates('箱号',keep='last',inplace=True)
    #
    gs = ['箱号','实装数量','物料编码','颜色','SNCODE','VERSION_CODE','EAN','PIN']

    df = pd.DataFrame(df,columns=gs)

    print('开始导出{}个数据'.format(len(df)))

    df.to_excel(r'D:\python\chuhuo\it5625({}pcs出货装箱清单){}.xls'.format(sl,rq),index=False)

    print('导出完成')

def pr_out():    
    '''IMEI清单查询'''
    #转换当前日期格式为20180101
    rq = datetime.datetime.now().date().strftime('%Y%m%d')
    rq = str(rq)

    sql1 = '''SELECT BOX_NO as '箱号',
    ACT_BOX_PER_QTY as '实装数量',
    FORMAT(NET_WEIGHT,2) as '净重',
    FORMAT(GROSS_WEIGHT,2) as '毛重',
    MAT_CODE as '物料编码',
    IMEI1,
    IMEI2,
    IMEI3,
    IMEI4,
    SN,
    VCCODE,
    BOX_WEIGHT as '盒重',
    COLOR as '颜色',
    SNCODE,
    VERSION_CODE,
    EAN,
    PIN 
    FROM imei_box_detail 
    WHERE batchCode='{}' or batchCode='{}' or batchCode='{}' or batchCode='{}' or batchCode='{}' '''.format('20180530','20180531','20180601','20180602',rq)

       
    print(rq)
    #提取查询结果
    sql_lianjie(sql1,rq)
          
    #bt1 = ['箱号','实装数量','净重','毛重','物料编码','IMEI1','IMEI2','IMEI3',
    #           'IMEI4','SN','VCCODE','盒重','颜色','SNCODE','VERSION_CODE',
    #           'EAN','PIN']
    #bt2 = ['箱号','实装数量','物料编码','颜色','生产日期代码','N标识','EAN','PIN']

if __name__ == '__main__':

    pr_out()