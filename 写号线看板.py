import matplotlib.pyplot as plt
import pandas as pd
import pymysql


plt.rcParams['font.sans-serif']=['simhei'] #windows系统
#plt.rcParams['font.sans-serif']=['Source Han Sans CN']
plt.rcParams['figure.figsize']=[13,7]

def hq_qty(sql):
    con = pymysql.connect(host="192.168.2.33",user="admin",password="zy=*986",database="db_pldb",charset="utf8")
    try:
        df = pd.read_sql(sql=sql,con=con,index_col='m') 
    except:
        print('err')
    con.close()

    return df

sql= "SELECT Model_Code AS m,SUM(PUT_QTY) AS p,SUM(GET_QTY) AS g FROM work_orders WHERE FSTATUS='13030010' AND order_nature='2' GROUP BY Model_Code" 

#df = hq_qty(sql)

#df.plot(kind='bar')

#print(df)
#plt.plot(df.index,df['g'])


def plot_bar():
    df = hq_qty(sql)
    try:

        plt.cla()
        
        plt.grid(axis='y', linestyle=':')

        plt.bar(df.index,df['g'],fc='dodgerblue',alpha=1)
        #标注每个机型产出
        for x,y in zip(df.index,df['g']):
            plt.text(x,y+130,int(y),size=12)
        #标注总产出
        #plt.text(0,300000,f"总产出： {int(df['g'].sum())}",size=18) 
        plt.title(f"写号线看板。（当前总产出： {int(df['g'].sum())}）")
        #plt.draw()
        
    except:
        pass    
    finally:
        #plt.draw()
        plt.pause(60)
        print('2222222')
if __name__ == '__main__': 
    #plt.axis([0, 1000, 0, 1])
    plt.ion()
 
    while True:
        
        plot_bar()

    print('2222222')