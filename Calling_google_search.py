import streamlit as st
from googlesearch import search
from bs4 import BeautifulSoup

import requests

st.title("Critical information nearby me")
menu=["USA","CHINA","RUSSIA","BRAZIL","FRANCE","GERMANY","JAPAN"]
choice=st.sidebar.selectbox("Country Selection",menu)

if choice=="USA":
    result="USA"
    query=st.text_input("Please enter your query here")
    for i in search(query,tld='co.in',country=result ,lang='en',num=5,stop=5,pause=2):
          req=requests.get(i)
          soup = BeautifulSoup(req.text, 'html.parser')
          st.write("Title of this website: " )
          for title in soup.find_all('title',limit=1):
            st.write(title.get_text())
            st.write(i)
         
elif choice=="CHINA":
    result="CHINA"
    query=st.text_input("Please enter your query here")
    for i in search(query,tld='co.in',country=result ,lang='en',num=5,stop=5,pause=2):
          req=requests.get(i)
          soup = BeautifulSoup(req.text, 'html.parser')
          st.write("Title of this website: " )
          for title in soup.find_all('title',limit=1):
            st.write(title.get_text())
            st.write(i)
         
elif choice=="RUSSIA":
    result="RUSSIA"
    query=st.text_input("Please enter your query here")
    for i in search(query,tld='co.in',country=result ,lang='en',num=5,stop=5,pause=2):
          req=requests.get(i)
          soup = BeautifulSoup(req.text, 'html.parser')
          st.write("Title of this website: " )
          for title in soup.find_all('title',limit=1):
            st.write(title.get_text())
            st.write(i)
         
elif choice=="BRAZIL":
    result="BRAZIL"
    query=st.text_input("Please enter your query here")
    for i in search(query,tld='co.in',country=result ,lang='en',num=5,stop=5,pause=2):
          req=requests.get(i)
          soup = BeautifulSoup(req.text, 'html.parser')
          st.write("Title of this website: " )
          for title in soup.find_all('title',limit=1):
            st.write(title.get_text())
            st.write(i)
         
elif choice=="FRANCE":
    result="FRANCE"
    query=st.text_input("Please enter your query here")
    for i in search(query,tld='co.in',country=result ,lang='en',num=5,stop=5,pause=2):
          req=requests.get(i)
          soup = BeautifulSoup(req.text, 'html.parser')
          st.write("Title of this website: " )
          for title in soup.find_all('title',limit=1):
            st.write(title.get_text())
            st.write(i)
         
elif choice=="GERMANY":
    result="GERMANY"
    query=st.text_input("Please enter your query here")
    for i in search(query,tld='co.in',country=result ,lang='en',num=5,stop=5,pause=2):
          req=requests.get(i)
          soup = BeautifulSoup(req.text, 'html.parser')
          st.write("Title of this website: " )
          for title in soup.find_all('title',limit=1):
           st.write(title.get_text())
           st.write(i)
         
elif choice=="JAPAN":
    result="JAPAN"
    query=st.text_input("Please enter your query here")
    for i in search(query,tld='co.in',country=result ,lang='en',num=5,stop=5,pause=2):
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
         for title in soup.find_all('title'):
            st.write(title.get_text())


elif option > 1 and option < 3:
      for i in search(query,tld='co.in',lang='en',num=2,stop=2,pause=2):
         temp=3
         count=2
         result2=st.write(i)
      if count<temp:
           col2.header("Top result 2")
           count=count+1
      for title in soup.find_all('title'):
              st.write(title.get_text())
              
elif option > 1 and option > 2:
     for i in search(query,tld='co.in',lang='en',num=3,stop=3,pause=2):
        temp=4
        count=3
        result3=st.write(i)
        if count<temp:
           col3.header("Top result 3")
        for title in soup.find_all('title'):
              st.write(title.get_text())
              count=count+1
        


  
