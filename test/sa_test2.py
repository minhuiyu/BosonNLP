# -*- coding: utf-8 -*-
'''
Created on 2016年10月9日

@author: Administrator
'''
from __future__ import print_function, unicode_literals
import json
import requests
from Canvas import Line


#SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis'
SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis?weibo'
# 注意：在测试时请更换为您的API Token
headers = {'X-Token': 'M4Th_Znq.9902.yv4gRv5hJhWh'}   #728019600@qq.com   GroundTruth
#headers = {'X-Token': '0bGs1eLu.9911.MVXdu3KQ2P2j'}    #851086783@qq.com   GroundTruth
#headers = {'X-Token': 'ouonDx-z.10033.aUxahjJzOTGO'}     # wisteriamhy@sina.com  GroundTruth
#headers = {'X-Token': 'ARcMMACb.10037.2t0e2YRvn6cC'}      #522724616@qq.com GroundTruth
#headers = {'X-Token': 'KRqOmkrG.10043.yA2GmkqgeN5Z'}   # emmyzhu@126.com   wisteriamhy920821
#headers = {'X-Token': 'cVFItZRN.10045.rARuZMsDeCay'}      #datasnail@163.com  mm1234
#headers = {'X-Token': 'BpvxYQof.10050.TRxkjC8ifQvh'}        #anklexiaoqiang@163.com     huo0044
#headers = {'X-Token': '_fWktNtl.10051.PDjOm-JhWABX'}     # 983496326@qq.com    983496326xz
#headers = {'X-Token': 'jMfULdKN.10052.qCO4gMChWYEO'}    #3148924737@qq.com     aixiaoyu
#headers = {'X-Token': 'MzunFfGy.10054.Gow1hXSqgkVW'}     #634212612@qq.com  wyy634212612
#headers = {'X-Token': 'BHu56kuq.10059.HsD0PHhFnbll'}    #312999282@qq.com      Quintin0818
#headers = {'X-Token': 'uWKqyd9e.10062.iUlnr6Vkzgnd'}    #1395958954@qq.com      123456

f=open('F:\\ExperimentData\\topic1_rewb_nlp_wb\\topic1_rewb_text24.txt','r')
#w1=file('F:\\ExperimentData\\topic1_rewb_nlp_wb\\topic1_rewb_text3_opin_wb.txt','w')
w2=file('F:\\ExperimentData\\topic1_rewb_nlp_wb\\topic1_rewb_text24_sa_wb.txt','w')
#w1=file('F:\\ExperimentData\\topic1_rewb_nlp_wb\\topic1_rewb_text13..._sa_wb.txt','a+')
'''
f=open('F:\\ExperimentData\\topic1_comment_nlp\\topic1_comments_text7.txt','r')
w1=file('F:\\ExperimentData\\topic1_comment_nlp\\topic1_comments_text7_opin.txt','w')
w2=file('F:\\ExperimentData\\topic1_comment_nlp\\topic1_comments_text7_sa.txt','w')
'''
while 1:
    line = f.readline()
    if not line:
         break
    s=[line]
    data = json.dumps(s)
    resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8')) 
    print(resp.text)
   # w1.write(resp.text+'\n')
   # w1.writelines(s) 
    w2.write(resp.text+'\n')
#w1.close()
f.close()
print('lllllfinishllllllll')
'''   
s = ['注意安全//@hugozhu:暴雨又来了 //@淘三多: 北京的同学们'  ]
data = json.dumps(s)
resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8'))
print(resp.text)
'''