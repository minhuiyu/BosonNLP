# -*- encoding: utf-8 -*-
'''
Created on 2016年10月9日

@author: Administrator
'''

from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP

# 注意：在测试时请更换为您的API Token
nlp = BosonNLP('M4Th_Znq.9902.yv4gRv5hJhWh')


def print_comments(idx, comments):
    print('=' * 50)
    print('第%d组典型意见是:' % (idx + 1))
    print(comments['opinion'])
    print('-' * 20)
    print('共包含%s份文档，意见内容和原文ID如下:' % comments['num'])
    for comment, doc_id in comments['list']:
        print(comment, doc_id)


def main():
    with open('F:\\ExperimentData\\text_comments.txt', 'rb') as f:
        docs = [line.decode('utf-8') for line in f if line]
    all_comments = nlp.comments(docs)
    sort_all_comments = sorted(all_comments, key=lambda comments: comments['num'], reverse=True)
    for idx, comments in enumerate(sort_all_comments):
        print_comments(idx, comments)


if __name__ == '__main__':
    main()