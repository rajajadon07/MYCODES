import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json
from gnews import GNews

topic=st.text_input('enter your query')
if st.button('Search'):
  keyword=('Threats,Risk,Danger,Riots, issues , pandemic , riots, agression')
  country = st.sidebar.selectbox('select your country',
                              ('us','uk'))
  stories= GNews.get_top_news(topic) 

  for story in top_stories:
    st.markdown(f"- [{story['title']}]({story['link']})")
    st.markdown(story['description'])








    






         



          
          
     

           
         
        

        
          


 
