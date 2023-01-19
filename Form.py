
import streamlit as st 
import PyPDF2
import json

pdf=st.file_uploader("upload your file",type=["pdf"])
# Open the PDF file
with open('SOP-GBS-0053-TEN-FIN-AR-JEE-Accruals booking-TEN.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ''
    # Loop through all pages
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extractText()

# Convert the text to JSON format
json_data = json.loads(text)

# Access the data in the JSON format
print(json_data['key'])

