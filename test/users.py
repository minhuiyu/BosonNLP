# -*- encoding: utf-8 -*-
'''
Created on 2016年11月3日

@author: Administrator
'''
from dbmanager import dbManager2
conn = dbManager2(dbname='weibo')
sql="SELECT DISTINCT(userID)from last_useful GROUP BY userID"
list=conn.executeSelect(sql)
count=0
for i in list:
     count+=1
     print count
     countid=i[0]
     sql1="SELECT  userID,positive,posttime ,weiboID,text from last_useful WHERE userID=%s order by posttime ASC" %countid
     userlist=conn.executeSelect(sql1)
     #w1=file("F:\\ExperimentData\\lastuseful\\user_"+i[0]+".txt" ,"a+")
     for j in userlist:
         print j[0],j[1],j[2],j[3],j[4]
        # w1.write(str(j[1])+'\n')
