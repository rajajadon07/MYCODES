import streamlit as st
from googlesearch import search
inp=st.text_input("Enter your text here")
query = 'inp'

for i in search(query,lang='en',num=20,stop=20,pause=2):
     st.write(i)
