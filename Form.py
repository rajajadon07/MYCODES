import streamlit as st
with st.form(key='my_form', clear_on_submit=True):
  title_SOP=st.title('SOP Questions form')
  def myFun(*argv):
    for arg in argv:
      st.write(arg)
  myFun('What is Living allowance ?', 'What is Supplier invoice ?')
  
  input_question=st.input_text()
  if arg==What is Living allowance ?:
     input_question='What is Living allowance ?'
     answer=st.input_text('It is the file received from the payroll department, which describes the allowances that had been incurred by the employee/Expat during the secondment period. Below mentioned screenshot is for your reference')
  else:
    input_question='What is Supplier invoice ?'
    answer='These are the invoices which are booked by the AP for payment and data has been used for calculation of the amount to be charged'

    
    
  submit_button = st.form_submit_button(label='Submit')
