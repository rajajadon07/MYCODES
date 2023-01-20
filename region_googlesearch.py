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

country_code=st.sidebar.selectbox("select your country",
                  ('us','uk'))
if st.button("Search"):
 def get_news():
    url = "https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    response = requests.get(url)
    news_data = response.json()
    st.write(news_data)
    return news_data

 def main():
    news_data = get_news()
    for article in news_data:
        st.title(article["title"])
        st.write(article["link"])
        st.write(article["url"])
       

if __name__ == "__main__":
    main()
    






         



          
          
     

           
         
        

        
          


 
