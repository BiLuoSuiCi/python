import win32con,win32gui
import re,time,shutil,os
import pandas as pd 
import pymysql

'''TPS工具配置批量化生成'''
#定义控件ID。软件变更便于修改。

PSN_ID = 5009

SIM_SLOT_ID = 5100

SCAN_IMEI_ID = 5102

PROJECT_NAME_ID  = 5000

WORK_ORDER_ID = 5006

MODEM_DB_ID = 5000

AP_DB_ID  = 5001

CHECK_BP_VERSION_ID  = 5020

BP_T= "BPLGUInfoCustomAppSrcP_MT6261_S00_"
#定义配置选项夹各子项，在遍历句柄列表中的位置
CUSTOMER_index = 309
PLATFORM_SET_index = 283
TEST_ITEMS_index = 231
CALFT_index = 202
ATA_index = 90
SPRD_CALIFLAG_index = 12
COUPLING_TEST_index = 0
#定义遍历窗口得来的句柄列表
#Hwnd_list = []
#设置窗口名称
Wname = "Config Dialog 20180322"
#主窗口名称正则匹配表达式
mname = ".*?- TPSTester"

tpsxml = "TPSConfig.xml"

tpsxml_path = "C:\\Program Files (x86)\\TPSTester_Release_V1.1804.27.15\\Release\\ConfigDlg"

def demo_top_windows():
    '''
    演示如何列出所有的顶级窗口
    :return:
    '''
    hWndList = []

    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
 
    return hWndList

def get_windows():
    '''匹配目标窗口标题。成功，返回窗口句柄。'''
    #获取所有顶层窗口句柄
    hWndList = demo_top_windows()

    for h in hWndList:

        if h:
            #获取窗口标题
            title = win32gui.GetWindowText(h)
            #获取窗口类名
            #clsname = win32gui.GetClassName(h)
            #匹配目标窗口
            jie_guo = re.search(mname,title)
            #获取目标句柄
            uhwnd = h if jie_guo else None
            #跳出循环
            if jie_guo: break
            
    return uhwnd

def get_menuhwnd(hw):
    '''获取窗口菜单。打开目标子菜单'''
    h = win32gui.GetMenu(hw)
    #获取子菜单句柄(菜单句柄,子菜单索引)
    h1 = win32gui.GetSubMenu(h,4)
    #获取子菜单项标识符
    menuid = win32gui.GetMenuItemID(h1,8)
    #发送开启命令(主窗口句柄,消息类型,菜单项标识,0)
    win32gui.PostMessage(hw,win32con.WM_COMMAND,menuid,0)

def set_x(hwnd):
    '''获取选项夹所有句柄'''

    hwndlist = []
    #枚举所有子窗口（控件）句柄
    win32gui.EnumChildWindows(hwnd,lambda hwnd,p:p.append(hwnd),hwndlist)
    #print(hwndlist)
    return hwndlist[CUSTOMER_index],hwndlist[PLATFORM_SET_index],hwndlist[TEST_ITEMS_index]

def get_hwnd():
    '''获取配置窗口的句柄。(配置窗口句柄>选择夹句柄)'''
    mainhwnd = win32gui.FindWindow(None,Wname)
    #获取OK按钮句柄
    hwnd1 = win32gui.FindWindowEx(mainhwnd,None,"Button","OK")
    #获取选择夹控件句柄
    hwnd2 = win32gui.FindWindowEx(mainhwnd,None,"SysTabControl32",None)

    if mainhwnd:
        return hwnd1,hwnd2
    else:
        return None,None    

def set_txt(x,x1,x2,x3,txts):
    '''发送消息修改配置文件'''
    if txts[2] in ['it5080','it5625']:
        bp_path1 = ''
        bp_path2 = ''
    else:    
        bp_path1 = os.sep.join([tpsxml_path,txts[6],BP_T + txts[5].upper()])
        bp_path2 = os.sep.join([tpsxml_path,txts[6],"VIVA"])

    psn_hwnd = win32gui.GetDlgItem(x1,PSN_ID)

    sim_hwnd = win32gui.GetDlgItem(x1,SIM_SLOT_ID)

    imei_hwnd = win32gui.GetDlgItem(x1,SCAN_IMEI_ID)

    xm_hwnd = win32gui.GetDlgItem(x1,PROJECT_NAME_ID)

    gd_hwnd = win32gui.GetDlgItem(x1,WORK_ORDER_ID)

    bp_hwnd = win32gui.GetDlgItem(x2,MODEM_DB_ID)

    bpv_hwnd = win32gui.GetDlgItem(x2,AP_DB_ID)

    ver_hwnd = win32gui.GetDlgItem(x3,CHECK_BP_VERSION_ID)

    #改变控件内容
    win32gui.SendMessage(psn_hwnd,win32con.WM_SETTEXT,0,txts[4])
    #改变下拉框内容（控件句柄，消息，下拉框内容索引，0）
    win32gui.SendMessage(sim_hwnd, win32con.CB_SETCURSEL, txts[1], 0)
    
    win32gui.SendMessage(imei_hwnd, win32con.CB_SETCURSEL, txts[1]-1, 0)
    #改变编辑框内容
    #修改项目名称
    win32gui.SendMessage(xm_hwnd, win32con.WM_SETTEXT, 0, txts[3])
    #修改工单号
    win32gui.SendMessage(gd_hwnd, win32con.WM_SETTEXT, 0, txts[0])
    #使编辑框可编辑
    #win32gui.SendMessage(sim_hwnd, win32con.EM_SETREADONLY,0,0 )
    #修改bp文件路径
    win32gui.SendMessage(bp_hwnd, win32con.WM_SETTEXT, 0, bp_path1)
    #修改bp文件路径2
    win32gui.SendMessage(bpv_hwnd, win32con.WM_SETTEXT, 0, bp_path2)

    #win32gui.SendMessage(bpv_hwnd, win32con.EM_SETREADONLY,0,0 )
    #修改版本号
    win32gui.SendMessage(ver_hwnd, win32con.WM_SETTEXT, 0, txts[5])

    #win32gui.SendMessage(ver_hwnd, win32con.EM_SETREADONLY,0,0 )
    time.sleep(0.5)

    win32gui.SendMessage(x, win32con.BM_CLICK,0, 0)

    print(x)

def get_order():
    '''获取工单信息'''

    sql = '''SELECT work_orders.Work_Order,
           work_orders.Model_Code,
           Project_Name,
           work_orders.PSN,
           work_orders.Version_Info 
           FROM work_orders,project 
           WHERE Work_Orders.Project_ID=project.Project_ID AND 
           work_orders.FSTATUS='13030010' AND 
           work_orders.order_nature='2' '''

    conn = pymysql.connect(host="192.168.2.33",user="admin",password="zy=*986",database="db_pldb",charset="utf8")

    df = pd.read_sql(sql,conn)

    conn.close()

    return df

def set_xml(msg):
    '''判断配置窗口是否开启'''
    h = get_windows()
    print(h)
    if h:
        mh,xxjhwnd = get_hwnd()
        if xxjhwnd:
            pass
        else:
            get_menuhwnd(h) 
            time.sleep(1)
            mh,xxjhwnd = get_hwnd()

        gd_hwnd,bp_hwnd,ver_hwnd = set_x(xxjhwnd)

        set_txt(mh,gd_hwnd,bp_hwnd,ver_hwnd,msg)            
    else:
        print('TPS工具未启动') 



if __name__ == "__main__":

    #print(gd_hwnd,bp_hwnd,ver_hwnd)
    
    df = get_order()
    df.insert(1,'SIM',2)
    
    df.insert(6,'xml',df['Version_Info'] + "\\" + df['Work_Order'] )

    df.loc[(df['Model_Code'] == 'it5080') | (df['Model_Code'] == 'it5625'),'SIM'] = 3

    for i in df.values:

        msgtxt = list(i)
        
        aa = os.sep.join([tpsxml_path,tpsxml])
        ab = os.sep.join([tpsxml_path,msgtxt[6]])
        bb = os.sep.join([tpsxml_path,msgtxt[6],tpsxml])

        if not os.path.exists(bb):
            set_xml(msgtxt)
            print(list(i))
            try:
                os.makedirs(ab)
                shutil.copyfile(aa,bb)
            except:
                print("文件复制失败")
        else: 
            print("文件已存在")       
            continue
            

        time.sleep(3)
