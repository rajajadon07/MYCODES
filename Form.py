import streamlit as st
with st.form(key='my_form', clear_on_submit=True):
  title_SOP=st.title('SOP Questions form')
  def myFun(*argv):
    for arg in argv:
      st.write(arg)
  myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
                                

    
    
  submit_button = st.form_submit_button(label='Submit')
