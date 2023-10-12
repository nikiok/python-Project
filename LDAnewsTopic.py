# -*- coding: utf-8 -*-
# @Time : 2023/5/24 16:39
# @Author : niki

import pandas as pd
import jieba
from gensim import corpora, models
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('../data.xlsx')

# 获取内容列数据
content_data = df['content']

# 停用词列表，根据实际情况进行添加
def get_stopwords():
    stop_words = []
    with open('./stopword.txt', 'r', encoding='gbk') as f:
          stop_words = [line.strip() for line in f.readlines()]
    return stop_words
stopwords = get_stopwords()

# 分词和去除停用词
corpus = []
for content in content_data:
    words = [word for word in jieba.cut(content) if word not in stopwords]
    corpus.append(words)

# 构建词典和文档-词频矩阵
dictionary = corpora.Dictionary(corpus)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in corpus]

# LDA主题建模
num_topics = 10  # 主题数量
lda_model = models.LdaModel(doc_term_matrix, num_topics=num_topics, id2word=dictionary)

# 提取主题词
topic_keywords = []
for i in range(num_topics):
    topic_words = [word for word, _ in lda_model.show_topic(i)]
    topic_keywords.append(topic_words)

# 生成主题词云
for i in range(num_topics):
    topic_text = ' '.join(topic_keywords[i])
    wordcloud = WordCloud(background_color='white',font_path='./simhei.ttf').generate(topic_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Topic {i+1} Keywords')
    plt.savefig(f'./topic/主题{i}.jpg')
    plt.show()
