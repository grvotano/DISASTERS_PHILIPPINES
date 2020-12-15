#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:53:56 2020

@author: giovanniremovotano
"""

import os
import pandas as pd
from datetime import datetime
import datetime
import matplotlib.pyplot as plt

foldername = r'/Users/giovanniremovotano/OneDrive - UvA/OneDrive - UvA/Philippines_Consecutive_Disasters_and_Migration_master/DATA/RAW'
filename = "EM_DAT_1980_2010_GEOCODED.csv"

full_path = os.path.join(foldername, filename)
data = pd.read_csv(full_path, parse_dates= ['start_isodate', 'end_isodate'] ,usecols= ('country_name', 'place_name', 'start_isodate',
       'end_isodate', 'latitude', 'longitude', 'year', 'location',
       'disaster_group', 'disaster_subgroup', 'disaster_type',
       'disaster_subtype', 'disaster_subsubtype', 'associated_disaster', 'no_killed', 'total_dam_usd', 'even_split_dam_usd' ))

# change column names
new_names = {'start_isodate': 'start_date', 'end_isodate': 'end_date' }
data = data.rename(columns= new_names)

## drop all rows with naa values 
data.dropna(axis=0, how = 'any', subset=['start_date'], inplace = True)
data.dropna(axis=0, how = 'any', subset=['end_date'], inplace = True)


# drop rows with incomplete dates
data.drop(axis=0,  index=0, inplace= True)

#data.drop(axis=0, how = 'any', subset=['start_date'], inplace = True)
#data.drop(axis=0, how = 'any', subset=['end_date'], inplace = True)

# convert from object to date-time

data['start_date'] = pd.to_datetime(data['start_date'], format="%y/%m/%d, %H:%M:%S")
data['end_date'] = pd.to_datetime(data['end_date'], format="%y/%m/%d, %H:%M:%S")
# new colun for duration of event
data['duration'] = data['end_date'] - data['start_date']

# basic plotting 
plt.scatter(data['year'], data['disaster_type'], linewidth= 1)
plt.scatter(data['start_date'], data['disaster_type'])
