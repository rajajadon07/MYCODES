import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json

st.title("Critical information nearby me")
query = st.text_input("Enter your query")



def get_news():
    api_key = "AIzaSyDEhUWGKuYW8G3JR3CpStnveTqu1gXrBD4"
    url = "https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=" + api_key
    response = requests.get(url)
    news_data = response.json()
    return news_data

def main():
    news_data = get_news()
    for article in news_data["articles"]:
        st.title(article["title"])
        st.write(article["description"])

if __name__ == "__main__":
    main()






         



          
          
     

           
         
        

        
          


 
