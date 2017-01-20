# -*- encoding: utf-8 -*-
'''
Created on 2016年10月9日

@author: Administrator
'''

from __future__ import print_function, unicode_literals
import json
import requests


KEYWORDS_URL = 'http://api.bosonnlp.com/keywords/analysis'


text = '注意安全//@hugozhu:暴雨又来了 //@淘三多: 北京的同学们'
params = {'top_k': 10}
data = json.dumps(text)
headers = {'X-Token': 'M4Th_Znq.9902.yv4gRv5hJhWh'}
resp = requests.post(KEYWORDS_URL, headers=headers, params=params, data=data.encode('utf-8'))


for weight, word in resp.json():
    print(weight, word)