import streamlit as st
from googlesearch import search

find=st.text_input("Enter your text here")
query = find
for i in search(query,tld='co.in',lang='en',num=5,stop=5,pause=3):
   top_results=st.number_input('Top results , format='%i')
   if i>=top_results:
      st.write(i)
   
   
   
   
option=st.number_input('Top results', format='%i')
st.container(
if option <2 and option < 3:
    for i in search(query,tld='co.in',lang='en',num=1,stop=1,pause=2):
        st.write(i)
elif option > 1 and option < 3:
    for i in search(query,tld='co.in',lang='en',num=2,stop=2,pause=2):
        st.write(i)
elif option > 1 and option > 2:
    for i in search(query,tld='co.in',lang='en',num=3,stop=3,pause=2):
        st.write(i)
)
        


  
