import itchat
import requests
import datetime
import time,re
import os
import threading


ai=False
key = '71f28bf79c820df10d39b4074345ef8c'
itchat.auto_login(hotReload=True,enableCmdQR=1)
def tl_ai(text):
    aiurl = 'http://www.tuling123.com/openapi/api'
    data = {'key':key,
    'info':text,
    'userid':'what'}
    try:
        r = requests.post(aiurl,data=data).json()
        return r.get('text')
    except:
        return '0.0'    

#@itchat.msg_register(itchat.content.TEXT)
def pipei(sx):
    pattern = re.compile(".*?(对数据).*?")
    m = pattern.search(sx)
    return m.group(1) if m else None 


#@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
@itchat.msg_register([itchat.content.TEXT,itchat.content.ATTACHMENT],isGroupChat=True)
def w_q(msg):
    global ai
    user_id = msg['FromUserName']
    print(msg['Type'])
    #user_name = msg['']
    if msg['Type'] == 'Text':
        group_text = msg['Text']

        ml = pipei(group_text)
        #print(ml)
        print(group_text)
    elif(msg['Type'] == 'Attachment'):
        msg_content = msg['FileName']
		#msg['Text'](str(msg_content))
        print(msg_content)
    elif ml == '对数据':
        ai = True
        itchat.send('你好我是机器人小冰！',toUserName=user_id)
        print('收到命令,开始启动ai')

    elif group_text == 'bye':
        ai = False
        print('收到结束命令。Bye')
        itchat.send('机器人小冰下线了。再见！',toUserName=user_id)

    elif ai:
        ms = tl_ai(group_text)
        itchat.send(ms,toUserName=user_id)
        print('ai:%s' %ms)
         
    else:
       pass             
    #print(user_id,group_text)


if  __name__ == "__main__":
  
    itchat.run()    