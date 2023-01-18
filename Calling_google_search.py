import streamlit as st
from googlesearch import search
from bs4 import BeautifulSoup

import requests

st.title("Critical information nearby me")
gl = st.selectbox("Select your country region",("us", "uk", "fr", "de"))


if gl=="us":
    query=st.text_input("Please enter your query here")
    for i in search(query,tld='co.in',lang='en',num=5,stop=5,pause=2,gl=gl):
          req=requests.get(i)
          soup = BeautifulSoup(req.text, 'html.parser')
          st.write("Title of this website: " )
          for title in soup.find_all('title',limit=1):
            st.write(title.get_text())
            st.write(i)
         
elif gl=="br":
    query=st.text_input("Please enter your query here")
    for i in search(query,tld='co.in',lang='en',num=5,stop=5,pause=2,gl=gl):
          req=requests.get(i)
          soup = BeautifulSoup(req.text, 'html.parser')
          st.write("Title of this website: " )
          for title in soup.find_all('title',limit=1):
            st.write(title.get_text())
            st.write(i)
         

         
   
option=st.number_input('Top results', format='%i')
col1,col2,col3=st.columns(3)

if option <2 and option < 3:
      for i in search(query,tld='co.in',lang='en',num=1,stop=1,pause=2):
         result1=st.write(i)
         col1.header("Top result 1")
         for title in soup.find_all('title',limit=1):
            st.write(title.get_text())


elif option > 1 and option < 3:
      for i in search(query,tld='co.in',lang='en',num=2,stop=2,pause=2):
         temp=2
         count=1
         col2.header("Top result 2")
         if count<temp:
            result2=st.write(i)
            for title in soup.find_all('title',limit=1):
             st.write(title.get_text())
            count=+1
              
elif option > 1 and option > 2:
     for i in search(query,tld='co.in',lang='en',num=3,stop=3,pause=2):
        temp=3
        count=1
        col3.header("Top result 3")
        if count<temp:
           result3=st.write(i)
           for title in soup.find_all('title',limit=1):
              st.write(title.get_text())
           count=+1
          
             


  
