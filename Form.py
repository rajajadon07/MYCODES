import streamlit as st
with st.form(key='my_form'):
       temp=15
       while temp>0:
         Question_enter=st.write('question')
         text_input = st.text_area()
         temp=temp-1
       
        
         
       submit_button = st.form_submit_button(label='Submit')
