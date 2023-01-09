import pikepdf
import streamlit as st
from PyPDF2 import PdfWriter

st.title("PDF Unlocker // Merger")

def main():
     
     option_op=st.selectbox(
                'Working with PDFs'
                ('Unlock PDF','Merge PDF')
     )                   

     if option_op == 'Unlock PDF':
       st.write("Unlock PDF")
       uploaded_files = st.file_uploader('Choose a PDF file', accept_multiple_files=True)
       for uploaded_file_data in uploaded_files:
          bytes_data=uploaded_file_data.read()
          st.write('filename:',uploaded_file_data.name)

          pdf_password=st.text_input("PDF password")
       unlock=st.button("Unlock PDF")
       if unlock:
           pdf=pikepdf.open(uploaded_file_data,password=pdf_password)
           pdf.save(uploaded_file_data.name)
           st.write("File is Successfully unlocked")


       
           with open(uploaded_file_data.name,'rb') as f:
              PDFbyte=f.read()
              st.download_button(label="Download",
              data=PDFbyte,
              file_name=uploaded_file_data.name)




     elif option_op == 'Merge PDF':
        st.write("Merge PDF")
        uploaded_files = st.file_uploader('Choose a PDF file', accept_multiple_files=True)
        for uploaded_file_data in uploaded_files:
          bytes_data=uploaded_file_data.read()
          st.write('filename:',uploaded_file_data.name)
        
        merge=st.button("Merge")
          
        if merge:
           merger=PdfWriter()
           for pdf in uploaded_files:
               merger.append(pdf)
               merger.write("result.pdf")
           with open('result.pdf','rb') as f:
              PDFbyte=f.read()
              st.download_button(label="Download",
              data=PDFbyte,
              file_name=uploaded_file_data.name)




if __name__ == "__main__":
     main()

