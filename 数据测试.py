import pandas as pd 
import os,xlrd
'''出货扫描数据与上一次数据比对'''

def hq_ktxtms(file_names,maindir):
 #获取文件名
    dflist = []
    for file_name in file_names:
        file_name = os.path.join(maindir,file_name)
    
        #print(file_name)
        try:
            excels = xlrd.open_workbook(file_name)
           
            for sheet in excels.sheets():
                print(sheet.name)
                if sheet.name == '考勤记录':

                    df = pd.read_excel(file_name,sheet.name)
                    print(df)
                    
                #dflist.append(df)
            df.to_excel(r"G:\shuju\ss.xlsx")    #df = pd.concat(dflist,axis=0)
        except:
            print('文件打开失败！请检查文件名称的正确性！\n')
            exit()

    ktxtms = []
        #箱号清理、聚合
        
        #print(df)
    for i in list(df.columns):
	    ktxtms += list(df[i].dropna(axis=0))
  

    return ktxtms 
#df = pd.DataFrame(ktxtms)   

#df.to_excel("22.xlsx",index=False)
#print(df)

if __name__ == "__main__":
    
    maindir,subdir,file_names = os.walk('G:\shuju').__next__()
    
    ktxtms_now = hq_ktxtms(file_names,maindir) if file_names else False

    #print(ktxtms_now)

           