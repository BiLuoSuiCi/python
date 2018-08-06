import win32api,win32gui,win32con
import pythoncom,PyHook3

key_code = ''
BOX_list = []
mk = 0

def OnKeyboardEvent(event):

    global key_code,mk

    #print ('Window:',event.Window)
    
    
    if event.Key != "Return":
        key_code += chr(event.Ascii)
    else:
        #print(key_code)
        if key_code == '101011':
            key_code = ''
            mk = 1
            print('开始装栈板')
        elif(key_code == '101010'):
            mk = 0
            print(BOX_list)
            print('上栈板完毕，准备打印标签')   
        elif(key_code not in BOX_list and key_code !='' and mk and len(key_code) == 14):
            key_code.replace(' ','')
            BOX_list.append(key_code)
            print ('扫描数据:',key_code,mk)
        elif(mk == 0):
            BOX_list.clear()    
        #print ('WindowName:',event.WindowName)
        txt = win32gui.GetWindowText(event.Window)
        print(txt)
        print(f"已上栈板箱数： {len(BOX_list)}")
        key_code = ''

    
    return True
hooks_manager = PyHook3.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()