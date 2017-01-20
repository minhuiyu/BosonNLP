# encoding: utf-8
'''
Created on 2016年10月9日

@author: Administrator
'''
from __future__ import print_function, unicode_literals
import json
import requests
import sys
from Canvas import Line


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
     reload(sys)
     sys.setdefaultencoding(default_encoding)
#SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis'
#SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis?weibo'
# 注意：在测试时请更换为您的API Token
#headers = {'X-Token': 'M4Th_Znq.9902.yv4gRv5hJhWh'}   #728019600@qq.com   GroundTruth
'''
f=open('F:\\ExperimentData\\topic1_rewb_nlp\\topic1_rewb_text15_2.txt','r')
w1=file('F:\\ExperimentData\\topic1_rewb_nlp\\topic1_rewb_text15_2_opin.txt','w')
w2=file('F:\\ExperimentData\\topic1_rewb_nlp\\topic1_rewb_text15_2_sa.txt','w')
'''
'''
f=open('F:\\ExperimentData\\topic1_comment_nlp\\topic1_comments_text7.txt','r')
w1=file('F:\\ExperimentData\\topic1_comment_nlp\\topic1_comments_text7_opin.txt','w')
w2=file('F:\\ExperimentData\\topic1_comment_nlp\\topic1_comments_text7_sa.txt','w')
'''

filepath_r='F:\\ExperimentData\\topic1_rewb_nlp\\topic1_rewb_text.txt'
w1=file('F:\\ExperimentData\\topic1_rewb_nlp\\test.txt','w')
f=open(filepath_r,'r')
result=[ ]
i=1
while 1:
     lines= f.readlines(5)
     for line in lines :
         result.append(line.split('//'))
         print(line.split('//@'))
f.close()

for item in result:  
    for j in item: 
         w1.write(j+'\n')
         print (j)         
w1.close()     

        
'''
count=0
j=14
while (j>20):
     filepath_r='F:\\ExperimentData\\topic1_comment_nlp\\topic1_comments_text'+j+'.txt'
     f=open(filepath_r,'r')
     filepath_w1='F:\\ExperimentData\\topic1_comment_nlp\\topic1_comments_text'+j+'_opin.txt'
     w1=file(filepath_w1,'w')
     filepath_w2='F:\\ExperimentData\\topic1_comment_nlp\\topic1_comments_text'+j+'_sa.txt'
     w2=file(filepath_w2,'w')
     tokenname=open('F:\\ExperimentData\\bosonnlp_token.txt','r')
     while (count<501):
         tokennum=tokenname.readline()
          if not tokennum:
                 break
         headers = {'X-Token': tokennum}
         print(tokennum)
         while 1:
             line = f.readline()
             count+=1
             if not line:
                 break
             s=[line]
             data = json.dumps(s)
             resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8')) 
             print(resp.text)
             w1.write(resp.text+'\n')
             w1.writelines(s) 
             w2.write(resp.text+'\n')
         j+=1
     tokenname.close()
w1.close()
w2.close()
f.close()
print('lllllfinishllllllll')
s = ['注意安全//@hugozhu:暴雨又来了 //@淘三多: 北京的同学们'  ]
data = json.dumps(s)
resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8'))
print(resp.text)
'''