import streamlit as st
from services.auth import validate_user

def show_login():
    st.title("🔐 Login Page")

    # ---- Username / Password login ----
    username = st.text_input("Enter Username:")
    password = st.text_input("Enter Password:", type="password")

    if st.button("Login"):
        if validate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"✅ Welcome, {username}!")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")
