import streamlit as st
import docx2txt
import pdfplumber
st.title("PDF upload and previewer")
st.subheader("let's start")
pdf_file=st.file_uploader("upload your pdf file",type=["pdf"])
st.button("Process")
if pdf_file is not None:
 pdf_details={"pdf_name":pdf_file.name,"pdf_size":pdf_file.size,"pdf_type":pdf_file.type}
 st.write(pdf_details)
 pdf_type=pdf_file.type
if pdf_type=="application/pdf":
 read_pdf=str(pdf_file.read(),"utf-8")
 st.text(read_pdf)
