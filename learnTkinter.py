#! /usr/bin/python3.5
from tkinter import *

root = Tk()  # 用库中的 Tk() 方法创建主窗口，并把窗口名称赋值给 root
root.title("The title of this window ")


def show():
    text.delete(1.0, END)
    text.insert(INSERT, "作品：")
    text.insert(INSERT, "\n作者：")


frame = Frame(root)
frame.pack(padx=50, pady=40)  # set area


turnOnTheProxy = Button(frame, text=" 开启 ", font=("宋体", 15), width=10, command=show).grid(row=0, column=0, padx=15, pady=5)
turnOffTheProxy = Button(frame, text=" 关闭 ", font=("宋体", 15), width=10, command=root.quit).grid(row=0, column=1, padx=15,pady=5)
exitTheSoftware = Button(frame, text=" 退出软件 ", font=("宋体", 15), width=10, command=root.quit).grid(row=0, column=2, padx=15,pady=5)
# self.hi_there.pack()

text = Text(frame, width=30, height=6, font=("华康少女字体", 15))
text.grid(row=1, column=0, padx=35, pady=5, columnspan=3)

root.mainloop()
