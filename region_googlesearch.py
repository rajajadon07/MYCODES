import streamlit as st
import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup

st.title("Critical information nearby me")
query=st.text_input("Please enter your query here")
st.write("Results for:", query)
for i in search(query,tld='com',lang='en',num=5,stop=5,pause=2):
      req=requests.get(i)
      soup = BeautifulSoup(req.text, 'html.parser')
      for title in soup.find_all('title',limit=1):
       heading=st.write(title.get_text())
       sources='cnn','bbc','fox','google','cbs'
          
       data = {'link':[i],'Title':[heading],'source':[sources]}
       df = pd.DataFrame(data)
       results=st.dataframe(df)
       for i in results:
            st.write(i)


 
