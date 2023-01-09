import streamlit as st
number1=st.number_input("Enter a number")
number2=st.number_input("Enter second number")
result=st.result_add(number1,number2)
st.write(result)
