import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json
from  gnewsclient import gnewsclient


client = gnewsclient.Client()

query = st.text_input('enter your query')
country = st.sidebar.selectbox('select your country',
                              ('us','uk'))
search_results = client.search(query,location='country', max_results=10)


for story in search_results:
    st.write(story['title'])
    st.write(story['description'])
    st.write(story['link'])
   



    






         



          
          
     

           
         
        

        
          


 
