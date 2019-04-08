# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 18:51:17 2019

@author: Pupi
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import matplotlib.pyplot as plt
import os
from os import path
from PIL import Image
import collections
import re, string
import sys
import time
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from mpl_toolkits.basemap import Basemap
nltk.download('stopwords')
from subprocess import check_output
%matplotlib inline

dir_path = os.path.dirname(os.path.abspath('yelp_business_attributes.csv'))
dir_path = dir_path + '\\Yelp\\'

df_bus = pd.read_csv(dir_path + 'yelp_business.csv')
df_ba = pd.read_csv(dir_path + 'yelp_business_attributes.csv')
df_bh = pd.read_csv(dir_path + 'yelp_business_hours.csv')
df_check = pd.read_csv(dir_path + 'yelp_checkin.csv')
df_review = pd.read_csv(dir_path + 'yelp_review.csv')
df_tip = pd.read_csv(dir_path + 'yelp_tip.csv')
df_user = pd.read_csv(dir_path + 'yelp_user.csv')

df_user.columns

df_bus.columns
df_ba.columns
df_user.columns



# calculating reviews ratios by business
df_review.columns

df_review_melt = df_review.groupby(['business_id','stars'], as_index=False).agg({"review_id": "count"})
df_review_pivot = pd.pivot_table(df_review_melt,index='business_id',columns='stars',values='review_id', )
df_review_pivot = df_review_pivot.reset_index()

df_review_pivot['tot_review'] = df_review_pivot.drop('business_id', axis=1).sum(axis=1)
df_review_pivot['high_review_ratio'] = df_review_pivot[[4,5]].sum(axis=1)/df_review_pivot['tot_review']
df_review_pivot['low_review_ratio'] = df_review_pivot[[1,2]].sum(axis=1)/df_review_pivot['tot_review']
df_review_pivot.fillna(0, inplace=True)

df_stars = df_review.groupby(['stars'], as_index = False).agg({"review_id": "count"})

df_5 = df_review[df_review['stars'] == 5]
df_1 = df_review[df_review['stars'] == 1]

def preprocess(x):
    x = re.sub('[^a-z\s]', '', x.lower())                  # get rid of noise
    x = [w for w in x.split() if w not in set(stopwords)]  # remove stopwords
    return ' '.join(x) # then join the text again
# let's find out which stopwords need to remove. We'll use english stopwords.
i = nltk.corpus.stopwords.words('english')
# punctuations to remove
j = list(string.punctuation)
# finally let's combine all of these
stopwords = set(i).union(j)

df_5['text_clear'] = df_5['text'].apply(preprocess)
df_1['text_clear'] = df_1['text'].apply(preprocess)


wc = WordCloud(width=1600, height=800, random_state=1, max_words=200000000)
# generate word cloud using df_yelp_tip_top['text_clear']
wc.generate(str(df_1['text_clear']))
# declare our figure 
plt.figure(figsize=(20,10), facecolor='k')
# add title to the graph
plt.title("1 Stars Restaurants", fontsize=40,color='white')
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=10)
# after lot of congiguration finally plot the graph
plt.show()