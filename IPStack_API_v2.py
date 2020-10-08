# -*- coding: utf-8 -*-
"""
Created on Thu Oct 8 11:35:00 2020

@author: mtav
"""
import os
import requests
import json
import pandas as pd

from dotenv import load_dotenv
load_dotenv()


myToken = os.environ.get("api-token")
url = 'http://api.ipstack.com/'
search_term = ['121.223.153.177',
               '14.201.123.98',
               '121.223.158.71']

#THIS SECTION TO READ RAW JSON FOR SINGLE IP - TESTING

# response = requests.get(url + str(search_term[0]) + '?access_key=' + myToken)
# print(response.json())

#THIS SECTION TO LOOP THROUGH IPs AND RETURN SPECIFIC FIELDS

search_results = []                           
while search_term:
    for ip in search_term:
        JSONContent = requests.get(url + str(search_term[0]) + '?access_key=' + myToken).json()
        if 'error' not in JSONContent:
            search_results.append([JSONContent['ip'], 
                                JSONContent['country_code'], 
                                JSONContent['city'], 
                                JSONContent['zip'],
                                JSONContent['connection']['isp'],
                                JSONContent['latitude'],
                                JSONContent['longitude']
                                ])
            del search_term[0]
    
ip_df = pd.DataFrame(search_results)
ip_df.columns=['ip_address','country','city','post_code','isp','latitude','longitude']
print(ip_df)


ip_df.to_csv(r'IPCountries.csv',index=False)

