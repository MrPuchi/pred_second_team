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

from os import path
from PIL import Image
import collections
import re, string
import sys
import time
from nltk.corpus import stopwords
from wordcloud import WordCloud
from mpl_toolkits.basemap import Basemap

from subprocess import check_output
%matplotlib inline

df_bus = pd.read_csv('J:\\warut.khern-am-nuai\\Students\\MBA\\yelp_business.csv')
df_ba = pd.read_csv('J:\\warut.khern-am-nuai\\Students\\MBA\\yelp_business_attributes.csv')
df_bh = pd.read_csv('J:\\warut.khern-am-nuai\\Students\\MBA\\yelp_business_hours.csv')
df_check = pd.read_csv('J:\\warut.khern-am-nuai\\Students\\MBA\\yelp_checkin.csv')
df_review = pd.read_csv('J:\\warut.khern-am-nuai\\Students\\MBA\\yelp_review.csv')
df_tip = pd.read_csv('J:\\warut.khern-am-nuai\\Students\\MBA\\yelp_tip.csv')
df_user = pd.read_csv('J:\\warut.khern-am-nuai\\Students\\MBA\\yelp_user.csv')

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
