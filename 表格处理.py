import xlrd
import pymysql

def sql_cx():
    sql = '''SELECT COUNT(UPDATED_TIME)
            FROM it5625_g2803_processing 
            WHERE UPDATED_TIME like '{}%' '''.format('2018-05-24')
    connt = pymysql.connect(host='192.168.2.33',
                            user='admin',
                            password=r'zy=*986',
                            database='db_pldb',port=3306)
    #print(connt)
    cur = connt.cursor()  

    cur.execute(sql)

    r = cur.fetchall()
    cur.close()
    connt.close()
    print(r)
sql_cx()    