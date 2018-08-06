
import win32com.client as com


###############################################################################################################
                                                  
with open('plan.txt','r') as p:                                                                               
    s = p.read()

print(s)

bo = int(s)  
print(s[2:10])

#实例化标签
w = com.DispatchEx('bartender.Application')
#模板是否可见
w.Visible = 1   

btformat = w.formats.open(r'D:\传音资料\模板\海运卡通箱标.btw',True,'')
################################################################################################################

def printer(plan,boxs):
    #输入栈板号
    btformat.setnamedsubstringvalue('W',plan)
    #输入箱号
    btformat.setnamedsubstringvalue('BOX_NO',boxs)
    #输入栈板信息1
    #btformat.setnamedsubstringvalue('TEXT',txt)
    #输入栈板信息2
    #btformat.setnamedsubstringvalue('BOXS',boxtxt)

    #btformat.printout(False,False)
    #关闭标签模板。1为保存，0为不保存（True=1，False=0）。
    #btformat.close(1) 

def df_zl(w):
 
    global bo

    bo += 1

    #bo = 
    
    if bo == 46021807150082:
        exit()

    box_n = str(bo)

    printer(w,box_n)

    with open('plan.txt','w') as s:
        s.write(box_n)


if __name__ == "__main__":
    
    while True:

        s = input('输入重量：')

        s = float(s)

        if s:
            df_zl('%.2f' % s)

    w.quit(1)
    print('结束老雷')