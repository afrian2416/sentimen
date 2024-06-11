import streamlit as st
import streamlit_authenticator as stauth
import yaml

def settings():
    st.title("Settings")
    st.subheader("User Settings")
    Name = st.text_input("Name", value="Name")
    username = st.text_input("Username", value="User")
    password = st.text_input("Password", type="password", value="Password")
    if st.button("Update Settings"):
        st.write("Settings updated!")

    # Add a logout button
    authenticator = stauth.Authenticate({}, 'sentiment_app', 'random_signature_key', 30)
    if st.button('Logout'):
        authenticator.logout('Logout', 'main')
        st.experimental_rerun()
