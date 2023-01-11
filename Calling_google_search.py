import streamlit as st
from googlesearch import search

find=st.text_input("Enter your text here")
query = find
option_days=st.selectbox('Select days your want search result for',
                         ('1','2','3'))
for i in search(query,tld='co.in',lang='en',num=10,stop=10,pause=2):
     st.write(i)
