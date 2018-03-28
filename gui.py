#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk           # 导入 Tkinter 库

master = tk.Tk()
tk.Label(master, text="明文").grid(row=5,column=0)
tk.Label(master, text="密文").grid(row=17,column=0)

tp = tk.Text(master)
ts = tk.Text(master)

i = 1
def s2pfun():
	v = tp.get(0.0, 'end')
	ts.insert('insert',v)

def p2sfun():
	global i
	tp.insert('end',str(i))
	i+=1

tp.grid(row=0, rowspan=11, column=2)
ts.grid(row=12, rowspan=11, column=2)

button1 = tk.Button(master, text='明转密', command=p2sfun)
button2 = tk.Button(master, text='密转明', command=s2pfun)

button1.grid(row=6,column=0)
button2.grid(row=18,column=0)

tk.mainloop()
