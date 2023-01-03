import streamlit as st
from fpdf import FPDF
import base64
import streamlit as st
import streamlit.components.v1 as components


report_text = st.text_area("Report Text")
components.html(""" <div style="text-align: center"> your-text-here </div> """ )


export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, report_text)
    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")
   

    st.markdown(html,,html1, unsafe_allow_html=True)
