import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json

st.title("Critical information nearby me")
query = st.text_input("Enter your query")
st.button("Search")



def get_news():
    api_key = "73770f3d51ef4ebbb571859c4ac153c1"
    url = "https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=" + api_key + query
    response = requests.get(url)
    news_data = response.json()
    st.write(news_data)
    return news_data

def main():
    news_data = get_news()
    for article in news_data["articles"]:
        st.title(article["title"])
        st.write(article["description"])
        st.write(article["url"])
       

if __name__ == "__main__":
    main()






         



          
          
     

           
         
        

        
          


 
