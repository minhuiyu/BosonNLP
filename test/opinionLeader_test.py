# -*- coding: utf-8 -*-
'''
Created on 2016年10月9日

@author: Administrator
'''
import os
from bosonnlp import BosonNLP
nlp = BosonNLP(os.environ[' BOSON_API_TOKEN '])
nlp.comments(['今天天气好', '今天天气好', '今天天气不错', '点点楼头细雨','重重江外平湖', '当年戏马会东徐', '今日凄凉南浦'] * 2)