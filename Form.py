import pdfplumber
from PyPDF2 import PdfWriter
import streamlit as st 
import PyPDF2
import json
import os

if os.path.exists('export.json'):
    with open('export.json', 'rb') as f:
        data = json.load(f)
        st.write(data)
else:
    st.warning("File not found.")



