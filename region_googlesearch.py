import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup

st.title("Critical information nearby me")
query = st.text_input("Enter your query")
if st.button("Search"):
        def search(query):
        query = query.replace(" ", "+")
        URL = f"https://www.google.com/search?q={query}"
        r = requests.get(url = URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup
    soup = search(query)
    titles = soup.findAll("div", {"class": "BNeawe iBp4i AP7Wnd"})
    heading=st.write(titles)



       sources='cnn','bbc','fox','google','cbs'
       no='1','2','3','4','5'
          
       data = {'s.no':[no],'link':[url],'Title':[heading],'source':[sources]}
       df = pd.DataFrame(data)
       st.dataframe(df)
    


 
