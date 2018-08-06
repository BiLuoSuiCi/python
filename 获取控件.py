import win32gui,win32con
import serial
cc = 0

hw = 0
 
def show_window_attr(hWnd):
    '''
    显示窗口的属性
    :return:
    '''
    global cc,hw
    if not hWnd:
        return
 
    #中文系统默认title是gb2312的编码
    title = win32gui.GetWindowText(hWnd)

    clsname = win32gui.GetClassName(hWnd)

    #print('窗口句柄:%s ' % (hWnd))
    #print('窗口标题:%s' % (title))
    #print('窗口类名:%s' % (clsname))
    #print('')
    if title == '工单信息':
        cc = 0

    elif(title == '电子秤'):
        #win32gui.SendMessage(hWnd,win32con.WM_SETTEXT,None,"不好,buhao")
        #print('222')
        cc = 1
    elif(cc):
        
        if clsname == 'TcxCustomInnerTextEdit':
            if cc == 2:
                #win32gui.SendMessage(hWnd,win32con.WM_SETTEXT,None,'13.22')
                hw = hWnd
            else:
                pass
            
            cc += 1
        #exit()

def show_windows(hWndList):
    for h in hWndList:
        show_window_attr(h)
 
def demo_top_windows():
    '''
    演示如何获取父窗口
    :return:
    '''
    ck = 'TRANSSION HOLDINGS [Ver: 1.0.0.2018062802]'

    hwnd = win32gui.FindWindow(None,ck)
    
    return hwnd 
   
def demo_child_windows(parent):
    '''
    演示如何列出所有的子窗口
    :return:
    '''
    if not parent:
        return
 
    hWndChildList = []
    win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd),  hWndChildList)
    show_windows(hWndChildList)
     
 
hWnd = demo_top_windows()
 
demo_child_windows(hWnd) 

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

    print(text,end='\r')


def open_qr(txt):

    if txt >= 123 and txt <= 234:
        pass

ser = serial.Serial("COM2",9600,timeout=5)

ok = bytes([160,1,1,162])
no = bytes([160,1,0,161])

while True:
    if hw:
        getstring(hw)
    else:
        break    