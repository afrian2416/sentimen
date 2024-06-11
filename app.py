import streamlit as st
from home import home
from analysis import analysis
from history import history
from settings import settings
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
import yaml

# Configuration for authentication
config = {
    'credentials': {
        'usernames': {
            'user': {
                'name': 'weisse',
                'password': stauth.Hasher(['password']).generate()[0]
            },
            'user2': {
                'name': 'User Two',
                'password': stauth.Hasher(['password']).generate()[0]
            }
        }
    },
    'cookie': {
        'name': 'sentiment_app',
        'key': 'random_signature_key',
        'expiry_days': 15
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
