import streamlit as st

def main():


  st.title("Simple Login App")
  menu=["Home","Login","Signup"]
  choice=st.sidebar.selectbox("Menu",menu)
  
    
  if choice=="Home":
     st.subheader("Home")


  elif choice=="Login":
     st.subheader("Login Section")

 
     username=st.sidebar.text_input("User Name")
     password=st.sidebar.text_input("Password",type=password)
     if st.sidebar.chechkbox("Login"):
          if password=='12345':
            st.success("Logged in as {}".format(Username))

            task=st.selectbox("Task",["ADD Post","Analytics","Profiles"])
            if task=="Add Post":
            st.subheader("Add Your Post")

            elif task=="Analytics":
               st.subheader("Analytics")
            elif task=="Profiles":
               st.subheader("User Profiles")
         else
            st.warning("Incorrect username/Password")
       


  elif choice=="Signup":
     st.subheader("Create New Account")
