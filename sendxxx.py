import win32con,win32gui,time


mainhwnd = win32gui.FindWindow(None,"Config Dialog 20180322")

hwnd1 = win32gui.FindWindowEx(mainhwnd,None,"SysTabControl32",None)
print(mainhwnd,hwnd1)
hwnd2 = win32gui.FindWindowEx(hwnd1,None,"TGridPanel",None)

hwnd3 = win32gui.FindWindowEx(hwnd2,None,"TcxButton",None)

win32gui.SendMessage(12388261,win32con.WM_COMMAND,10000,None)

h = win32gui.GetMenu(657646)
#获取子菜单句柄(菜单句柄,子菜单索引)
h1 = win32gui.GetSubMenu(h,4)
#获取子菜单项标识符
menid = win32gui.GetMenuItemID(h1,8)
#发送开启命令(主窗口句柄,消息类型,菜单项标识,0)
#win32gui.PostMessage(657646,win32con.WM_COMMAND,menid,0)
#win32gui.SendMessage(h1, win32con.WM_LBUTTONDOWN, 0, 0)
hwndlist = []

win32gui.EnumChildWindows(hwnd1,lambda hwnd,p:p.append(hwnd),hwndlist)

#使选项夹获取焦点
#win32gui.SendMessage(hwnd1,4912,1,None)
#SendMessage(hTab,TCM_SETCURFOCUS,1,0)
#SendMessage(hTab,TCM_SETCURSEL,2,0)
#消息值4912 是用在 选择夹 上的。
#消息值4876 是用在 高级选择夹的
#win32gui.SendMessage(hwnd1,4876,1,None)

#win32gui.SendMessage(hwnd1,4912,1,None)
#向窗口发送左键按下。不然，选项内容不跟随刷新。
#win32gui.SendMessage(hwnd1, win32con.WM_LBUTTONDOWN, 0, 0)

#获取控件句柄
xmhwnd = win32gui.GetDlgItem(hwndlist[309],5000)
gdhwnd = win32gui.GetDlgItem(hwndlist[309],5006)
#改变控件内容
win32gui.SendMessage(xmhwnd, win32con.WM_SETTEXT, 0, "1212121")
win32gui.SendMessage(gdhwnd, win32con.WM_SETTEXT, 0, "1212121")
win32gui.SendMessage(xmhwnd, win32con.EM_SETREADONLY,0,0 )
#win32gui.UpdateWindow(mainhwnd)
print(hex(hwndlist[0]))
print(hex(hwndlist[12]))
print(hex(hwndlist[90]))
print(hex(hwndlist[202]))
print(hex(hwndlist[231]))
print(hex(hwndlist[283]))
print(hex(hwndlist[309]))

#win32gui.SendMessage(h1, win32con.WM_LBUTTONUP, 0, 0)
#win32gui.CheckMenuItem(2,win32con.MF_BYCOMMAND,2)
#hwnd3 = win32gui.FindWindowEx(hwnd2,None,"TPanel","PASS")
#print(h1,menid)
if not hwnd3:

    hwnd3 = win32gui.FindWindowEx(hwnd2,None,"TPanel","FAIL") 
    #根据控件ID获取句柄（控ID固定的窗口）   
    #hwnd3 = win32gui.GetDlgItem(hwnd2,659556)
else:
    pass
if hwnd3:
    print(hwnd3)
    #更改控件内容
    win32gui.SendMessage(hwnd3,win32con.WM_SETTEXT,None,'5000')
    #设置更新区域
    win32gui.InvalidateRect(hwnd3,None,True)
    #立即更新窗口
    win32gui.UpdateWindow(hwnd3)