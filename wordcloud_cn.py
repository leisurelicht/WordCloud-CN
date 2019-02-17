#! /usr/bin/env python
"""
中文词云
"""

import os

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 设置中文字体
font_path = os.path.join(BASE_DIR, 'simhei.ttf')

# stopword
stopword_path = os.path.join(BASE_DIR, 'stopwords.txt')

# 读入 stopword
with open(stopword_path) as f_stop:
    f_stop_text = f_stop.read()
    f_stop_seg_list = f_stop_text.splitlines()

# 读入文本内容
text = open(os.path.join(BASE_DIR, '张小龙演讲.txt')).read()

# 中文分词
seg_list = jieba.cut(text, cut_all=False)

# 把文本中的stopword剃掉
my_word_list = []

for my_word in seg_list:
    if len(my_word.strip()) > 1 and not (my_word.strip() in f_stop_seg_list):
        my_word_list.append(my_word)

my_word_str = ' '.join(my_word_list)

# 生成词云
wc = WordCloud(
    font_path=font_path,
    background_color="white",
    random_state=42,
    width=1000,
    height=860,
)
wc.generate(my_word_str)

# 生成图片
wc.to_file('./examples/张小龙演讲.png')
