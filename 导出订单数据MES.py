import pymysql
import pandas as pd 
import xlrd
import os
import tkinter
import datetime
import shutil

def sql_lianjie(sql1,rq,ktxtms):

    conn = pymysql.connect(host="192.168.2.33",user="admin",password="zy=*986",database="db_pldb",charset="utf8")
    #查询使用带中文的语句需使用charset='utf8'
#查询语句一    
    df = pd.read_sql(sql=sql1,con=conn)

    conn.close()
    #print(df)
    model = df['MODEL_CODE']
    #提取机型型号，并过滤
    model = list(set(model))
  
    
    if len(model) != 1:
        print('请分离区别不同机型箱号数据！！！\n'*3)
        exit()
    else:
        model = model[0]
        del df['MODEL_CODE']

    sl = len(df)
    #统计各颜色数量
    print('-'*60)
    print(f'   机型：{model}\n') 
    print(df['颜色'].value_counts())
    print('-'*60)
    print(f'   总数量为  {sl} \n')
    print('-'*60)
    cpath = os.sep.join(['D:','python','chuhuo',rq])
    try:
        os.makedirs(cpath)
    except:
        print('目录已存在')    
    imei_path = f"{cpath}\\{model}({sl}pcs出货IMEI清单){rq}.xlsx"
    box_path = f"{cpath}\\{model}({sl}pcs出货装箱清单){rq}.xlsx"
    #r'{}\{}({}pcs出货IMEI清单){}.xlsx'.format(cpath,model,sl,rq)
    #{}\{}({}pcs出货装箱清单){}.xlsx
    df.to_excel(imei_path,index=False)

    print('清单导出完成。开始整理装箱清单。',end="\r")

    #取箱号唯一值
    df.drop_duplicates('箱号',keep='last',inplace=True)
    #
    print('开始查询箱号是否全部获得',end="\r")
    a = 0
    ktxtms_2 = list(df['箱号'])
   
    for ktxtm in ktxtms:
        if ktxtm not in ktxtms_2:
            
            a += 1
            print("以下数据未查询到：{} \n".format(a))
            with open(cpath +r'\未查询到数据.txt','a') as rz:
                rz.write(ktxtm + '\n')
            print(ktxtm)
            print('\n')
    

    gs = ['箱号','实装数量','物料编码','颜色','SNCODE','VERSION_CODE','EAN','PIN']
    #重命名列名称
    df = pd.DataFrame(df,columns=gs)

    print(f'开始导出  {len(df)}  个箱号出货装箱数据')

    df.to_excel(box_path,index=False)
    
    if a:
        os.remove(imei_path)
        os.remove(box_path)
    else:
        print('导出完成',end='\r')    

def pr_out(ktxtms):    
    '''IMEI清单查询'''
    #转换当前日期格式为20180101  
    rq = str(datetime.datetime.now().date().strftime('%Y%m%d'))
    
    sql1 = f'''SELECT BOX_NO as '箱号',
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
    PIN,
    MODEL_CODE 
    FROM imei_box_detail 
    WHERE BOX_NO IN {ktxtms}'''#.format(ktxtms)
     
    #print(rq)
    #提取查询结果
    sql_lianjie(sql1,rq,ktxtms)
          
    #bt1 = ['箱号','实装数量','净重','毛重','物料编码','IMEI1','IMEI2','IMEI3',
    #           'IMEI4','SN','VCCODE','盒重','颜色','SNCODE','VERSION_CODE',
    #           'EAN','PIN']
    #bt2 = ['箱号','实装数量','物料编码','颜色','生产日期代码','N标识','EAN','PIN']
def saomiao_zl():

    rq = str(datetime.datetime.now().date().strftime('%Y%m%d'))
    #整理出货扫描数据
    cpath = os.sep.join(['D:','python','ktxtms',rq])

    try:
        os.makedirs(cpath)
    except:
        print('>>>>>>')
    wpath = r'D:\python\ktxtms'
    #取根目录文件
    maindir, subdir, file_name_list = os.walk(wpath).__next__()  

    if file_name_list:
        for file_k in file_name_list:

            file_k = os.path.join(maindir,file_k)
        
            shutil.move(file_k,cpath)


if __name__ == '__main__':

    app = tkinter.Tk()

    app.geometry('300x220+500+50')

    app.title('数据导出')
    
    wpath = r'D:\python\ktxtms'

    os.system('shujubidui.py')

    listbox = tkinter.Listbox(app,width=42,height=10)

    #提取excel文档加入列表
    for i in os.listdir(wpath):
        #文件过滤
        if os.path.splitext(i)[1] == '.xlsx':
            listbox.insert(0,i)

    listbox.grid(row=2,column=0)

    def dc_sj():

        biaoge = os.sep.join([wpath,listbox.selection_get()])
    
        print(biaoge)
#读取excel文档
        global dflist
        dflist = []
        try:
            excels = xlrd.open_workbook(biaoge)
           
            for sheet in excels.sheets():
                print(sheet.name)
                df = pd.read_excel(biaoge,sheet.name)
                
                dflist.append(df)
            df = pd.concat(dflist,axis=0)
        except:
            print('文件打开失败！请检查文件名称的正确性！\n')
            exit()
#将所有列合并
        #定义全局变量 
        #global ktxtms
        ktxtms = []
        #箱号清理、聚合
        
        #print(df)
        for i in list(df.columns):
	        ktxtms += list(df[i].dropna(axis=0))
        #箱号重复性验证
        #print(ktxtms)
        if len(ktxtms) == len(set(ktxtms)):
            print('\n箱号无重复，开始下一步整理。\n')
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
        
        #print(ktxtms)
        #exit()
        pr_out(ktxtms)

        lb = tkinter.Label(text='导出完成',bg="green")

        lb.grid(row=5,column=0)
#实例化按钮控件        
    btn = tkinter.Button(text='出货数据导出',command=dc_sj)
    btn2 = tkinter.Button(text='扫描数据归档',command=saomiao_zl)
    btn.grid(row=5,column=0,sticky=tkinter.W)  
    btn2.grid(row=5,column=0,sticky=tkinter.E)    

    app.mainloop()