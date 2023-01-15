import streamlit as st
from googlesearch import search

find=st.text_input("Enter your text here")
query = find
option=st.selectbox('Select days your want search result for',
                         ('1','2','3'))
if option >1 and option >2:
 for i in search(query,tld='co.in',lang='en',num=5,stop=5,pause=2):
        st.write(i)

  
