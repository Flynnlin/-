#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
import time
import datetime
import random
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
url_history= "http://xmh.sptc.cn:3000/api/a/SignUp/idx/getLoginUserTbqk" #查看历史记录链接艾
url_log = "http://xmh.sptc.cn:3000/api/loginMobileNew" #登陆链接诶
url_go = "http://xmh.sptc.cn:3000/api/a/SignUp/idx/saveMRBPA.do" #填报数据链接诶

passwd='YDX*2020post' #默认密码
tem="36.5" #默认温度

tuoguan_data=[
    #[姓名，登陆账号，密码，温度，短信开关模式，手机号码，付费日期]


    ]

def login(tuoguan_data):
    for i in tuoguan_data:
    ###########################################################################
        name = i[0]#
        xh = i[1] #
        adress = '中国四川省成!!!号'  #填报地址 
        tem = i[3]#温度
        bei ='暂无其他症状' #默认备注信息
        tz=i[4] #发送模式
        tzd=i[6] #付费日期
        phone=i[5]
        ##############################################################
        head={
            'Host': 'xmh.sptc.cn:3000',
            'Connection':'keep-alive',
            'Content-Length': '80',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'http://xmh.sptc.cn:3000',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Referer': 'http://xmh.sptc.cn:3000/mobile/?y7bRbP=qAq_rArdI6edI6edIy.1QgUF0V6DBA9rresMQ.fFWXQqqoZ',
            'Accept-Encoding':'gzip, deflate',
        }
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
        try:
            ss = requests.session()#利用session模块实现会话维持
            rr=ss.post(url_log,data=paylaod,headers=head,allow_redirects=False)#登陆
            log_mes=str(time.ctime())+"  "+name
            if "成功" in rr.text: #判断登陆状态
                log_mes+="--登陆成功"
                IamFine = ss.post(url_go,data=paylaod2,headers=head)#填报数据 
                if "填报成功" in IamFine.text:
                    log_mes+="--数据上传成功"
                else:
                    log_mes+="++数据上传失败"
                his=ss.post(url_history,data="no:''",headers=head)
                #print(his.text[0:1000])
                if name in his.text[0:1000]:
                    log_mes+="--检查当日数据记录已存在---"
                else:
                    log_mes+="++数据检查失败！！！！"
            else:
                log_mes+="++登陆失败"
        except:
            log_mes=str(time.ctime())+"++"+name+"++失败：链接失效"
        with open("/www/wwwroot/have/project/python/tuoguan_log.log","r+",encoding="gb2312") as llog:
            old = llog.read()
            llog.seek(0)
            llog.write(log_mes+"\n")
            llog.write(old)
        #判断状态
        if("+" in log_mes):#"+" in log_mes and
            status="失败"
        else:
            status="成功"
        #填报结果提醒
        if tz == 0:
            pass
        elif tz==2:
            template={
                'name':name,
                'stasus':status,
                'time':str(time.localtime().tm_mon)+"月"+str(time.localtime().tm_mday)+"日",
                }
            send_sms(template,phone,"XXXX")
        elif tz==1 and "+" in log_mes:
            template={
                'name':name,
                'stasus':status,
                'time':str(time.localtime().tm_mon)+"月"+str(time.localtime().tm_mday)+"日",
            }
            send_sms(template,phone,"XXXXX")
        time.sleep(random.randint(10,30))#休眠随机秒（10～30）
def send_sms(template,phone,mode):
    # client = AcsClient('<accessKeyId>', '<accessSecret>', 'default')
    client = AcsClient('你的key', '你的key', 'default')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    # 以上部分是公用的不变
    request.set_action_name('SendSms')
    # set_action_name 这个是选择你调用的接口的名称，如：SendSms，SendBatchSms等
    request.add_query_param('RegionId', "default")
    # 这个参数也是固定的
    
    request.add_query_param('PhoneNumbers', phone) # 发给谁
    request.add_query_param('SignName', "XXX") # 签名
    request.add_query_param('TemplateCode', mode) # 模板编号
    request.add_query_param('TemplateParam', template) # 发送验证码内容
    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))

if __name__ == '__main__':
    with open("/www/wwwroot/have/project/python/tuoguan_log.log","r+",encoding="gb2312") as slog:
        old = slog.read()
        slog.seek(0)
        slog.write("\n\n\n")
        slog.write(str(old))
    login(tuoguan_data)