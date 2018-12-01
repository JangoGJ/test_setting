# -*- coding: utf-8 -*-
import datetime
import time
class Num2Work:
    # 0.0 : xia ling dian
    # 1.0 : shang bai bian
    # 2.0 : shang si dian
    # 3.0 : shang ling dian
    Dictionary_WorkDay2Work={0.0:'will come back home from night work',
                             1.0:'wiil work all day',
                             2.0:'will go to work after 14:00',
                             3.0:'will go to work after 21:00'}


    Dictionary_Work2WorkTime={
        0.0:'7:00 >-< 9:30',
        1.0:'6:00 >-< 17:45',
        2.0:'14:00 >-< +2:00',
        3.0:'21:00 >-< +9:30'}



#字符串转化为日期
StateTime=datetime.datetime.strptime('2018-12-01 0:0:1', '%Y-%m-%d %H:%M:%S')
#StateTime转化为timestamp
timestamp_StateTime=time.mktime(StateTime.timetuple())
delta=86400*4
WorkDay=((time.time()-timestamp_StateTime)%delta)//86400
today=time.strftime("%Y-%m-%d %H:%M")
print('Today is {}.\nAnd father {}.\nSo, play time is {}.\n'.format(
    today,Num2Work.Dictionary_WorkDay2Work[WorkDay],Num2Work.Dictionary_Work2WorkTime[WorkDay]))
input()