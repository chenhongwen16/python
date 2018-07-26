#!/usr/bin/env python
#coding:utf-8

import matplotlib.pyplot as plt
import jieba
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from PIL import Image

abel_mask = np.array(Image.open("./kobe.jpg"))
text_from_file_with_path = open('./text.txt').read()


#通过jieba分词进行分词并通过空格分隔
wordlist_after_jieba = jieba.cut(text_from_file_with_path, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(
    background_color = 'grey',
    mask = abel_mask,
    max_words = 200,
    stopwords = STOPWORDS,
    max_font_size = 50,
    random_state = 20,
    scale=1.5).generate(wl_space_split)

#根据图片生成词云颜色
image_colors = ImageColorGenerator(abel_mask)

#For showing picture
plt.imshow(my_wordcloud)
plt.axis("on")
plt.show()