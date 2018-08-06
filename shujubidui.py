import pandas as pd 
import os,xlrd

'''出货扫描数据与上一次数据比对'''

def hq_ktxtms(file_names,maindir):
 #获取文件名
    dflist = []

    for file_name in file_names:

        file_name = os.path.join(maindir,file_name)

        try:
            excels = xlrd.open_workbook(file_name)
           
            for sheet in excels.sheets():
                #print(sheet.name)
                df = pd.read_excel(file_name,sheet.name)
                
                dflist.append(df)

                df = pd.concat(dflist,axis=0)
        except:

            print('文件打开失败！请检查文件名称的正确性！\n')
            exit()

    ktxtms = []

    for i in list(df.columns):

	    ktxtms += list(df[i].dropna(axis=0))
        #箱号重复性验证
    if len(ktxtms) == len(set(ktxtms)):

        print('箱号正常获取',end='\r')
      

    else:

        print('箱号    重复   请   复   查   后   继续！！！！！！！！！！！！！！！！！！')

        exit()          
    #print(ktxtms)
    return ktxtms 


if __name__ == "__main__":
    
    maindir,subdir,file_names = os.walk(r'ktxtms').__next__()
    
    ktxtms_now = hq_ktxtms(file_names,maindir) if file_names else False

    print(f"最近出货批次 {max(subdir)}")

    subdir = os.path.join("ktxtms",max(subdir))

    maindir,subdir,file_names = os.walk(subdir).__next__()
    #if file_names:
        #ktxtms_old = hq_ktxtms(file_names,maindir)
    ktxtms_old = hq_ktxtms(file_names,maindir) if file_names else False

    if ktxtms_now and ktxtms_old:

        if len(set([len(str(x)) for x in ktxtms_now])) == 1:

            print(len(set([len(str(x)) for x in ktxtms_now])),end='\r')

            print('数据格式正确。开始箱号比对：',end="\r")
        else:

            print('==========》数据格式不正确。请检查修正！！') 

            exit()   
        
        i = 0

        for a in ktxtms_now:

            if a in ktxtms_old:

                i += 1

                print('出货箱号重复：{a}')

            else:
                pass
                #print('通过',end='\r')    
        if not i:

             print('箱号比对通过。请选择导出数据文件。',end='\r')            