import pymssql
import pandas as pd
import time
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['simhei'] #windows系统
#plt.rcParams['font.sans-serif']=['Source Han Sans CN']
plt.rcParams['figure.figsize']=[12,5]

def cx_sql(sql):
    '''执行SQL查询语句，返回结果'''
#创建数据库连接实例对象
    conn = pymssql.connect(host="192.168.2.100",user="sa",password="123456",database="mobile")
#创建指针对象
    cur = conn.cursor()           
#执行SQL语句
    cur.execute(sql)
#执行修改语句时，需要提交修改。否则不生效    
    #conn.commit() #提交事务
#提取所有查询的结果
    r = cur.fetchall()
#关闭数据库连接   
    conn.close()
#打印结果
    print('查询到{}条数据'.format(len(r))) 
    return r

def sj_zl(sql3):
    '''对数据整理''' 
    #查询
    r=cx_sql(sql3)

    if r:
        sj = [str(data[0])[10:13] for data in r]

        sjd = set(sj)
        #转换为列表并排序
        sjd = list(sjd)
        sjd.sort()
        print(sjd)
        #统计每个时间段的数量
        cs = [sj.count(sd) for sd in sjd] 
        #返回表格和数量
        return cs,str(len(r)),sjd
    else:
        return [0],0,['07']    
def zlsj():
    '''数据格式统一'''
    cs1,s1,sjd1 = sj_zl(sql1) #包装数据
    cs2,s2,sjd2 = sj_zl(sql2) #写号数据  
    df1 = pd.DataFrame({'卡通箱包装数据':cs1},index=sjd1)
    df2 = pd.DataFrame({'写号数据':cs2},index=sjd2)
    df = pd.merge(df2,df1,how='outer',left_index=True,right_index=True)
    df = df.fillna(0)
    print(df)

    return df,str(s1),str(s2)
def huitu():
    ''' 时间段判断'''
    ti = ['08','09','10','11','12','13','14','15','16','17','18','19','20','21']
    fig = plt.subplot()
    #fig.xaxis.tick_top()
    while True:
        #plt.close()
        #取时间
        t = time.strftime("%X")
        print(t[:2])
        
        if t[:2] in ti:
            plot_sj(fig)
        else:
            exit()
        #刷新间隔
        #time.sleep(50)
        #plt.show()
def plot_sj(fig):
    '''数据可视化'''
    df,s1,s2 = zlsj()
    
    #bz = [(i,int(b)) for i in range(len(df.index))  for b in list(df['卡通箱包装数据'])]
    a = list(range(len(df.index)))

    bz = dict(zip(a,list(df['卡通箱包装数据'])))
        #xh = [(i,int(b)) for i in range(len(df.index))  for b in list(df['写号数据'])]
    xh = dict(zip(a,list(df['写号数据'])))

    plt.cla() #清理画布
        
    #df = pd.DataFrame({'卡通箱包装数据':cs1,'写号数据':cs2},index=sjd)
    print(bz)
    df.plot(kind='bar',rot=0,title=' '.join([rq,'包装线数据看板']),ax=fig,ylim=[0,3000]) #包装数据
    #df1.plot(kind='bar',rot=0,grid=True,ax=ax1) #写号数据
    plt.text(-0.5,2700,''.join(['当前包装数量：',s1]))
    plt.text(-0.5,2850,''.join(['当前写号数量：',s2]))
    for x1,y1 in bz.items():
        plt.text(x1+0.01,y1+10,str(int(y1)))
    for x2,y2 in xh.items():
        plt.text(x2-0.3,y2+10,str(int(y2)))
    #fig.invert_yaxis()
    plt.pause(30)

if __name__ == '__main__':

    #scx = '写号'
    t = time.strftime("%Y-%m-%d %X")
    t = str(t)
    
    rq = t[:10]
    print(rq)

    sql1 = '''SELECT dysj
              FROM ktxb 
              WHERE convert(varchar,dysj,120) like '{}%' '''.format(rq)

    sql2 = '''SELECT xhsj
             FROM dhmx 
             WHERE convert(varchar,xhsj,120) like '{}%' '''.format(rq)

    #plt.grid(axis='y',color='r')#绘制y轴刻度
  
    plt.style.use('ggplot') #设置图表风格
    stype = ['bmh', 'classic', 'dark_background', 'fast', 
           'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 
           'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 
           'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 
           'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 
           'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 
           '_classic_test'] #支持风格样式

    huitu()
    #zlsj()
    #plt.show()
