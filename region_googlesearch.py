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
          URL = f"https://www.googleapis.com/customsearch/v1?key={AIzaSyDEhUWGKuYW8G3JR3CpStnveTqu1gXrBD4}&cx={f23358939906b4e32}&q={query}"
          r = requests.get(url=URL)
          data = r.json()
        return data
          results = search(query)
          st.write(results)
          
         
        

        
          


 
