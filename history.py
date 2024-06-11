import streamlit as st

def history():
    st.title("History")
    history_tabs = st.tabs(["Single History", "Batch History"])

    with history_tabs[0]:
        st.subheader("Single Sentiment Analysis History")
        # Placeholder for single analysis history
        st.write("No history available.")

    with history_tabs[1]:
        st.subheader("Batch Sentiment Analysis History")
        # Placeholder for batch analysis history
        st.write("No history available.")
