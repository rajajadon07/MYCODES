
import streamlit as st 
import PyPDF2
import json

file=st.file_uploader("upload your file",type=["json"])

# Open the PDF file
with open('export.json', 'rb') as f:
 data=json.load(f)
 st.write(data)

