import streamlit as st
from googlesearch import search

find=st.text_input("Enter your text here")
query = find
option=st.number_input('Insert the number of days', format='{%i}')
if option <2 and option < 3:
    for i in search(query,tld='co.in',lang='en',num=1,stop=1,pause=2):
        st.write(i)
elif option > 1 and option < 3:
    for i in search(query,tld='co.in',lang='en',num=2,stop=2,pause=2):
        st.write(i)
elif option > 1 and option > 2:
    for i in search(query,tld='co.in',lang='en',num=3,stop=3,pause=2):
        st.write(i)

  
