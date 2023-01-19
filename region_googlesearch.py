import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json

st.title("Critical information nearby me")
query = st.text_input("Enter your query")

api_key=AIzaSyDYCPvmSL8RHxDIkukU2-VRy9FJA9I9bLk
if st.button("Search"):
        def search(query,api_key):
          query = query.replace(" ", "+")
          URL = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={https://cse.google.com/cse.js?cx=f23358939906b4e32}&q={query}"
          r = requests.get(url=URL)
          data = r.json()
          return data
          results = search(query, api_key)
          st.write(results)
          
         
        

        
          


 
