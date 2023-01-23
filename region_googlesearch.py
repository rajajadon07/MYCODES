import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json
from gnews import GNews

keyword=('Threats,Risk,Danger,Riots, issues , pandemic , riots, agression')
api_key = '96cff03d866a222cb5837f417a57eb85'
country_id=st.sidebar.selectbox('select your country',
                                ('USA','UK'))

query=st.text_input('enter your query')
if st.button('Search'):
   url = f'https://gnews.io/api/v3/search?q={query}&topic={keyword}&sort_by={publishedAt}&country={country_id}&token={api_key}'
   news = requests.get(url).json()
                                
   for article in news['articles']:
      st.write("Title:", article['title'])
      st.write("Published at:", article['publishedAt'])
      st.write("Source:", article['source']['name'])
      st.write("Link:", article['url'])
      









    






         



          
          
     

           
         
        

        
          


 
