import streamlit as st

st.set_page_config(page_title="Google Search", page_icon=":mag:", layout="wide")

query = st.text_input("Enter your search query")
gl = st.selectbox("Select your country region", ("us", "uk", "fr", "de"))

st.write("Results for:", query)

results = google_search(query, num_results=10, gl=gl)

for result in results:
    st.write("- " + result.title)
