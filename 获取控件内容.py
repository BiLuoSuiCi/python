import win32api,win32gui,win32con
import time,pythoncom

def send_box():
   
    ck = 'TRANSSION HOLDINGS [Ver: 1.0.0.2018062802]'
    ck = '发货扫描'
    #ck = '彩盒称重'
    
    hwnd = win32gui.FindWindow(None,ck)
    hwnd = win32gui.FindWindow('#32770','')
    print(hwnd)
    hwnd_1 = win32gui.FindWindowEx(hwnd, None, 'TcxGroupBox','扫描箱号')

    hwnd_2 = win32gui.FindWindowEx(hwnd_1, None, 'TGridPanel', None)
    #发货扫描
    hwnd_3 = win32gui.FindWindowEx(hwnd_2, None, 'TcxButtonEdit', None)

    #hwnd_3 = win32gui.FindWindowEx(hwnd_2, None, 'TPanel',"FAIL")

    hwnd_4 = win32gui.FindWindowEx(hwnd_3, None, 'TcxCustomInnerTextEdit', None)

    #h = win32gui.GetDlgItem(1577278, 59648)
    print(h)
    #win32gui.SetForegroundWindow(hwnd_4) #获取焦点
    #time.sleep(1)
    #win32gui.SendMessage(hwnd_3,win32con.WM_SETTEXT,None,"不好")
    return hwnd_4
def getstring(hwnd):    
    len = win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH) + 1 #获取edit控件文本长度
    #构建缓冲区
    b = win32gui.PyMakeBuffer(len)
    #获取控件文本
    a = win32gui.SendMessage(hwnd, win32con.WM_GETTEXT, len, b)
    #获取缓存区地址和存储长度
    address, a = win32gui.PyGetBufferAddressAndLen(b) 
    #获取缓冲区字符串（地址，长度）
    text = win32gui.PyGetString(address, a) 

    print(text)

h = send_box()
while True:
    if h:
        getstring(h)
    else:
        break