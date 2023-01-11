import streamlit as st
from googlesearch import search

find=st.text_input("Enter your text here")
query = find
num=st.selectbox('Select days your want search result for',
                         ('1','2','3'))
for i in search(query,tld='co.in',lang='en',num,stop=10,pause=2):
     if i>1 and i>2:
      st.write(i)
     elif i>1 and i<3:
      st.write(i)
     else i<2 and i<3:
      st.write(i)
