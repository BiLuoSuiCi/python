import tkinter #导入tkinter模块


#定义数值
w = 280					#整个界面的宽度
h = 480					#整个界面的高度
processH = 120			#存放计算过程的Label的高度
resultH = 60			#存放计算结果的Label的高度
btnWidth = 70			#按纽宽度
btnHeight = 60			#按纽高度
msfont = '微软雅黑'		#微软雅黑字体
fontSize = 20			#字体大小
btnFgColor = '#4F4F4F'	#按纽颜色
btnBorderWidth = 0.5	#按纽边框粗细


#面板设置
root = tkinter.Tk()
root.minsize(w,h)						#面板大小的最小值
root.title('海天一树的计算器')			#面板的标题

process = tkinter.StringVar()           #字符串用于存放计算过程，初始状态为空
process.set('')
result = tkinter.StringVar()			#字符串用于存放计算结果，初始状态为0
result.set(0)                           

#labelProcess用于显示计算过程，labelResult用于显示计算结果
labelProcess = tkinter.Label(root,font = (msfont,fontSize),bg = '#EEE9E9',bd ='9',fg = '#828282',anchor = 'se',textvariable = process)
labelProcess.place(width = w,height = processH)
labelResult = tkinter.Label(root,font = (msfont,30),bg = '#EEE9E9',bd ='9',fg = 'black',anchor = 'se',textvariable = result)
labelResult.place(y = processH,width = w,height = resultH)

#数字按键
btn7 = tkinter.Button(root,text = '7',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('7'))
btn7.place(x = 0,y = processH + resultH + btnHeight,width = btnWidth,height = btnHeight)
btn8 = tkinter.Button(root,text = '8',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('8'))
btn8.place(x = btnWidth,y = processH + resultH + btnHeight,width = btnWidth,height = btnHeight)
btn9 = tkinter.Button(root,text = '9',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('9'))
btn9.place(x = 2 * btnWidth,y = processH + resultH + btnHeight,width = btnWidth,height = btnHeight)

btn4 = tkinter.Button(root,text = '4',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('4'))
btn4.place(x = 0,y = processH + resultH + 2 * btnHeight,width = btnWidth,height = btnHeight)
btn5 = tkinter.Button(root,text = '5',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('5'))
btn5.place(x = btnWidth,y = processH + resultH + 2 * btnHeight,width = btnWidth,height = btnHeight)
btn6 = tkinter.Button(root,text = '6',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('6'))
btn6.place(x = 2 * btnWidth,y = processH + resultH + 2 * btnHeight,width = btnWidth,height = btnHeight)

btn1 = tkinter.Button(root,text = '1',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('1'))
btn1.place(x = 0,y = processH + resultH + 3 * btnHeight,width = btnWidth,height = btnHeight)
btn2 = tkinter.Button(root,text = '2',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('2'))
btn2.place(x = btnWidth,y = processH + resultH + 3 * btnHeight,width = btnWidth,height = btnHeight)
btn3 = tkinter.Button(root,text = '3',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('3'))
btn3.place(x = 2 * btnWidth,y = processH + resultH + 3 * btnHeight,width = btnWidth,height = btnHeight)
btn0 = tkinter.Button(root,text = '0',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda : clickNum('0'))
btn0.place(x = btnWidth,y = processH + resultH + 4 * btnHeight,width = btnWidth,height = btnHeight)

#运算符号按键
btnac = tkinter.Button(root,text = 'AC',bd = btnBorderWidth,font = ('黑体',fontSize),fg = 'orange',command = lambda :clickSign('AC'))
btnac.place(x = 0,y = processH + resultH,width = btnWidth,height = btnHeight)
btnback = tkinter.Button(root,text = '←',font = (msfont,fontSize),fg = btnFgColor,bd = btnBorderWidth,command = lambda:clickSign('b'))
btnback.place(x = btnWidth,y = processH + resultH,width = btnWidth,height = btnHeight)
btndiv = tkinter.Button(root,text = '÷',font = (msfont,fontSize),fg = btnFgColor,bd = btnBorderWidth,command = lambda:clickSign('/'))
btndiv.place(x = 2 * btnWidth,y = processH + resultH,width = btnWidth,height = btnHeight)
btnmul = tkinter.Button(root,text ='×',font = (msfont,fontSize),fg = btnFgColor,bd = btnBorderWidth,command = lambda:clickSign('*'))
btnmul.place(x = 3 * btnWidth,y = processH + resultH,width = btnWidth,height = btnHeight)
btnsub = tkinter.Button(root,text = '-',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda:clickSign('-'))
btnsub.place(x = 3 * btnWidth,y = processH + resultH + btnHeight,width = btnWidth,height = btnHeight)
btnadd = tkinter.Button(root,text = '+',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda:clickSign('+'))
btnadd.place(x = 3 * btnWidth,y = processH + resultH + 2 * btnHeight,width = btnWidth,height = btnHeight)
btnequ = tkinter.Button(root,text = '=',bg = 'orange',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda :clickEqual())
btnequ.place(x = 3 * btnWidth,y = processH + resultH + 3 * btnHeight,width = btnWidth,height = 2 * btnHeight)
btnper = tkinter.Button(root,text = '%',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda:clickPer())
btnper.place(x = 0,y = processH + resultH + 4 * btnHeight,width = btnWidth,height = btnHeight)
btnpoint = tkinter.Button(root,text = '.',font = (msfont,fontSize),fg = (btnFgColor),bd = btnBorderWidth,command = lambda:clickNum('.'))
btnpoint.place(x = 2 * btnWidth,y = processH + resultH + 4 * btnHeight,width = btnWidth,height = btnHeight)


#点击数字
lists = []                     		#数组，保存数字和运算符
isSignClicked = False              	#是否点击了符号按纽
isEqualClicked = False				#是否点击了等号按纽

def clickNum(num):                   
    global isSignClicked			#将isSignClicked变量设为全局变量
    global isEqualClicked
	
    if True == isSignClicked:               	
        result.set(0)				#如果上次按过运算符，那么这次要把原先的数字清空，否则会加在上次那个数的末尾
        isSignClicked = False

    if True == isEqualClicked:
        result.set(0)
        isEqualClicked = False
	
    #判断界面的数字是否为0
    oldnum = result.get()      
    if '0' == oldnum:              	#如果界面上数字为0 则获取按下的数字
        if '.' == num:
            num = '0.'
        result.set(num)
    else:
        if '.' in oldnum and '.' == num:  #如果之前已经输入过'.'，那么再输入'.'不会有反应
	        pass 
        else:	
            newnum = oldnum + num
            result.set(newnum)         	#将按下的数字写到面板中


#点击运算符号（等号除外）
def clickSign(sign):
    global lists
    global isSignClicked
	
    num = result.get()              #获取界面数字
    if 0 == num.find('='):			#在连续计算时，若得到的是“=15”，要去掉等号，取其数字
        num = num[1:len(num)]
    lists.append(num)               #将界面获取的数字保存列表中

    lists.append(sign)              #将运算符号保存到列表中
    isSignClicked = True

    if 'AC' ==  sign:              	#如果按下的是'AC'按键，则清空列表内容，并将屏幕上的数字设置为默认值0
        lists.clear()
        process.set('')
        result.set(0)
    if 'b' ==  sign:              	#如果按下的是退格按纽，则选取当前数字第一位到倒数第二位
        a = num[0:-1]
        lists.clear()
        result.set(a)
        if 0 == len(a):				#如果是最后一个数，退格后变成0
            result.set(0)

			
#求百分值
def clickPer():
    curval = result.get()
    lists.append(curval)
    lists.append('/')
    lists.append('100')
	
    res = ''.join(lists)
    res = eval(res)
    result.set(res)
	
    lists.clear()
        

#获取运算结果
def clickEqual():
    global lists
    global isEqualClicked

    isEqualClicked = True
    curval = result.get()           #将界面上的数字添加到列表中
	# 2*=4, 4*=16, 16*=256, 如果按了*=之前，有等号的话，要把等号去掉
    if True == isSignClicked and 0 == curval.find('='): 
        curval = curval[1:len(curval)]
    lists.append(curval)

    proc = ''.join(lists)     		#将列表内容用join命令将字符串链接起来
    res = eval(proc)       			#用eval命令运算字符串中的内容
    res = '='+str(res)              #给运算结果前添加一个 ‘=’ 显示 
    res = res[0:10]                 #所有的运算结果取9位数
    
    process.set(proc)         		#显示运算过程
    result.set(res)                 #显示运算结果

    lists.clear()                   #清空lists数组中的内容

	
root.mainloop()
