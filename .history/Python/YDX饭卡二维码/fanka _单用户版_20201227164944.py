import os
try:
    import requests
    import time
    import re
    import random
    import qrcode
except:
    os.system('python -m pip install Image qrcode -i https://pypi.tuna.tsinghua.edu.cn/simple')
# python3 -m pip install Image
# python3 -m pip install qrcode

import requests
import time
import re
import random
import qrcode
url_log = "http://xmh.sptc.cn:3000/api/loginMobileNew"  # 登陆链接诶
url_t2 = "http://xmh.sptc.cn:3000/oApi/yd/system/interface/load/99999001"
url_yanz = "https://ecardh5.17wanxiao.com/ecardh5/bootcallback"
url_token = 'http://xmh.sptc.cn:3000/oApi/blade-auth/oauth/token'
url_fond = "http://xmh.sptc.cn:3000/oApi/ccense/getOddFareByCardApp?MmEwMD=5LWD9RQEe4uawFWhdrihJzuV4F01Ews2sbx02e9n6fE5wTixfOkJxGRKYpXkHbVuW63JzWrkaUPDLYXxTWPv5hDujP4Jr852NksA8Gutnp45SYlazUUVl2vmovnON.T7wNX5rBxis_iTfnJesfzcI59Gp3prgvAW_e73Gp5EupHOeLCk.g9mxkWcfyoKKEJ2n64r4kkgxGxFMuXnwJdCvCa3Up7jRSDHn3SakVzeNEZPJkd.wBEaTXWIWVi2pJxu4OxKJjbeDAOMYQgLG41AwQUwl5Yszo7yt5vtwmGjYt_oTr9KEMLFtxxCZnvIWvk8auyQI5KSYi4gXQCj5WgomJkiixlgTbRmc0SQ6J6g7eu.Cxw_0PqCbQsTqVsYCCooQ&c1K5tw0w6_=4j44MyHAVXtCdswvrEuuZ0ciSFlqHGJjP2D3gsiT8mV2uSCLUQd6GUaOcK2eWK0o5A3cnQdLvfQPkjphy.1uPq5NoBWGJInmlij6C7cwArs0"


def log(payPass, userid, passwd):
    proxies = {}
    paylaod = {  # 登陆数据
        'username': userid,  # 你的登陆账号
        'password': passwd  # 你的密码
    }
    head = {
        'Host': 'xmh.sptc.cn:3000',
        'Connection': 'keep-alive',
        'Content-Length': '80',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'http://xmh.sptc.cn:3000',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': 'Basic c2FiZXI6c2FiZXJfc2VjcmV0',
    }
    paylaod2 = {  # 登陆数据
        'username': userid,  # 你的登陆账号
        'password': passwd,  # 你的密码
        'registrationId': '1507bfd3f7769b823b7',
        'tenantId': '000000'
    }
    rs = requests.session()
    true = '0'
    false = '0'
    loo = rs.post(url_log, data=paylaod, allow_redirects=False,
                  headers=head, proxies=proxies)
    print("登陆中-----"+userid)
    print(loo.text)
    token = rs.post(url_token, data=paylaod2, headers=head)
    token0 = (eval(token.text)['access_token'])
    print("获取身份token-----"+token0)
    head3 = {
        'Host': 'xmh.sptc.cn:3000',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Cache-Control': 'no-cache',
        'Blade-Auth': 'bearer '+token0,
        'Authorization': 'Basic c2FiZXI6c2FiZXJfc2VjcmV0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36',
        'tenantId': '000000',
        'Referer': 'http://xmh.sptc.cn:3000/mobile/?y7bRbP=qAcxcarjFbNjFbNjFN.1QZKhpHuk77JPpIqHMND8V90qqDL',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.9',
    }
    fond_o = rs.get(url_fond, headers=head3)
    fond = str(eval(fond_o.text).get('data').get('oddFare'))
    print("获取饭卡余额-----"+fond+"元")
    head2 = {
        'Host': 'xmh.sptc.cn:3000',
        'Accept': 'application/json, text/plain, */*',
        'Blade-Auth': 'bearer '+token0,
        'Authorization': 'Basic c2FiZXI6c2FiZXJfc2VjcmV0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36',
    }

    code_url = rs.get(url_t2, headers=head2, cookies=loo.cookies)
    # print(code_url.request.headers)
    true = '0'
    false = '0'
    # print(code_url.text)
    qcode_url = eval(code_url.text).get('data')
    print("获取二维码url-----"+qcode_url)
###################################         获取二维码链接          #############################################
    rc = requests.session()
    qcde_go = rc.get(qcode_url)
    url_redirect = "https://hub.17wanxiao.com/bsacs/redirect.action"
    flag_p = re.compile(r'flag=(.*)&time')
    sign_p = re.compile(r'sign=(.*)&')
    User_p = re.compile(r'userid=(.*)&key')
    key_p = re.compile(r'key=(.*)&sign')
    time_p = re.compile(r'time=(.*)&user')
    sign = re.findall(sign_p, qcode_url)[0]
    flag = re.findall(flag_p, qcode_url)[0]
    userid = re.findall(User_p, qcode_url)[0]
    key = re.findall(key_p, qcode_url)[0]
    Time = re.findall(time_p, qcode_url)[0]
    redict = rc.post(url_redirect, data={'userData': '{"sign":"'+sign+'","time":"'+Time+'","flag":"basicopengroup_scyd_ecardh5","userid":"' +
                                         userid+'","ecardFunc":"HB_2DCode","key":"'+key+'"}'}, allow_redirects=False, proxies=proxies)
    userinfo = eval(redict.text)
    print("获取认证信息-----")
    # print(redict.cookies)
    url_author = userinfo['url']
    head4 = {
        'host': 'open.17wanxiao.com',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006J10C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36'
    }
    auth = rc.get(url_author, allow_redirects=False, headers=head4)
    nextg = eval(str(auth.headers))
    nextg_url = (nextg['Location'])
    nextgg = rc.get(nextg_url, allow_redirects=False)
    session_p = re.compile(r'SESSION=(.*) for')
    session_check = re.findall(session_p, str(nextgg.cookies))[0]
    print('获取到会话session-----')
    paylaod3 = {
        'password': payPass,
        'deviceid': '5be345dd700364ca18e2837ff0a6b613d',
        'gotowhere': 'vcard_activate',
    }
    head3 = {
        'SESSION': session_check,
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006J10C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36'
    }
    yanz = rc.post(url_yanz, data=paylaod3, headers=head3)
    print("支付密码正确-----")
    paylaod4 = {
        'deviceid': '5be345dd700364ca18e2837ff0a6b613d',
        'gotowhere': 'vcard_pay_code'
    }
    againg0 = rc.post(url_yanz, data=paylaod4, headers=head3)
    code_number_p = re.compile(r'ode":"(.*)"},"m')
    code_number = re.findall(code_number_p, againg0.text)[0]
    print("获取到当前code-----"+code_number)
    return code_number, fond, qcode_url


def qcode_make(code):
    img = qrcode.make(code)
    print("正在将code转换为二维码-----")
    with open('paycode.png', 'wb') as f:
        img.save(f)


if __name__ == "__main__":
    print("\n\n----------\n\n")
    userid = str(input('账户id：'))
    passwd = str(input('账户密码：'))
    paypass = str(input('支付密码：'))
    while True:
        if 1:
            code, fond, url = log(paypass, userid, passwd)
            qcode_make(code)
            with open('show.html', 'w') as ta:
                payload_r = '''
    <!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="30">
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta name="viewport" content="width=device-width,user-scalable=yes,minimal-ui">
	<h1>学号：{} 余额：{}</h1> <br>
    <img src="{}.png"><br>
    <a href="{}">每分钟自动更新, 限当面使用 支付密码：{}</a>
    
            '''.format(userid, fond, 'paycode', url, paypass)
                ta.write(payload_r)
            print("输出到文件中（当前工作目录下）-----完成\n正在等待60s")
            time.sleep(60)
            print("\n\n----------\n\n")
        # except:
        #     print("\n\n----------\n\n")
        #     print('something error!!')
        #     exit(0)
