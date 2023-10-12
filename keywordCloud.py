# -*- coding: utf-8 -*-
# @Time : 2023/5/24 15:18
# @Author : niki
import jieba
import jieba.analyse
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_excel('../data.xlsx')
# 获取内容列数据
content_data = df['content']

#获取停用词
def get_stopwords():
    stop_words = []
    with open('./stopword.txt', 'r', encoding='gbk') as f:
          stop_words = [line.strip() for line in f.readlines()]
    return stop_words
stopwords = get_stopwords()
# 去停用词
content_data = content_data.apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stopwords]))


# 设置关键词提取参数
top_k = 20  # 获取前n个关键词
# allow_pos = ('n', 'nr', 'ns', 'nt', 'nz', 'vn', 'v')  # 限定词性，如名词、动词等

# 关键词提取
keywords = []
for content in content_data:
    # 使用jieba.analyse.extract_tags进行关键词提取
    tags = jieba.analyse.extract_tags(content, topK=top_k)
    keywords.append(tags)

# 将关键词结果添加到DataFrame中
df['keywords'] = keywords

# # 将关键词列表转换为以空格分隔的字符串
# keyword_text = ' '.join(str(keyword) for keyword in keywords)
filename_li=df['id']
for i in range(len(keywords)):
        keyword_text = ' '.join(str(keyword) for keyword in keywords[i])
        filename = filename_li[i]
        # 生成词云图'
        wordcloud = WordCloud(background_color='white',font_path='./simhei.ttf').generate(keyword_text)
        # 显示词云图
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        # plt.show()
        plt.savefig(f'./cloudPic/{filename}词云图.jpg')
        print(f'{filename}词云图,保存成功!')
