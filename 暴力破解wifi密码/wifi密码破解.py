import pywifi
from pywifi import const

class password(pywifi.PyWiFi):
    #检查当前wifi
    def __init__(self):
        self.wifi = pywifi.PyWiFi()

    def gic(self):
        #创建类的实例

        #得到当前网卡
        self.networkcard = self.wifi.interfaces()[0]
        #网卡名字
        # print(self.networkcard.name())
        #当前链接状态 0  未连接 4 已连接
        # print(self.networkcard.status())
        if self.networkcard.status() == 4:
            print('wifi已连接')
        else:
            print('wifi未连接')
    #扫描附近wifi
    def scanning(self):
        self.networkcard.scan()
        wifi_list = self.networkcard.scan_results()
        print(wifi_list)


if __name__ == '__main__':
    password = password()
    password.gic()
    password.scanning()