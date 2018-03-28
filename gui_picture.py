#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk           # 导入 Tkinter 库
import Image
import ImageTk
#导入tk模块
master = tk.Tk()
#初始化Tk
master.title('label test')
#标题显示为label test
label = tk.Label(master, text = 'this is my first label')
#创建一个label，它属于top窗口，文本显示内容为.....
label.pack()

im = Image.open('./2.bmp')
im = ImageTk.PhotoImage(im)
label2 = tk.Label(master, image = im)
label2.pack()
tk.mainloop()
