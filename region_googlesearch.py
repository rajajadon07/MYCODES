import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json
import gnews


client = gnews.Client()



query = st.text_input('enter your query')
search_results = client.search(query, max_results=10)


for story in search_results:
    print(story['title'])
    print(story['description'])
    print(story['link'])
    print('\n')



    






         



          
          
     

           
         
        

        
          


 
