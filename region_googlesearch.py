import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json
from gnewsclient import Client

client = Client()
client.language = 'en'
client.location = 'United States'
client.topic = 'top_stories'

data = client.get_news()

for i in range(5):
    st.write(data[i]['title'])
    st.write(data[i]['link'])
    
    






         



          
          
     

           
         
        

        
          


 
