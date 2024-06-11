import streamlit as st

def settings():
    st.title("Settings")
    st.subheader("User Settings")
    Name = st.text_input("Name", value="Name")
    username = st.text_input("Username", value="User")
    password = st.text_input("Password", type="password", value="Password")
    if st.button("Update Settings"):
        st.write("Settings updated!")
