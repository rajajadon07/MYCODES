import streamlit as st
from googlesearch.googlesearch import GoogleSearch
import requests

find=st.text_input("Enter your text here")


response = GoogleSearch().search(find)
for results in reponse.results:
     Title=result.title
     Title_text=result.getText()
     st.write("Title: ",Title,Title_text)
     st.write(result)
   
   
   

option=st.number_input('Top results', format='%i')
col1,col2,col3=st.columns(3)

if option <2 and option < 3:
   for i in search(query,tld='co.in',lang='en',num=1,stop=1,pause=2):
     result1=st.write(i)
     col1.header("Top result 1")


elif option > 1 and option < 3:
     temp=3
     count=2
     for i in search(query,tld='co.in',lang='en',num=2,stop=2,pause=2):
       result2=st.write(i)
       if count<temp:
          col2.header("Top result 2")
          count=count+1
elif option > 1 and option > 2:
     temp=4
     count=3
     for i in search(query,tld='co.in',lang='en',num=3,stop=3,pause=2):
       result3=st.write(i)
       if count<temp:
          col3.header("Top result 3")
          count=count+1
        


  
