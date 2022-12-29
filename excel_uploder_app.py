import streamlit as st 
import pandas as pd  
import plotly.express as px



st.set_page_config(page_title='Excel Plotter')
st.title('Excel Plotter')
st.subheader('Feed me with your Excel file')

uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    groupby_column = st.selectbox(
        'What would you like to analyse?',
        ('Ship Mode', 'Segment', 'Category', 'Sub-Category'),
    )
       
   fig = px.bar(
       x=groupby_column,
       y='Sales'
   )
   st.plotly_chart(fig)

   
