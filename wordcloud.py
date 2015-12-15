#coding: utf-8
 
import os
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import jieba


stopwords = {}

def stopword(filename = ''):
    global stopwords
    f = open(filename, 'r')
    line = f.readline().rstrip()
    while line:
        stopwords.setdefault(line, 0)
        stopwords[line.decode('utf-8')] = 1
        line = f.readline().rstrip()
    f.close()
stopword(filename = '/Users/Fantas/Desktop/git/stopwords.txt')


# # 导入
# d = path.dirname(__file__)
# text = open(path.join(d, 'letter_one.rtf')).read().decode("gbk")
# print text


with open ('/Users/Fantas/Desktop/情书一.txt') as f:

    text = f.readlines()
    text = r' '.join(text)

    seg_generator = jieba.cut(text)

    seg_list = [i for i in seg_generator if i not in stopwords]

    seg_list = [i for i in seg_list if i != u' ']

    seg_list = r' '.join(seg_list)

# def wordcloudplot(txt):

#     wordcloud = WordCloud(font_path='/Users/Fantas/Downloads/simheittf/simhei.ttf', 

#                           background_color="black",   #可以选择black或white

#                           margin=5, width=1800, height=800,  relative_scaling=.5) # 长宽度控制清晰程度​

#     wordcloud = wordcloud.generate(txt)

#     # Open a plot of the generated image.

#     plt.imshow(wordcloud)
#     plt.axis("off")
#     plt.show()

# wordcloudplot(seg_list)
#  # 词云
# # wordcloud = WordCloud(max_font_size=40, relative_scaling=.5)
wordcloud = WordCloud(font_path='/Users/Fantas/Downloads/simheittf/git/simhei.ttf',    background_color="black",   margin=5, width=1800, height=800) 

wordcloud = wordcloud.generate(seg_list)
#画图

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


