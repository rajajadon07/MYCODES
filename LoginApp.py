import streamlit as st




st.title("Simple Login App")
menu=["Home","Login","Signup"]
choice=st.sidebar.selectbox("Menu",menu)
  
    
if choice=="Home":
     st.subheader("Home")
     st.text("Welcome USER How are you ?")


elif choice=="Login":
     st.subheader("Login Section")

 
     username=st.sidebar.text_input("User Name")
     password=st.sidebar.text_input("Password",type='password')
     if st.sidebar.checkbox("Login"):
          if password=='12345':
            
            st.success("Logged in as {}".format(username))

            task=st.selectbox("Task",["Add Post","Analytics","Profiles"])
            if task=="Add Post":
               st.subheader("Add Your Post")

            elif task=="Analytics":
               st.subheader("Analytics")
            elif task=="Profiles":
               st.subheader("User Profiles")
          else:
            st.warning("Incorrect username/Password")
       

elif choice=="Signup":
     st.subheader("Create New Account")
      
      
     
