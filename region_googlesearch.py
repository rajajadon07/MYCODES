import streamlit as st
from serpapi import GoogleSearch

params = {
    "q" : "Coffee",
    "location" : "Austin, Texas, United States",
    "hl" : "en",
    "gl" : "us",
    "google_domain" : "google.com",
    "api_key" : "demo",
}

query = GoogleSearch(params)
dictionary_results = query.get_dict()
 
