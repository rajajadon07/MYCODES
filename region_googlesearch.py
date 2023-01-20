import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json

st.title("Critical information nearby me")
query = st.text_input("Enter your query")
st.button("Search")

country_code=st.sidebar.selectbox("select your country",
                  ('us','uk'))

def get_news():
    api_key = "73770f3d51ef4ebbb571859c4ac153c1"
    url = "https://newsapi.org/v2/query?sources=google-news&country={country_code}&apiKey={api_key}"
    response = requests.get(url)
    news_data = response.json()

    return news_data

def main():
    news_data = get_news()
    for article in news_data["articles"]:
        st.title(article["title"])
        st.write(article["description"])
        st.write(article["url"])
       

if __name__ == "__main__":
    main()
    






         



          
          
     

           
         
        

        
          


 
