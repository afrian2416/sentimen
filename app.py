import streamlit as st
from home import home
from analysis import analysis
from history import history
from settings import settings
from streamlit_option_menu import option_menu

PAGES = {
    "Home": home,
    "Analysis": analysis,
    "History": history,
    "Settings": settings
}

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login()
    else:
        with st.sidebar:
            selected = option_menu("Main Menu", list(PAGES.keys()), 
                                   icons=['house', 'bar-chart-line', 'clock-history', 'gear'], 
                                   menu_icon="cast", default_index=0,)
        
        page = PAGES[selected]
        page()

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    main()
