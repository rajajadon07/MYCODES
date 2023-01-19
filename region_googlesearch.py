import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup

st.title("Critical information nearby me")
query = st.text_input("Enter your query")
region = "us"
website = "cnn.com"

if st.button("Search"):
        def search(query):
          query = query.replace(" ", "+")
          URL = f"https://www.google.com/search?q={query}&site={website}&gl={region}"
          r = requests.get(url = URL)
          st.write(query)
          soup = BeautifulSoup(r.content, 'html.parser')
          return soup
        soup = search(query)
        for title in soup.find_all('title',limit=1):
            st.write(title.get_text())
         
        

        
          


 
