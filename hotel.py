# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import category_encoders as ce
import collections
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#import and get info
df = pd.read_csv('Dataset.csv', sep=";")
df.info()

#Let's drop the this values
df_after = df[(df.Age > 0) & (df.Age <= 112)]
df_after = df_after[df_after.AverageLeadTime >= 0]
df_after

cl = ['LodgingRevenue', 'OtherRevenue','BookingsCanceled','BookingsNoShowed', 'BookingsCheckedIn', 'PersonsNights', 'RoomNights', 'DistributionChannel', 'MarketSegment']
test = df_after[cl]
test = test[(test.LodgingRevenue == 0) & (test.OtherRevenue == 0) ]
to = test[test.PersonsNights > 0]
to2 = test[(test.BookingsCanceled == 0) & (test.BookingsNoShowed == 0) & (test.BookingsCheckedIn == 0)]
#test.columns