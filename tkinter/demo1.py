#!/usr/bin/python3
# coding: utf-8

# from tkinter import *

# top = Tk()
# # 进入消息循环



 
# B = Button(top, text ="点我", command = helloCallBack)
# B.pack()
# B = Button(top, text ="点我", command = helloCallBack)
# B.pack()
# B = Button(top, text ="点我", command = helloCallBack)
# B.pack()
# B = Button(top, text ="点我", command = helloCallBack)
# B.pack()
# button1=Button(top,text="Zoom in")
# button1.grid(row=2,column=2)
# button2=Button(top,text="Zoom out")
# button2.grid(row=2,column=3)
# top.mainloop()

from tkinter import *



tk=Tk()
# var=IntVar()


# def helloCallBack(btn):
#     print(type(btn))
#     # btn.bind()
#     btn.flash()
# #标签控件，显示文本和位图，展示在第一行
# Label(tk,text="First").grid(row=0,sticky=E)#靠右
# Label(tk,text="Second").grid(row=1,sticky=W)#第二行，靠左

# #输入控件
# Entry(tk).grid(row=0,column=1,padx=10,pady=10)
# Entry(tk).grid(row=1,column=1)

# #多选框插件
# button=Checkbutton(tk,text="Precerve aspect",variable=var)
# button.grid(row=2,columnspan=2,sticky=W)


#按钮控件

# button1=Button(tk,text="Zoom in",command=helloCallBack(button1), bg='gray')

def btn1_change_btn1(event):
    '''方式一：通过事件控制自己'''
    print(event.widget['state'])
    print(event.widget['text'])
    if event.widget['state'] == 'normal':
        event.widget['state'] = 'disabled'
        event.widget['bg'] = "gray"
        print("dis")
    # elif event.widget['bg'] == 'disabled':
    else:
        event.widget['state'] = 'disabled'
        event.widget['bg'] = "white"
        print("normal")
        pass

class Program:
    def __init__(self, tk):
        self.b = Button(tk, text="click me", command=self.callback)
        self.b.grid(row=2,column=6)

    def callback(self):
        print("button!!!")
        self.b.config(bg="read")
        self.b.flash()

# button1=Button(tk,text="Zoom in", bg='gray')
button1=Button(tk,text="Zoom in")
button1.bind("<Button-1>", btn1_change_btn1)  
button1.grid(row=2,column=2)

button2=Button(tk,text="Zoom out", bg='red')
button2.grid(row=2,column=3)
button3=Button(tk,text="Zoom out")
button3.grid(row=2,column=4)

# s = Program(tk)


#主事件循环
mainloop()