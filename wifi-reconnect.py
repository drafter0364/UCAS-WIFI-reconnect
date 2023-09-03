# -*- coding: utf-8 / GBK -*-
'''
重连WiFi
'''
import subprocess
import time
import os
from time import strftime, localtime

ssid = "UCAS"
# 可设置为自己需要连接的WiFi名称


def reconnect():
    '''
    重连
    '''
    print("%s 正在重连WiFi" % strftime("%Y-%m-%d %H:%M:%S", localtime()))
    os.system("netsh wlan disconnect")
    os.system("netsh wlan connect ssid=%s name=%s" % (ssid, ssid))


def check_wifi():
    subp = subprocess.Popen("ping baidu.com", stdout=subprocess.PIPE)
    print("%s " % strftime("%Y-%m-%d %H:%M:%S", localtime()))
    while subp.poll() is None:
        text = str(subp.stdout.readline(), encoding='GBK')
        print(" %s" % text)
        if match(text):
            reconnect()
            break
       


def match(text):
    '''
    匹配
    '''
    # 如果匹配到"请求超时"或者"找不到"就认为是没网了 可根据自己电脑系统语言更改匹配规则
    if text:
        if text.find('请求超时') >= 0 or text.find('找不到') >= 0:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    while True:
        check_wifi()
        time.sleep(20)
        #此处设置检测周期为20s, 可根据个人记场景需要进行配置 

