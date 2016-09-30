# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:53:20 2016

@author: gus
"""

import pandas as pd
import numpy as np

df = pd.read_csv('details_NG_1990_out_results_old_v2.csv')

print len(df)

df.drop_duplicates(inplace=True)

print len(df)

good_df = df[df['latitude'].notnull()]

good_df[['latitude', 'longitude','temp_max', 'temp_min', 'precipitation', 'wind_avg', 'solar', 'humid_max', 'humid_min']] = \
good_df[['latitude', 'longitude','temp_max', 'temp_min', 'precipitation', 'wind_avg', 'solar', 'humid_max', 'humid_min']].apply(pd.to_numeric, errors='coerce')

print "Changed Columns"
bad_df = df[df['errorId'].notnull()]

grp_df = good_df.groupby(['id', 'latitude', 'longitude'], as_index=False)

avgs_df = grp_df.aggregate({"wind_avg":np.mean, "precipitation": np.mean, "humid_max":np.mean, 
                            "humid_min":np.mean, "temp_max": np.mean, "temp_min": np.mean})
                            
avgs_df['clean_id'] = pd.to_numeric(avgs_df['id'].str.split("_").str.get(1))

avgs_df['Date'] = avgs_df['id'].str.split("_").str.get(4) + "-" + avgs_df['id'].str.split("_").str.get(5)

#avgs_df['CleanDate'] = avgs_df['Date'].apply(lambda x: "0"+str(x).split("-")[1] if len(str(x)).split("-")[1] < 2 else x)

avgs_df['clean_date'] = avgs_df['Date'].apply(lambda x: str(x).split("-")[0] + "-0" + str(x).split("-")[1] if len(str(x).split("-")[1]) < 2 else x)

myPivot = avgs_df.pivot_table(values=['temp_max', 'temp_min', 'humid_max', 'humid_min', 'precipitation', 'solar'], 
                                   index=['clean_id', 'latitude', 'longitude'], columns='clean_date')
"""
try:
    monthly_averages = good_df.aggregate({"wind_avg":np.mean, "precipitation": np.mean, "humid_max":np.mean, "humid_min":np.mean,
                                 "temp_max": np.mean, "temp_min": np.mean})
except (pd.core.groupby.DataError, KeyError):
    monthly_averages = good_df.aggregate({"temp_max": np.mean, "temp_min": np.mean})

"""
"""
with open(r'details_NG_1990_out_results_old_v2.csv') as f:
    content = f.readlines()
    for row in content:
        print row
"""
        
