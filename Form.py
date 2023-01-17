import streamlit as st
with st.form(key='my_form', clear_on_submit=True):
  title_SOP=st.title('SOP Questions form')
  Question_enter=st.input("text")
  text_input = st.text_input(label='please enter your answer')
  submit_button = st.form_submit_button(label='Submit')
