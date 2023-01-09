import streamlit as st
from fpdf import FPDF
import base64
import streamlit as st
import streamlit.components.v1 as components


report_text = st.text_area( label='Enter your text Here',value='', height=300, max_chars=10000, key=None)



export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val) 
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(20, 10, report_text)
    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")
   

    st.markdown(html, unsafe_allow_html=True)
