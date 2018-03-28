#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk           # 导入 Tkinter 库
import Image
import ImageTk
import tkFileDialog
#导入tk模块

label_pic = None
'''
def selectPath():
	path_ = tkFileDialog.askopenfilename()
	path.set(path_)
	
	global label2
	im = Image.open(path_)
	im = ImageTk.PhotoImage(im)
	label_pic.configure(image = im)
'''
master = tk.Tk()
master.geometry('280x380+30+00')
im = Image.open('./2.bmp')
im = ImageTk.PhotoImage(im)
label_pic = tk.Label(master, image = im).place(x=0,y=0,width=280,height=280)

'''
label2.grid(row = 1, column = 0)
path = tk.StringVar()

tk.Label(master,text = "目标路径:").grid(row = 0, column = 0)
tk.Entry(master, textvariable = path).grid(row = 0, column = 1)
tk.Button(master, text = "路径选择", command = selectPath).grid(row = 0, column = 2)

'''
master.mainloop()
