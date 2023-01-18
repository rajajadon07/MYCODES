import streamlit as st



search_query = st.search_bar(label='Search', region='fr')

if search_query:
  st.text_input("enter your query")
 
