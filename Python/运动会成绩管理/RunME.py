import pymysql
from dbutils.persistent_db import PersistentDB
def sqlcon(code1):
    config = {
        'host': '***',##
        'port': 3306,
        'database': 'yundonghui',
        'user': 'test',   
        'password': '****',
        'charset': 'utf8'
    }
    db_pool = PersistentDB(pymysql, **config)
    # 从数据库连接池是取出一个数据库连接
    conn = db_pool.connection()
    cursor = conn.cursor()
    cursor.execute(code1)
    result = cursor.fetchall()
    cursor.connection.commit()
    conn.close()
    return result
def start():
    #主界面
    while 1:
        print('''
#########################################
#   please choose you op                #
#       1.前期编排                       #
#       2.比赛管理                       #
#       3.查询管理                       #
#      。other num to quit              #
#########################################   
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            start1()
        elif opcode==2:
            start2()
        elif opcode==3:
            start3()
        else:
            print("quit!!!   bye")
            break
def start1():#菜单1
    while 1:
        print('''
    #########################################
    #   please choose you op                #
    #       1.sport projects insert         #
    #       2.staff member insert           #
    #       3.staff position insert         #
    #       4.Athlete registration          #
    #       5.The sport game order          #
    #      。other num to quit              #
    ######################################### 
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            bianpai_dingyibisai()
        elif opcode==2:
            bianpai_gongzuorenyuan()
        elif opcode==3:
            bianpai_gongzuogangwei()
        elif opcode==4:
            bianpai_yundongyuanbaomin()
        elif opcode==5:
            bianpai_chakanzhixunce()
        else:
            print("quit!!!   bye")
            break
def start2():#菜单2
    while 1:
        print('''
    #########################################
    #   please choose you op                #
    #       1.insert a score                #
    #      。other num to quit              #
    ######################################### 
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            bisai_scoreIN()
        else:
            print("quit!!!   bye")
            break
def start3():#菜单3
    while 1:
        print('''
    #########################################
    #   please choose you op                #
    #       1.Athlete registration info     #
    #       2.sport projects info           #
    #       3.staff position info           #
    #       4.search score @ athlete'name   #
    #       5.search score @ project'name   #
    #       6.ranking of each projects      #
    #       7.High&low scores @each item    #
    #       8.sql query code                #
    #      。other num to quit              #
    ######################################### 
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            chaxun_yundongyuanpeople()
        elif opcode==2:
            chaxun_perject()
        elif opcode==3:
            chaxun_saff()
        elif opcode==4:
            chaxun_yundongyuan()
        elif opcode==5:
            chaxun_xiangmu()
        elif opcode==6:
            bisai_scoreOuT()
        elif opcode==7:
            chaxun_score_ana()
        elif opcode==8:
            chaxun_zizhu()
        else:
            print("quit!!!   bye")
            break
#前期编排$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def bianpai_dingyibisai():
    #定义比赛项目
    while 1:
        print('''
##############################
#   please choose you op     #
#       1.insert a project   #
#       2 or any num .quit   #
##############################
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            name=(input("please input project name:\n>"))
            code=(input("please input project code:\n>"))
            code1="INSERT INTO `xiangmu` (`Xname`, `XID`) VALUES ('{}', '{}');".format(name,code)
            try:
                result=sqlcon(code1)
            except:
                print("project existed")
            print("op is done!!")
        else:
            print("quit!!!")
            break
def bianpai_gongzuogangwei():
    #设置工作岗位
    while 1:
        print('''
##############################
#   please choose you op     #
#       1.insert a station   #
#       2 or any num .quit   #
##############################
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            name=(input("please input station name:\n>"))
            code=(input("please input station code:\n>"))
            code1="INSERT INTO `gongzuogongwei` (`g_name`, `g_ID`) VALUES ('{}', '{}');".format(name,code)
            try:
                result=(sqlcon(code1))
            except:
                print("project existed")
            print("op is done!!")
        else:
            print("quit!!!")
            break
def bianpai_gongzuorenyuan():
    #录入工作人员
    while 1:
        print('''
##############################
#   please choose you op     #
#       1.insert a staff     #
#       2 or any num .quit   #
##############################
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            name=(input("please input Person's name:\n>"))
            p_code=(input("please input Person's id:\n>"))
            code=(input("please input station name:\n>"))
            code1="SELECT g_ID FROM `gongzuogongwei` WHERE g_name='{}'".format(code)
            try:
                result=tuple(sqlcon(code1))[0][0]
            except:
                print("this sation is not exist")
                break
            code2="INSERT INTO `gongzuorenyuan` (`Gname`, `GID`, `g_ID`) VALUES ('{}', '{}', '{}');".format(name,p_code,result)
            result2=sqlcon(code2)
            print("op is done!!")
        else:
            print("quit!!!")
            break
def bianpai_yundongyuanbaomin():
    #运动员报名
    while 1:
        print('''
############################################
#   please choose you op                   #
#       1.Register for the competition     #
#       2 or any num .quit                 #
############################################
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            name=(input("please input person's name:\n>"))
            y_code=(input("please input person;s id:\n>"))
            code=(input("please input perject name:\n>"))
            code1="SELECT XID FROM `xiangmu` WHERE Xname='{}'".format(code)
            try:
                result=tuple(sqlcon(code1))[0][0]
            except:
                print("this perject is no exist")
                break
            code2="INSERT INTO `yundongyuan` (`Yname`, `YID`, `XID`) VALUES ('{}', '{}', '{}');".format(name,y_code,result)
            result2=sqlcon(code2)    
            print("op is done!!")
        else:
            print("quit!!!")
            break
def bianpai_chakanzhixunce():
    #查看秩序手册
    print('''
####################################################################################################################################################################
#                                                                           大会纪律                                                                                #
#                            为了顺利完成本届运动会的各项任务，充分展示我校学生风采， 杜绝意外事故的发生，特拟定运动会纪律要求如下：                                                #
#   1、全校师生必须服从大会安排，听从大会指挥，遵守大会纪律。                                                                                                               #
#                                                                                                                                                                 #
#   2、发扬顽强拼搏精神，赛出风格，赛出水平，努力为班集体争光。比赛中必须尊重裁判，服从判决。                                                                                    #
#                                                                                                                                                                 #7

#   3、贯彻“友谊第一，比赛第二”的方针，增进友谊，促进团结。严禁吵架等不文明事件发生。运动员因故请假获准，换人不换项， 如有发现冒名顶替的，取消该两名（顶替与被顶替者）运动员所有项目的所得分。   #
# 
#   4、除运动员 、裁判工作人员外，其他人未经大会同意不得到运动场内，尤其在沙包、实心球比赛时，特别要注意安全。各班必须在指定的区域休息、观看比赛。
#  
#   5、全校师生必须自始至终参加本届运动会，教师的到岗情况由校办负责考勤和检查。学生若无特殊情况，不得请假。如有请假者须由班主任上报孟主任，批准后方可离校。各班学生出勤情况，由学生会干部检查记录
# 
#   6、爱护运动场内的一切设备设施，并注意清洁卫生，违者，视其情节给予处罚或纪律处分。
#  
#   7、工作人员、裁判员请假须经校长室批准方可有效。
####################################################################################################################################################################
    ''')
#比赛管理￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
def bisai_scoreIN():
    #成绩录入
    while 1:
        print('''
############################################
#   please choose you op                   #
#       1.insert a score                   #
#       2 or any num .quit                 #
############################################
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            name=(input("please input person's name:\n>"))
            code=(input("please input perject name:\n>"))
            score=(input("please input score:\n>"))
            code1="SELECT XID FROM `xiangmu` WHERE Xname='{}'".format(code)
            try:
                result=tuple(sqlcon(code1))[0][0]
            except:
                print("this perject is not exist")
                break
            code2="SELECT YID FROM `yundongyuan` WHERE Yname='{}'".format(name)
            try:
                result2=tuple(sqlcon(code2))[0][0]
            except:
                print("this person is not exist")
                break
            code3="INSERT INTO `chengji` (`YID`, `XID`, `Score`) VALUES ('{}', '{}', '{}');".format(result2,result,score)
            result3=sqlcon(code3)
            print("op is done!!")
        else:
            print("quit!!!")
            break
def bisai_scoreOuT():
    #成绩输出
    code="SELECT yundongyuan.Yname,xiangmu.Xname,chengji.Score FROM `chengji`,yundongyuan,xiangmu WHERE chengji.YID=yundongyuan.YID and chengji.XID=xiangmu.XID ORDER by chengji.XID,chengji.Score "
    # code="SELECT * FROM `chengji`"
    result=(tuple(sqlcon(code)))
    print('''
#######################################
#   运动员      项目        成绩        #
    ''')
    for i in result:
        print("#\t{}\t{}\t\t{}\t\t#".format(i[0],i[1],i[2]))
    print('''
#######################################
    ''')
#查询功能############################################################################
def chaxun_yundongyuan():
    #查询运动员成绩
    while 1:
        print('''
############################################
#   please choose you op                   #
#       1.search a score                   #
#       2 or any num .quit                 #
############################################
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            name=(input("please input person's name:\n>"))
            code="SELECT YID FROM `yundongyuan` WHERE Yname='{}'".format(name)
            try:
                result=tuple(sqlcon(code))[0][0]
            except:
                print("this person is not exist")
                break
            code2="SELECT xiangmu.Xname,chengji.Score FROM `chengji`,xiangmu WHERE chengji.YID='{}' and chengji.XID=xiangmu.XID".format(result)
            result2=sqlcon(code2)
            print(code2)
            print('''
#######################################
#   运动员      项目        成绩        #
    ''')
            for i in result2:
                print("#\t{}\t{}\t\t{}\t\t#".format(name,i[0],i[1]))
            print('''
#######################################
                ''')
            print("op is done!!")
        else:
            print("quit!!!")
            break
def chaxun_xiangmu():
    #查询项目成绩
    while 1:
        print('''
############################################
#   please choose you op                   #
#       1.search a score                   #
#       2 or any num .quit                 #
############################################
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            name=(input("please input perject's name:\n>"))
            code="SELECT XID FROM `xiangmu` WHERE Xname='{}'".format(name)
            try:
                result=tuple(sqlcon(code))[0][0]
            except:
                print("this perject is not exist")
                break
            code2="SELECT yundongyuan.Yname,chengji.Score FROM `chengji`,yundongyuan WHERE chengji.XID='{}' and chengji.YID=yundongyuan.YID".format(result)
            result2=sqlcon(code2)
            print(code2)
            print('''
#######################################
#   运动员      项目        成绩        #
    ''')
            for i in result2:
                print("#\t{}\t{}\t\t{}\t\t#".format(i[0],name,i[1]))
            print('''
#######################################
                ''')
            print("op is done!!")
        else:
            print("quit!!!")
            break
def chaxun_saff():
    #查询工作人员
    code="SELECT gongzuorenyuan.Gname,gongzuogongwei.g_name FROM `gongzuorenyuan`,gongzuogongwei WHERE gongzuorenyuan.g_ID=gongzuogongwei.g_ID"
    result=(tuple(sqlcon(code)))
    print('''
################################
#    工作人员        职位        #
    ''')
    for i in result:
        print("#\t{}\t{}\t\t#".format(i[0],i[1]))
    print('''
#######################################
    ''')
def chaxun_score_ana():
    code="SELECT xiangmu.Xname,max(Score),MIN(Score) FROM `chengji`,xiangmu WHERE xiangmu.XID=chengji.XID GROUP by chengji.XID"
    result=(tuple(sqlcon(code)))
    print('''
############################################
#   项目         最高分        最低分        #
    ''')
    for i in result:
        print("#\t{}\t{}\t\t{}\t\t#".format(i[0],i[1],i[2]))
    print('''
######################################
    ''')
def chaxun_zizhu():
    #自助查询
    while 1:
        print('''
##############################
#   please choose you op     #
#       1.Self-help check    #
#       2 or any num .quit   #
##############################
        ''')
        opcode=int(input("please input op code:\n>"))
        if opcode==1:
            code1=(input("please input sql code:\n>"))
            try:
                result=tuple(sqlcon(code1))
            except:
                print("this code is error")
                break
            print(result)
            print("op is done!!")
        else:
            print("quit!!!")
            break
def chaxun_yundongyuanpeople():
    #查询报名表
    code="SELECT yundongyuan.Yname,xiangmu.Xname FROM xiangmu,yundongyuan WHERE yundongyuan.XID=xiangmu.XID ORDER by xiangmu.Xname,yundongyuan.Yname"
    result=tuple(sqlcon(code))
    print('''
############################################
#   运动员         报名项目                   #
    ''')
    for i in result:
        print("#\t{}\t{}\t\t\t\t#".format(i[0],i[1]))
    print('''
############################################
    ''')
def chaxun_perject():
    #查询项目表
    code="SELECT * FROM `xiangmu`"
    result=tuple(sqlcon(code))
    print('''
############################################
#   项目         项目代码                   #
    ''')
    for i in result:
        print("#\t{}\t\t{}\t\t#".format(i[0],i[1]))
    print('''
############################################
    ''')
if __name__ == "__main__":

    print('''
                    welcome to this system
        ！！admin is required to enter, please enter your name


please type you name(Default admin:hulin)
    ''')
    adminname=input('>')##只有管理员可以进入
    code="SELECT if(Gname='{}',1,0) FROM `gongzuorenyuan` WHERE g_ID='00'".format(adminname)
    result=tuple(sqlcon(code))[0][0]
    if int(result):
        print("\n\nwelcome back,{}\n".format(adminname))
        start()
    else:
        print('sorry you have no access')