import winreg
import ctypes
from tkinter import *

'''
说明（重要）：只有以前开过代理才可以使用！！！！
            如果从来没有开过代理，有可能注册表的键不存在，会报错
'''

global theStatus
theStatus = 0#0为未开代理，1为代理打开

def set_key(name, value,INTERNET_SETTINGS):#修改键值
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    #print("name+value")
    #print(name)
    #print(value)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)


def turnOn():
    #启用代理
    global theStatus
    if(theStatus==0):
        try:
            # 设置刷新
            INTERNET_OPTION_REFRESH = 37
            INTERNET_OPTION_SETTINGS_CHANGED = 39
            internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
            #打开handle
            INTERNET_SETTINGS_ON = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                               r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                               0, winreg.KEY_ALL_ACCESS)
            set_key('ProxyEnable', 1,INTERNET_SETTINGS_ON) #启用
            #set_key('ProxyOverride', u'*.local;<local>')  # 绕过本地
            set_key('ProxyOverride', u' ')  # 不绕过本地
            set_key('ProxyServer', u'127.0.0.1:8080',INTERNET_SETTINGS_ON)  #代理IP及端口
            internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
            internet_set_option(0,INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
            winreg.CloseKey(INTERNET_SETTINGS_ON)
        except:
            text.delete(1.0, END)
            text.insert(INSERT, "开启失败")
        else:
            theStatus = 1
            text.delete(1.0, END)
            text.insert(INSERT, "开启成功")
    else:
        text.delete(1.0, END)
        text.insert(INSERT, "请勿重复开启！")

def turnOff():
    #停用代理
    global theStatus
    if(theStatus==1):
        try:
            # 设置刷新
            INTERNET_OPTION_REFRESH = 37
            INTERNET_OPTION_SETTINGS_CHANGED = 39
            internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
            #打开handle
            INTERNET_SETTINGS_OFF = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                               r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                               0, winreg.KEY_ALL_ACCESS)
            set_key('ProxyEnable', 0, INTERNET_SETTINGS_OFF) #停用
            internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
            internet_set_option(0,INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
            winreg.CloseKey(INTERNET_SETTINGS_OFF)
        except:
            text.delete(1.0, END)
            text.insert(INSERT, "关闭失败")
        else:
            theStatus = 0
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