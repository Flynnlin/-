#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
import time
import datetime
import random


url_history= "http://61.139.70.179:3000/api/a/SignUp/idx/getLoginUserTbqk" #查看历史记录链接艾
url_log = "http://61.139.70.179:3000/api/loginMobileNew" #登陆链接诶
url_go = "http://61.139.70.179:3000/api/a/SignUp/idx/saveMRBPA.do" #填报数据链接诶

passwd='XXXXXXXX' #默认密码
tem="36" #默认温度

tuoguan_data=[
    #[姓名，登陆账号，密码，温度]
    ["","","",""],
    
    
    ]

def login(tuoguan_data):
    for i in tuoguan_data:
    ###########################################################################
        name = i[0]#
        xh = i[1] #
        adress = '某XXX街'  #填报地址 
        tem = i[3]#温度
        bei ='暂无其他症状' #默认备注信息

        ###################           构造上传数据     ###########################
        paylaod = {  #登陆数据
        'username': i[1], #你的登陆账号
        'password': i[2] #你的密码
        }
        paylaod2 = {  
            'xh': xh, 
            'name': name, 
            'lx': '1',
            'sfzh': '',
            'sjh': '',
            'sfzc': '1',
            'sfjc': '2',
            'sflr': '2',
            'xxdz': adress, #你的地址
            'cxqk': '',
            'cxdd': '',
            'cxfs': '',
            'jrjc': '2',
            'jrqk': '1',
            'frsj': '',
            'sfgl': '2',
            'glfs': '',
            'glkssj': '',
            'glyy': '',
            'sfjrrj': '2',
            'mqjzd': adress, #你的地址
            'fgfs': '',
            'sfsx': '2',
            'sxdd': '',
            'qymc': '',
            'wd': tem,
            'locationX': '',
            'locationY': '',
            'bz': bei,
            'sbjtgj': '',
            'sfjy': '2',
            'sfcdjy': '',
            'sfhx': '',
            'jysheng': '',
            'jyshi': '',
            'jyx': '',
            'jyxxdz': '',
            'jyqymc': '',
            'sfzsb': '2',
            'zsblx': '',
            'zsbxx': '',
            'sfdgsx': '2',
            'dgsheng': '',
            'dgshi': '',
            'dgx': '',
            'dgxxdz': '',
            'dgsxqymc': '',
            'dgsxfs': '',
            'dgsxcxfs': '',
            'dgzjsheng': '',
            'dgzjshi': '',
            'dgzjx': '',
            'dgzjxxdz': '',
        }
    #############################################################################
        ss = requests.session()#利用session模块实现会话维持
        rr=ss.post(url_log,data=paylaod)#登陆
        log_mes=str(time.ctime())+name#初始化日志记录
        if "成功" in rr.text: #判断登陆状态
            log_mes+="--登陆成功"
            IamFine = ss.post(url_go,data=paylaod2)#填报数据 
            if "填报成功" in IamFine.text:
                log_mes+="--数据上传成功"
            else:
                log_mes+="++数据上传失败"
            his=ss.post(url_history)
            #print(his.text[0:1000])
            if name in his.text[0:1000]:
                log_mes+="--检查当日数据记录已存在---"
            else:
                log_mes+="++数据检查失败！！！！"
        else:
            log_mes+="++登陆失败"
        with open("tuoguan_log.log","r+",encoding="gb2312") as llog:#从文件头写入新的日志记录
            old = llog.read()
            llog.seek(0)
            llog.write(log_mes+"\n")
            llog.write(old)
        time.sleep(random.randint(0,60))#休眠随机秒（0～60）后再填写下一条数据
if __name__ == '__main__':
    login(tuoguan_data)