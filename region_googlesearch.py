import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json
from gnews import GNews


api_key = '96cff03d866a222cb5837f417a57eb85'
topic = st.sidebar.selectbox("Topic", ["travel"])
country = st.sidebar.selectbox("Country", ["us", "in", "gb", "fr", "jp"])

query=st.text_input('enter your query')
if st.button('Search'):
   url = f'https://gnews.io/api/v3/search?q={query}&topic={topic}&sort_by=publishedAt&country={country}&token={api_key}'
   news = requests.get(url).json()
                                
   for article in news['articles']:
      st.write("Title:", article['title'])
      st.write("Published at:", article['publishedAt'])
      st.write("description:", article['description'])
      st.write("Source:", article['source']['name'])
      st.write("Link:", article['url'])
     
 








    






         



          
          
     

           
         
        

        
          


 
