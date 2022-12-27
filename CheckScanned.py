import streamlit as st
import pandas as pd
import base64,random
import time,datetime
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
import io,random
from streamlit_tags import st_tags
from PIL import Image
import plotly.express as px
import docx2txt
import nltk




def show_pdf(file_path):
    with open(file_path, "./temp/fb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)



def run():
    st.title("Scanned or Digital PDF Identifier")
    img = Image.open('C:/Users/rjadon/Documents/Scanned_UnScanned/logo.jpg')
    st.image(img)

    
    if True:
        pdf_file = st.file_uploader("Choose your file", type=["pdf"])
        st.text(pdf_file.name)
        
        
        if pdf_file is not None:
            save_image_path = 'C:/Users/rjadon/Documents/Scanned_UnScanned/temp'+pdf_file.name
            
            directory = r'C:\Users\rjadon\Documents\Scanned_UnScanned\temp\fb.pdf'
            st.text(directory)

            pdfFileObj = open(pdf_file.name, 'fb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj , strict=False)
            page_data = pdfReader.getPage(0)

            if '/Font' in page_data['/Resources']:
                st.success("This is digital PDF with below tags")
                st.text(page_data['/Resources'].keys())
            else :
                st.error("This is a scanned pdf with below tags" )
                st.text(page_data['/Resources'].keys())    
                              
                   
            with open(save_image_path, "C:/Users/rjadon/Documents/Scanned_UnScanned/logo.jpg") as f:
                f.write(pdf_file.getbuffer())
            show_pdf(save_image_path)            
                                     
run()
