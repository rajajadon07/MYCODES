import streamlit as st
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='73770f3d51ef4ebbb571859c4ac153c1')
from pandas.io.json import json_normalize
import pandas as pd
import pprint as pp
import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta


def top_headlines():
    country=st.text_input("Which country are you interested in?")
    category=st.text_input("""Which category are you interested in? \nHere are the categories to choose from: 
                   \nbusiness\nentertainment\ngeneral\nhealth\nscience\ntechnology""")
    
    top_headlines = newsapi.get_top_headlines(category=category,language='en',country=country)
    top_headlines=json_normalize(top_headlines['articles'])
    newdf=top_headlines[["title","url"]]
    dic=newdf.set_index('title')['url'].to_dict()
    top_headlines
    for (k,v) in dic.items():
           st.write(k+"\n\n"+v)
           query=st.text_input('enter your query')
           def date(base):
              date_list=[]
              yr=datetime.today().year
              if (yr%400)==0 or ((yr%100!=0) and (yr%4==0)):
                    numdays=366
                    date_list.append([base - timedelta(days=x) for x in range(366)])
              else:
                numdays=365
                date_list.append([base - timedelta(days=x) for x in range(365)])
                newlist=[]
                for i in date_list:
                    for j in sorted(i):
                        newlist.append(j)
                return newlist

           def last_30(base):

                date_list=[base - timedelta(days=x) for x in range(30)]
                return sorted(date_list)


           def from_dt(x):
                from_dt=[]
                for i in range(len(x)):
                    from_dt.append(last_30(datetime.today())[i-1].date())
                return from_dt

           def to_dt(x):
                to_dt=[]
                for i in range(len(x)):
                    to_dt.append(last_30(datetime.today())[i].date())
                return to_dt
           from_list=from_dt(last_30(datetime.today()))
           to_list=to_dt(last_30(datetime.today()))
          
           def func(query):
                newdf=pd.DataFrame()
                for (from_dt,to_dt) in zip(from_list,to_list):
                    all_articles = newsapi.get_everything(q=query,language='en',sort_by='relevancy',  from_param=from_dt,to=to_dt)
                    d=json_normalize(all_articles['articles'])
                    newdf=newdf.append(d)

                return newdf
           df1=pd.DataFrame(func('Travel risk'))
          
top_headlines()
