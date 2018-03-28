#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk           # 导入 Tkinter 库
import Image
import ImageTk
import tkFileDialog
#导入tk模块

def selectPath():
	path_ = tkFileDialog.askopenfilename()
	path.set(path_)
	im2 = Image.open(path_)
	if im2 != None:
		im2 = ImageTk.PhotoImage(im2)
		label_pic.bm=im2
		label_pic.configure(image=im2)
		inum.delete(0,'end')

def identifyNum():
	inum.delete(0,'end')
	inum.insert(0,'1 可信度99%')

master = tk.Tk()
master.geometry('280x380+20+20')
im = Image.open('./2.bmp')
im = ImageTk.PhotoImage(im)
label_pic = tk.Label(master, image = im)
label_pic.bm = im
label_pic.place(x=5,y=0,width=280,height=280)

path = tk.StringVar()
tk.Label(master,text = "目标路径:").place(x=5, y=300, width=60, height=20)
tk.Entry(master, textvariable = path).place(x=65, y=300, width=200, height=20)
tk.Button(master, text = "路径选择", command = selectPath).place(x=5,y=320, width=60, height=20)

tk.Button(master, text = "识别数字", command = identifyNum).place(x=5,y=340, width=60, height=20)
inum = tk.Entry(master)
inum.place(x=65, y=340, width=200, height=20)

master.update_idletasks()
master.mainloop()
