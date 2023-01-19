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
          
       data = {'link':[i],'Title':[heading],'source':['cnn','bbc']}
       df = pd.DataFrame(data, index=[{'S.no':[1,2,3,4,5]}])
       st.dataframe(df)
       st.write(df)


 
