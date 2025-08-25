import streamlit as st
from services.auth import validate_user, register_user
from streamlit_oauth import OAuth2Component

# 👉 Replace with your credentials from Google Cloud Console
CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"
CLIENT_SECRET = "YOUR_GOOGLE_CLIENT_SECRET"
AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
REDIRECT_URI = "http://localhost:8501"  # Change to your deployed Streamlit app URL

oauth2 = OAuth2Component(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    authorize_endpoint=AUTHORIZE_URL,
    token_endpoint=TOKEN_URL,
    redirect_uri=REDIRECT_URI,
    scope="openid email profile"
)

def show_login():
    st.title("🔐 Login / Register")

    # --- Tabs for Login and Registration ---
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
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

        st.write("----")
        st.subheader("🔑 Or Sign in with Google")

        if st.button("Sign in with Google"):
            result = oauth2.authorize_button("Sign in with Google")
            if result:
                st.session_state.logged_in = True
                st.session_state.username = result["userinfo"]["email"]
                st.success(f"✅ Logged in as {st.session_state.username}")
                st.rerun()

    with tab2:
        st.subheader("📝 Create New Account")
        new_username = st.text_input("Choose a Username:")
        new_password = st.text_input("Choose a Password:", type="password")
        confirm_password = st.text_input("Confirm Password:", type="password")

        if st.button("Register"):
            if new_password != confirm_password:
                st.error("❌ Passwords do not match")
            elif register_user(new_username, new_password):
                st.success("✅ Registration successful! Please login now.")
            else:
                st.error("⚠️ Username already exists")
