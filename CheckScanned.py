import streamlit as st
import pandas as pd
import base64,random
import time,datetime
import pdfplumber
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfReader
import io,random
from streamlit_tags import st_tags
from PIL import Image
import plotly.express as px
import docx2txt
import nltk



def show_pdf(pdf_file):
    with open(pdf_file, 'rb') as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    



def run():
    st.title("Scanned or Digital PDF Identifier")
    img = Image.open("./Logo/logo.jpg")
    st.image(img)

    
    if True:
        pdf_file = st.file_uploader("Choose your file", type=["pdf"])
        if True:
         st.text(pdf_file.name)
        
        
        if pdf_file is not None:
            save_image_path = './Scanned_UnScanned'+ pdf_file.name
            
            directory = r'.\Scanned_UnScanned\temp '+ pdf_file.name
            st.text(directory)

            pdfFileObj = open(pdf_file.name, 'rb') 
            pdf_Reader = PdfReader(pdfFileObj)
            page_data = pdf_Reader.pages[0]
            count=0
            
            for image_file_object in page_data.images:
                with open(str(count) + image_file_object.name, "wb") as fp:
                     fp.write(image_file_object.data)
                     count += 1

            if '/Font' in page_data['/Resources']:
                st.success("This is digital PDF with below tags")
                st.text(page_data['/Resources'].keys())
            else :
                st.error("This is a scanned pdf with below tags" )
                st.text(page_data['/Resources'].keys())    
                              
                   
            with open(save_image_path,'wb') as f:
                f.write(pdf_file.getbuffer())
            show_pdf(save_image_path)            
                                     
run()
