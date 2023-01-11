import streamlit as st
from googlesearch import search
import urllib
from bs4 import BeautifulSoup
st.code(
 def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

 i = 1
 query = 'search this'
 for url in search(query, stop=10):
    a = google_scrape(url)
    print str(i) + ". " + a
    print url
    print " "
    i += 1
)
