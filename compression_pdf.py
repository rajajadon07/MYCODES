import pikepdf
import base64
import streamlit as st

from PyPDF2 import PdfReader, PdfWriter

uploader_pdf=st.file_uploader('Choose your pdf',accept_multiple_files=True)
st.write(uploader_pdf)
reader = PdfReader(uploader_pdf)
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams() 
    writer.add_page(page)

with open(uploader_pdf, "wb") as f:
    writer.write(f)
