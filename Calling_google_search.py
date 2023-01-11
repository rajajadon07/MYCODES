import streamlit as st
from googlesearch import search
inp=st.text_input("Enter your text here")
query = 'inp'

for i in search(query,tld='co.in',lang='en',num=10,stop=10,pause=2):
     st.write(i)
