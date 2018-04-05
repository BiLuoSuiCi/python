import pymssql
import pandas as pd 


def sql_lianjie(sql1,sql2=None):

    conn = pymssql.connect(host="192.168.2.100",user="sa",password="123456",database="mobile")
#查询语句一    
    cur1 = conn.cursor()

    cur1.execute(sql1)

    r1 = cur1.fetchall()
#查询语句二
    if sql2:
        cur2 = conn.cursor()

        cur2.execute(sql2)

        r2 = cur2.fetchall()
#查询完毕关闭连接
        return r1,r2
    else: 
        return r1 

    conn.close()

    

def pr_out(ktxtms,rq):    
#IMEI清单查询
    sql1 = '''SELECT
        ktxtm,
        sl,
        '10.45',
        zl,
        '',
        imei1,
        imei2,
        meid1,
        '',
        '',
        psn,
        '260',
        color,
        msn,
        'N7',
        '',
        ''
        FROM ktxb 
        WHERE ktxtm IN {}  
        '''.format(ktxtms)
#装箱清单查询
    sql2 = '''SELECT DISTINCT(ktxtm),
          '40',
          '',
          color,
          msn,
          'N7',
          '',
          '' 
          FROM ktxb 
          WHERE ktxtm IN {} 
          '''.format(ktxtms)
#提取查询结果
    imei,zx = sql_lianjie(sql1,sql2)
   
    if len(imei):    
        bt1 = ['箱号','实装数量','净重','毛重','物料编码','IMEI1','IMEI2','IMEI3',
               'IMEI4','SN','VCCODE','盒重','颜色','SNCODE','VERSION_CODE',
               'EAN','PIN']
        bt2 = ['箱号','实装数量','物料编码','颜色','生产日期代码','N标识','EAN','PIN']
        df1 = pd.DataFrame(imei,columns=bt1)
        df2 = pd.DataFrame(zx,columns=bt2)
        print('开始整理数据.........',int(len(imei)/40),len(zx))
        df1['毛重'].isnull()
        if len(imei)/40 != len(zx):
            print('数据有出入。注意复查！差值：',len(imei)/40 - len(zx))
            rq = ''.join([rq,'注意检查箱号数据重复'])
        df1.loc[df1['颜色']=='ORANGE',['物料编码','EAN']] = ('10008365','4895180725395')
        df1.loc[df1['颜色']=='DARK BLUE',['物料编码','EAN']] =('10008366','4895180725401')
        df1.loc[df1['颜色']=='CHAMPAGNE GOLD',['物料编码','EAN']] =('10008367','4895180725418')
        df2.loc[df2['颜色']=='ORANGE',['物料编码','EAN']] = ('10008365','4895180725395')
        df2.loc[df2['颜色']=='DARK BLUE',['物料编码','EAN']] =('10008366','4895180725401')
        df2.loc[df2['颜色']=='CHAMPAGNE GOLD',['物料编码','EAN']] =('10008367','4895180725418')    
        print('导出.......')
        
        df1.to_excel('it5625({}pcs出货IMEI清单){}.xlsx'.format(str(len(imei)),rq),index=False)
        df2.to_excel('it5625({}pcs出货装箱清单){}.xlsx'.format(str(len(imei)),rq),index=False)
        print('导出完成！')
    else:
        print('未搜索到')

if __name__ == '__main__':

    #cc = [['橙色','10008365','ORANGE','4895180725395'],
    #      ['深蓝色','10008366','DARK BLUE','4895180725401'],
    #      ['香槟金','10008367','CHAMPAGNE GOLD','4895180725418']]

    df = pd.read_excel('20180404.xlsx')
    #箱号列表化
    ktxtms = []

    for i in list(df.columns):
	    ktxtms += list(df[i])

    #ktxtms = [str(i) for i in df['ktxtm']]
    
    #ktxtms.sort()

    ktxtms = tuple(ktxtms)

    print(ktxtms)

    #pr_out(ktxtms,'0404')
    
    print('结束')            