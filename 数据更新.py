import pymssql
import pandas as pd 
def sql_lianjie():

    conn = pymssql.connect(host="192.168.2.100",user="sa",password="123456",database="mobile")
#查询语句一    
    cur1 = conn.cursor()
    for i in range(4000):
        sql = "UPDATE dhmx SET bt='{}' ,bh='it5080静谧蓝测试',czr='mac' WHERE imei='{}' ".format(macs[i],imeis[i])
        print(sql)
        cur1.execute(sql)
    conn.commit()    
    conn.close()
df = pd.read_excel(r'D:\5080mac.xlsx')
df1 = pd.read_excel(r'D:\5080imei.xlsx')
macs = []
imeis = []
        #箱号清理、聚合
for i in list(df.columns):
	macs += list(df[i].dropna(axis=0))

for i1 in list(df1.columns):
	imeis += list(df1[i1].dropna(axis=0))

#ss = [(x,y) for x in macs for y in imeis ]


sql_lianjie()    