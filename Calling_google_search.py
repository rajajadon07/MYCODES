import streamlit as st
from googlesearch import search

find=st.text_input("Enter your text here")
query = option
option=st.selectbox('Select days your want search result for',
                         ('1','2','3'))

   for i in search(query,tld='co.in',lang='en',num=1,stop=1,pause=2):
        st.write(i)

  
