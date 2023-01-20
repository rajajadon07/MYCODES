import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json

st.title("Critical information nearby me")
query = st.text_input("Enter your query")
api_key="AIzaSyDEhUWGKuYW8G3JR3CpStnveTqu1gXrBD4"
cx="f23358939906b4e32"

if st.button("Search"):
        def search(query,api_key,cx):
          query = query.replace(" ", "+")
          URL = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
          r = requests.get(url=URL)
          data = r.json()
          return data
        results = search(query,api_key,cx)
        
        for i in range(10):
          text = results['items'][i]['snippet']
          link = results['items'][i]['link']
          title = results['items'][i]['title']
          st.write("Title :",title)
          st.write("description : ", text)
          st.write("Link: ", link)
         
          
          
     

           
         
        

        
          


 
