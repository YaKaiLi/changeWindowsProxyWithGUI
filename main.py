import winreg
import subprocess
import ctypes
from tkinter import *

'''
说明（重要）：只有以前开过代理才可以使用！！！！
            如果从来没有开过代理，有可能注册表的键不存在，会报错
'''

def get_proxy_status():
    ie_setting_reg = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        )
    proxy_status_key = winreg.QueryValueEx(ie_setting_reg ,"ProxyEnable")
    winreg.CloseKey(ie_setting_reg)
    assert type(proxy_status_key[0]) == int
    return proxy_status_key[0]

def set_key(name, value,INTERNET_SETTINGS):#修改键值
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    #print("name+value")
    #print(name)
    #print(value)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)


def turnOn():
    #启用代理
    if get_proxy_status()==0:
        try:
            ie_setting_reg = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                "Software\Microsoft\Windows\CurrentVersion\Internet Settings",
                0,
                winreg.KEY_WRITE
            )
            winreg.SetValueEx(ie_setting_reg, 'ProxyEnable', 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(ie_setting_reg, 'ProxyServer', 0, winreg.REG_SZ, '127.0.0.1:8080')
            winreg.SetValueEx(ie_setting_reg, 'ProxyOverride', 0, winreg.REG_SZ, ' ')
            winreg.CloseKey(ie_setting_reg)
            subprocess.Popen(r'c:\\Program Files\\Internet Explorer\\iexplore.exe')
        except:
            text.delete(1.0, END)
            text.insert(INSERT, "开启失败")
        else:
            text.delete(1.0, END)
            text.insert(INSERT, "开启成功")
    else:
        text.delete(1.0, END)
        text.insert(INSERT, "请勿重复开启！")

def turnOff():
    #停用代理
    if get_proxy_status()==1:
        try:
            ie_setting_reg = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                "Software\Microsoft\Windows\CurrentVersion\Internet Settings",
                0,
                winreg.KEY_WRITE
            )
            winreg.SetValueEx(ie_setting_reg, 'ProxyEnable', 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(ie_setting_reg)
            subprocess.Popen(r'c:\\Program Files\\Internet Explorer\\iexplore.exe')
        except:
            text.delete(1.0, END)
            text.insert(INSERT, "关闭失败")
        else:
            text.delete(1.0, END)
            text.insert(INSERT, "关闭成功")
    else:
        text.delete(1.0, END)
        text.insert(INSERT, "代理未开启！")


root = Tk()  # 用库中的 Tk() 方法创建主窗口，并把窗口名称赋值给 root
root.title("一键启用Windows ie代理--配合burp使用")

frame = Frame(root)
frame.pack(padx=50, pady=40)  # set area


turnOnTheProxy = Button(frame, text=" 开启 ", font=("宋体", 15), width=10, command=turnOn).grid(row=0, column=0, padx=15, pady=5)
turnOffTheProxy = Button(frame, text=" 关闭 ", font=("宋体", 15), width=10, command=turnOff).grid(row=0, column=1, padx=15,pady=5)
exitTheSoftware = Button(frame, text=" 退出软件 ", font=("宋体", 15), width=10, command=root.quit).grid(row=0, column=2, padx=15,pady=5)

text = Text(frame, width=30, height=6, font=("华康少女字体", 15))
text.grid(row=1, column=0, padx=35, pady=5, columnspan=3)

root.mainloop()