import pymysql
import pandas as pd
import win32com.client as com
import datetime
import pythoncom,PyHook3


###############################################################################################################
rq = str(datetime.datetime.now().date().strftime('%Y%m%d'))                                                   #
with open('plan.txt','r') as p:                                                                               #
    s = p.read()

print(s)
key_code = ''

bo = int(s) if s[2:10]==rq else int(f"46{rq}000")  
print(s[2:10])

BOX_list = []

mk = 0
#实例化标签
w = com.DispatchEx('bartender.Application')
#模板是否可见
w.Visible = 1   

btformat = w.formats.open(r'D:\传音资料\itel_印度标签模板更新BIS标准号_20180307\模板\栈板信息.btw',True,'')
################################################################################################################
def sql_out(sql):

    conn = pymysql.connect(host="192.168.2.33",user="admin",password="zy=*986",database="db_pldb",charset="utf8")

    df = pd.read_sql(sql=sql,con=conn)

    conn.close()

    return df

def sql_in(qt):

    sqlin = f"insert into plan_ch(PLAN,QTY,BOX_NO) values {qt}"

    #print(sqlin)

    conn = pymysql.connect(host="192.168.2.55",user="admin",password="zy=*986",database="chuhuo",charset="utf8")

    cur = conn.cursor()

    cur.execute(sqlin)

    conn.commit()
    
    conn.close()


def printer(plan,boxs,txt,boxtxt):
    #输入栈板号
    btformat.setnamedsubstringvalue('PLAN',plan)
    #输入箱号
    btformat.setnamedsubstringvalue('BOX_NO',boxs)
    #输入栈板信息1
    btformat.setnamedsubstringvalue('TEXT',txt)
    #输入栈板信息2
    btformat.setnamedsubstringvalue('BOXS',boxtxt)

    btformat.printout(False,False)
    #关闭标签模板。1为保存，0为不保存（True=1，False=0）。
    #btformat.close(1) 

def df_zl(df):
    bs = []
    global bo

    model = df['MODEL_CODE']
    #提取机型型号，并过滤
    model = list(set(model))
  
    if len(model) != 1:
        print('请分离区别不同机型箱号数据！！！\n'*3)
        exit()
    else:
        model = model[0]
        del df['MODEL_CODE'] 
    #统计各颜色数量
    tj = str(df['颜色'].value_counts()).replace('Name: 颜色, dtype: int64','')

    txt = f"机型：{model} \n{tj}\n总数量为:  {len(df)} \n"

    df.drop_duplicates('箱号',keep='last',inplace=True)

    box = list(df['箱号'])

    boxs = [x+"\n" for x in box]

    x = len(box)

    bo += 1

    plan = str(bo)

    for i in range(x):
        b = (plan,x,box[i])
        bs.append(str(b))

    qt = ",".join(bs)

    sql_in(qt)

    boxs_txt = "".join(boxs)

    txt = txt + f"箱数：{x}"

    printer(plan,boxs_txt,txt,boxs_txt)

    with open('plan.txt','w') as s:
        s.write(plan)

def gjsql(ktxtms):

    sql = f'''SELECT BOX_NO as '箱号',
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
    WHERE BOX_NO IN {ktxtms}'''
    #print(sql)
    return sql

def OnKeyboardEvent(event):

    global key_code,mk
    #print ('Window:',event.Window)
    if event.WindowName == '发货扫描':

        if event.Key != "Return":
            key_code += chr(event.Ascii)
        else:
        #print(key_code)
            if mk == 1:
                if key_code in BOX_list:
                    BOX_list.remove(key_code)
                    print(f'删除箱号 {key_code}')
                mk = 0
                key_code = ''

            elif(key_code == '101011'):
                
                key_code = ''
                mk = 1 
                print('再次扫描将移除箱号')

            elif(key_code == '101010'):
                
                ktxtms = tuple(BOX_list)
                if ktxtms:

                    print(len(BOX_list))

                    df = sql_out(gjsql(ktxtms))
    
                    df_zl(df)

                    BOX_list.clear()

                
                print('打印完毕。\n准备下一栈板。',end='')

            elif(key_code not in BOX_list and key_code !='' and len(key_code) == 14):
                key_code.replace(' ','')
                BOX_list.append(key_code)
                print ('扫描:',key_code,mk,)
                     
        #print (event.WindowName,end='\r')
        
            print(f"已扫入箱数： {len(BOX_list)}               ",end='\r')
            key_code = ''
  
    return True


if __name__ == "__main__":
    
    #注册键盘钩子
    hooks_manager = PyHook3.HookManager()
    hooks_manager.KeyDown = OnKeyboardEvent
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()

    w.quit(1)
    print('结束老雷')