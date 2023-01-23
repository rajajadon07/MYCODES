import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json
from gnews import GNews
from datetime import datetime, timedelta


api_key = '96cff03d866a222cb5837f417a57eb85'

query=st.text_input('enter your query')        
topic = st.sidebar.selectbox("Topic", ["health","science","breaking news"])
country = st.sidebar.selectbox("Country", ["us", "in", "gb", "fr", "jp","gb"])
date_from = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
date_to = (datetime.now().strftime("%Y-%m-%d")


           
   url = f'https://gnews.io/api/v3/search?q={query}&topic={topic}&country={country}&date_from={date_from}&date_to={date_to}&token{api_key}'
   news = requests.get(url).json()
                                
   for article in news['articles']:
      st.write("Title:", article['title'])
      st.write("Published at:", article['publishedAt'])
      st.write("description:", article['description'])
      st.write("Source:", article['source']['name'])
      st.write("Link:", article['url'])
     
 



           





    






         



          
          
     

           
         
        

        
          


 
