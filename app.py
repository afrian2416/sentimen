import hashlib
import streamlit as st
from home import home
from analysis import analysis
from history import history
from settings import settings
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
import yaml

# Helper function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Configuration for authentication
config = {
    'credentials': {
        'usernames': {
            'user1': {
                'name': 'User One',
                'password': hash_password('password')
            },
            'user2': {
                'name': 'User Two',
                'password': hash_password('password')
            }
        }
    },
    'cookie': {
        'name': 'sentiment_app',
        'key': 'random_signature_key',
        'expiry_days': 30
    }
}

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

PAGES = {
    "Home": home,
    "Analysis": analysis,
    "History": history,
    "Settings": settings
}

def main():
    # Perform authentication
    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:
        with st.sidebar:
            selected = option_menu("Main Menu", list(PAGES.keys()), 
                                   icons=['house', 'bar-chart-line', 'clock-history', 'gear'], 
                                   menu_icon="cast", default_index=0)

        page = PAGES[selected]
        page()

        # Add a logout button to the sidebar
        if st.sidebar.button('Logout'):
            authenticator.logout('Logout', 'main')
            st.experimental_rerun()

    elif authentication_status is False:
        st.error('Username/password is incorrect')

    elif authentication_status is None:
        st.warning('Please enter your username and password')

if __name__ == "__main__":
    main()
