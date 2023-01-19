import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json

st.title("Critical information nearby me")
query = st.text_input("Enter your query")


if st.button("Search"):
        def search(query):
          query = query.replace(" ", "+")
          URL = f"https://www.googleapis.com/customsearch/v1?key={AIzaSyDYCPvmSL8RHxDIkukU2-VRy9FJA9I9bLk}&cx={https://cse.google.com/cse.js?cx=f23358939906b4e32}&q={query}"
          r = requests.get(URL)
          st.write(URL)
          soup = BeautifulSoup(r.text, 'html.parser')
          for title in soup.find_all('title',limit=1):
            st.write(title.get_text())
          return soup
        soup = search(query)
          
         
        

        
          


 
