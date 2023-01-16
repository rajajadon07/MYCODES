import streamlit as st
from googlesearch import search
from bs4 import BeautifulSoup

import requests

query=st.text_input("Enter your text here")

for i in search(query,tld='co.in',lang='en',num=5,stop=5,pause=2):
     req=requests.get(i)
     soup = BeautifulSoup(req.text, 'html.parser')
     st.write("Title of this website: " )
     for title in soup.find_all('title'):
          st.write(title.get_text())
          st.write(i)
         
   
   

option=st.number_input('Top results', format='%i')
col1,col2,col3=st.columns(3)

if option <2 and option < 3:
      result1=st.write(i)
      col1.header("Top result 1")
      for title in soup.find_all('title'):
          st.write(title.get_text())


elif option > 1 and option < 3:
      temp=3
      count=2
      result2=st.write(i)
      if count<temp:
         col2.header("Top result 2")
         for title in soup.find_all('title'):
            st.write(title.get_text())
            count=count+1
elif option > 1 and option > 2:
     temp=4
     count=3
     result3=st.write(i)
     if count<temp:
        col3.header("Top result 3")
        for title in soup.find_all('title'):
           st.write(title.get_text())
           count=count+1
        


  
