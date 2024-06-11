import streamlit as st
from home import home
from analysis import analysis
from history import history
from settings import settings

PAGES = {
    "Home": home,
    "Analysis": analysis,
    "History": history,
    "Settings": settings
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
    
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
