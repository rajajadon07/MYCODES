import streamlit as st
form=st.form(key='form')
temp=15
while temp>0:
  Question_enter=form.write('question')
  text_input = form.text_area()
  temp=temp-1
       
        
         
submit_button = st.form_submit_button(label='Submit')
