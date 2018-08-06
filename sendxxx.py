import win32con,win32gui


mainhwnd = win32gui.FindWindow(None,"发货扫描")
hwnd1 = win32gui.FindWindowEx(mainhwnd,None,"TcxGroupBox","扫描箱号")

hwnd2 = win32gui.FindWindowEx(hwnd1,None,"TGridPanel",None)

hwnd3 = win32gui.FindWindowEx(hwnd2,None,"TcxButton",None)

#hwnd3 = win32gui.FindWindowEx(hwnd2,None,"TPanel","PASS")
print(hwnd3)
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