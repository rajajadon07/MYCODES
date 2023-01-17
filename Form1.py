import streamlit as st
with st.form(key='Form' , clear_on_submit=True):
 temp=15
 while temp>0:
   Question_enter=st.write('question')
   text_input = st.selectbox(label='some text',key=temp)
   temp=temp-1
       
        
         
 submit_button = st.form_submit_button(label='Submit')

 
