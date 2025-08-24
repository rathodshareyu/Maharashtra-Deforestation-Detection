import streamlit as st

def navbar(active_page):
    st.sidebar.title("📑 Navigation")

    if st.sidebar.button("Main Website"):
        st.session_state.page = "main"
        st.rerun()

    if st.sidebar.button("Cities"):
        st.session_state.page = "Cities"
        st.rerun()

    if st.sidebar.button("Greenery Detection"):
        st.session_state.page = "greenery"
        st.rerun()

    if st.sidebar.button("Datasets"):
        st.session_state.page = "Datasets"
        st.rerun()    

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.page = "main"
        st.rerun()
