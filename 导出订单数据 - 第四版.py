import pymssql
import pandas as pd 
import os
import tkinter

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
        WHERE ktxtm IN {} ORDER BY ktxtm'''.format(ktxtms)
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
          WHERE ktxtm IN {} ORDER BY ktxtm'''.format(ktxtms)

#提取查询结果
    imei,zx = sql_lianjie(sql1,sql2)
   
    if len(imei):    
        bt1 = ['箱号','实装数量','净重','毛重','物料编码','IMEI1','IMEI2','IMEI3',
               'IMEI4','SN','VCCODE','盒重','颜色','SNCODE','VERSION_CODE',
               'EAN','PIN']
        bt2 = ['箱号','实装数量','物料编码','颜色','生产日期代码','N标识','EAN','PIN']

        df1 = pd.DataFrame(imei,columns=bt1)

        df2 = pd.DataFrame(zx,columns=bt2)

        df2 = df2.drop_duplicates(['箱号'],keep='last')


        if len(imei)/40 != len(zx):
            print('数据有出入。注意复查！差值：{}\n'.format(len(imei)/40 - len(zx)))
            rq = ''.join([rq,'注意数据复查'])

        print('本次整理出货数据：{}个卡通箱。装箱清单共{}个卡通箱。\n'.format(int(len(imei)/40),len(zx)))

        shuju_bd(list(df2['箱号']))#数据整理完成后对比

                                       
        df1.loc[df1['颜色']=='ORANGE',['物料编码','EAN']] = ('10008365','4895180725395')
        df1.loc[df1['颜色']=='DARK BLUE',['物料编码','EAN']] = ('10008366','4895180725401')
        df1.loc[df1['颜色']=='CHAMPAGNE GOLD',['物料编码','EAN']] = ('10008367','4895180725418')
        #df1.loc[df1['毛重'].isnull(),'毛重'] = '11.03'
        
        try:
        #尝试补充数据
            print('重量数据缺失检测：\n{}\n'.format(set(df1.loc[df1['毛重']=='','箱号'])))
            

            df1.loc[df1['毛重']=='','毛重'] = '11.13'
            
        except:

            df1.loc[df1['毛重'].isnull(),'毛重'] = '11.13'   

        #print(df1.loc[df1['毛重']=='','毛重'])
        #exit()
        df2.loc[df2['颜色']=='ORANGE',['物料编码','EAN']] = ('10008365','4895180725395')
        df2.loc[df2['颜色']=='DARK BLUE',['物料编码','EAN']] = ('10008366','4895180725401')
        df2.loc[df2['颜色']=='CHAMPAGNE GOLD',['物料编码','EAN']] = ('10008367','4895180725418') 
        #df2.loc[df2['SNCODE'].isnull(),'SNCODE'] = 'H5'
        try:
        #尝试补充数据
            print('生产日期数据缺失检测：\n{}\n'.format(set(df2.loc[df2['生产日期代码'].isnull(),'生产日期代码'])))    
            
            df2.loc[df2['生产日期代码'].isnull(),'生产日期代码'] = 'H5'
            
        except:

            df2.loc[df2['生产日期代码']=='','生产日期代码'] = 'H5' 

        print('开始导出.......\n')
        
        df1.to_excel(r'D:\python\chuhuo\it5625({}pcs出货IMEI清单){}.xlsx'.format(str(len(imei)),rq),index=False)
        df2.to_excel(r'D:\python\chuhuo\it5625({}pcs出货装箱清单){}.xlsx'.format(str(len(imei)),rq),index=False)

        print('导出完成！\n')
    else:
        print('未搜索到')
def shuju_bd(ktxh):

    print('开始检测箱号数据，是否获取完全。\n')

    for ktxraw in ktxtms:
        if ktxraw not in ktxh:

            print('卡通箱号: {} 无记录数据，请检测完毕后再次运行\n'.format(ktxraw))
            
        else:
            pass
            
    print('提供的箱号，已全部查询到数据记录。开始按照模板优化数据... ... \n')
    
if __name__ == '__main__':

    app = tkinter.Tk()
    app.geometry('300x300+500+100')
    #cc = [['橙色','10008365','ORANGE','4895180725395'],
    #      ['深蓝色','10008366','DARK BLUE','4895180725401'],
    #      ['香槟金','10008367','CHAMPAGNE GOLD','4895180725418']]
    app.title('数据导出')
    
    wpath = r'D:\python\ktxtms'

    listbox = tkinter.Listbox()


    #提取excel文档加入列表
    for i in os.listdir(wpath):
        #文件过滤
        if os.path.splitext(i)[1] == '.xlsx':
            listbox.insert(0,i)

    listbox.grid(row=2,column=2)

    def dc_sj():

        biaoge = os.sep.join([wpath,listbox.selection_get()])
    
        print(biaoge)
#读取excel文档
        try:

            df = pd.read_excel(biaoge)
    
        except:
            print('文件打开失败！请检查文件名称的正确性！\n')
            exit()
#将所有列合并
        #定义全局变量 
        global ktxtms
        ktxtms = []
        #箱号清理、聚合
        for i in list(df.columns):
	        ktxtms += list(df[i].dropna(axis=0))
        #箱号重复性验证
        if len(ktxtms) == len(set(ktxtms)):
            print('箱号无重复，开始下一步整理。\n')
        else:
            print('箱号    重复   请   复   查   后   继续！！！！！！！！！！！！！！！！！！')
            exit()        
#转换为字符串元组
        try:
            print('尝试转换\n')
            ktxtms = tuple(str(int(i)) for i in ktxtms)
        except:
            print('直接转换为字符串\n')
            ktxtms = tuple(str(i) for i in ktxtms)

        #print(ktxtms,'\n')
    
        print('获取箱号数量：%s \n' % len(ktxtms))
        #exit()
        rq = os.path.split(biaoge)[1]
    
        rq = rq[4:8]

        pr_out(ktxtms,rq)

        lb = tkinter.Label(text='导出完成',bg="green")

        lb.grid(row=3,column=5)
#实例化按钮控件        
    btn = tkinter.Button(text='出货数据导出',command=dc_sj)

    btn.grid(row=2,column=5)    

    app.mainloop()