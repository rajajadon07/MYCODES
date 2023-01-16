import streamlit as st
from googlesearch import search

find=st.text_input("Enter your text here")
query = find

for i in search(query,tld='co.in',lang='en',num=5,stop=5,pause=2):
    st.write(i)
   
   
   

option=st.number_input('Top results', format='%i')
col1,col2,col3=st.columns(3)
temp=2
if option <2 and option < 3:
   for i in search(query,tld='co.in',lang='en',num=1,stop=1,pause=2):
    result1=st.write(i)
    if i<temp:
    col1.header("Top result 1")
    
       
elif option > 1 and option < 3:
   for i in search(query,tld='co.in',lang='en',num=2,stop=2,pause=2):
   result2=st.write(i)
   col2.header("Top result 2")

elif option > 1 and option > 2:
   for i in search(query,tld='co.in',lang='en',num=3,stop=3,pause=2):
   result3=st.write(i)
   col3.header("Top result 3")
        


  
