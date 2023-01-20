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
        def get_news(query,api_key):
          query = query.replace(" ", "+")
          URL = f"https://newsapi.org/v2/top-headlines?sources=google-news&apiKey="+ api_key +query
          response = requests.get(url=URL)
          news_data = response.json()
          st.write(news_data)
          return news_data
       
        def main():
         news_data = get_news(query,api_key)
         for article in news_data["articles"]:
              st.title(article["title"])
              st.write(article["description"])

if __name__ == "__main__":
        main()
         



          
          
     

           
         
        

        
          


 
