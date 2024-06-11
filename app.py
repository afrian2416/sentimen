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
    
    # Membuat tombol untuk setiap halaman
    if st.sidebar.button("Home"):
        page = home
    elif st.sidebar.button("Analysis"):
        page = analysis
    elif st.sidebar.button("History"):
        page = history
    elif st.sidebar.button("Settings"):
        page = settings
    else:
        page = home  # Halaman default jika tidak ada tombol yang ditekan
    
    page()

if __name__ == "__main__":
    main()
