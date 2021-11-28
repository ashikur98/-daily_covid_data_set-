from bs4 import BeautifulSoup
import requests as req    
import pandas as pd
import os
from datetime import date

# getting worldometer data
contents = req.get("https://www.worldometers.info/coronavirus/")
res=[]
soup = BeautifulSoup(contents.text, 'lxml')
table = soup.find_all('table')[1]
table_rows = table.find_all('tr')
data_row=pd.DataFrame()
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    if(len(row)>0):
        res.append(row) 

# Formatting Data

column_dict = {1:'Country',2:'Total cases',3:'New Cases',4:'Total Deaths',5:'New Deaths',6:'Total Recovered',\
               7:'New Recovered',8:'Active cases',9:'Serious,Critical',10:'Tot cases 1M pop',11:'Death 1M pop',\
               12:'Total Tests',13:'Tests 1M pop',14:'Population'}

# pd.set_option("display.max_rows", None, "display.max_columns", None)
tmp_df = pd.DataFrame(res)
tmp_df = tmp_df[tmp_df[0] != ''].reset_index()
tmp_df.drop(['index', 0,15,16,17,18,19,20,21], axis = 1, inplace=True)
tmp_df.rename(columns=column_dict, inplace=True)
tmp_df.to_csv('covid_19_country_data.csv',index=False)
