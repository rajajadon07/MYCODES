import streamlit as st
st.title("PDF upload and previewer")
st.subheader("let's start")
pdf_file=st.file_uploader("upload your pdf file",type=["pdf"])
st.button("Process")
if pdf_file is not None:
 pass
 
