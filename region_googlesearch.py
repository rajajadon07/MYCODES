import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json
import gnews from GNews

topic=.text_input('enter your query')
keyword=('Threats,Risk,Danger,Riots, issues , pandemic , riots, agression')
country = st.sidebar.selectbox('select your country',
                              ('us','uk'))
stories= GNews.get_news_by_topic(topic) 

for story in top_stories:
    st.markdown(f"- [{story['title']}]({story['link']})")
    st.markdown(story['description'])








    






         



          
          
     

           
         
        

        
          


 
