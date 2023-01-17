import streamlit as st
with st.form(key='my_form', clear_on_submit=True):
  title_SOP=st.title('SOP Questions form')
  Question_dropdown=st.selectbox(
                                  'Enter your question',
                                ('What is Living allowance ?','What is Supplier invoice ?'))
  if Question_dropdown=="What is Living allowance ?":
    st.write("It is the file received from the payroll department, which describes the allowances that had been incurred by the employee/Expat during the secondment period. Below mentioned screenshot is for your reference")
  else
    st.text_input(label="Answer","These are the invoices which are booked by the AP for payment and data has been use for calculation of the amount to be charged")

  submit_button = st.form_submit_button(label='Submit')
