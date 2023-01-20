import streamlit as st
from googlesearch import search
from bs4 import BeautifulSoup
from gnewsclient import gnewsclient
import requests

st.title("Critical information nearby me")
region = st.selectbox("Select your country region",("us", "uk", "fr", "de"))
Newsfeed = gnewsclient.NewsClient(language='english', location='region', topic='Business', max_results=5)
Newsfeed.get_news()



