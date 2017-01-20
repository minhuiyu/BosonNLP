# -*- encoding: utf-8 -*-
'''
Created on 2016年11月3日

@author: Administrator
'''
import MySQLdb
from twisted.python.formmethod import Password
from nltk.sem.chat80 import sql_demo
import sys 
import MySQLdb 
import re
from _mysql import result
reload(sys) 
sys.setdefaultencoding('utf-8') 

from dbmanager import dbManager2
conn = dbManager2(dbname='weibo')

sql="SELECT countID,posttime from last_useful WHERE posttime like '%/0%/%'"
list=conn.executeSelect(sql)
for i in list:
     countid=i[0]
     str=i[1]
     result=str.replace('/0', '/')
     sql1= "update last_useful set posttime='%s' where countID=%d" %(result,countid)
     conn.execute(sql1)
     print countid,result

