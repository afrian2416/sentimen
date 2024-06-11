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
    with st.sidebar:
        selected = option_menu("Main Menu", list(PAGES.keys()), 
                               icons=['house', 'chart-line', 'history', 'gear'], 
                               menu_icon="cast", default_index=0)
        
    page = PAGES[selected]
    page()

if __name__ == "__main__":
    main()
