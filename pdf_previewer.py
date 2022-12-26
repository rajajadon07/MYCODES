import streamlit as st
import PyPDF2
st.title("PDF upload and previewer")
st.subheader("let's start")
pdf_file=st.file_uploader("upload your pdf file",type=["pdf"])
st.button("Process")
if pdf_file is not None:
 st.write(type(pdf_file))
