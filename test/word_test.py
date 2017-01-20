# -*- coding: utf-8 -*-
'''
Created on 2016年10月21日

@author: Administrator
'''
import sys
import re
import json
import requests
from Canvas import Line
from _mysql import result
#from __future__ import print_function, unicode_literals

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
     reload(sys)
     sys.setdefaultencoding(default_encoding)
     
SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis?weibo'  
    
filepath_r='F:\\ExperimentData\\topic1_rewb_nlp\\5965_5989.txt'
w1=file('F:\\ExperimentData\\topic1_rewb_seg_nlp\\5965_5989','a+')
w2=file('F:\\ExperimentData\\topic1_rewb_seg_nlp\\5965_5989','a+')
f=open(filepath_r,'r')
strinfo=re.compile('//@......*')
count=1
tokenid=['M4Th_Znq.9902.yv4gRv5hJhWh'
          ,'0bGs1eLu.9911.MVXdu3KQ2P2j'
          ,'ouonDx-z.10033.aUxahjJzOTGO'
          ,'ARcMMACb.10037.2t0e2YRvn6cC'
          ,'KRqOmkrG.10043.yA2GmkqgeN5Z'
          ,'cVFItZRN.10045.rARuZMsDeCay'
          ,'BpvxYQof.10050.TRxkjC8ifQvh'
          ,'_fWktNtl.10051.PDjOm-JhWABX'
          ,'jMfULdKN.10052.qCO4gMChWYEO'
          ,'MzunFfGy.10054.Gow1hXSqgkVW'
          ,'BHu56kuq.10059.HsD0PHhFnbll'
          ,'uWKqyd9e.10062.iUlnr6Vkzgnd']
i=1
while 1:
     headers = {'X-Token': tokenid[0]}  
     if(count<501):
         line=f.readline()
         if not line:
             break
         result=strinfo.sub(' ' , line)
         print(result)
         w2.write(result)
         data = json.dumps(result)
         resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8')) 
         print(resp.text)
         w1.write(resp.text+'\n')
         w2.write(resp.text+'\n')
         count+=1
     if(count>=501): 
         i+=1
         count=1
     if(i>12):
         break
print('########finished')
#result=line.replace('//@','  ' )
