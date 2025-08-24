import streamlit as st
from views import login
from screens import Cities, greenery, main,Datasets,Amravati, Nagpur, Akola, Aurangabad, Yavatmal

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "page" not in st.session_state:
    st.session_state.page = "main"

if not st.session_state.logged_in:
    login.show_login()
else:
    if st.session_state.page == "main":
        main.show_main()
    elif st.session_state.page == "Cities":
        Cities.show_Cities()
    elif st.session_state.page == "greenery":
        greenery.show_greenery()
    elif st.session_state.page == "Amravati":
        from screens import Amravati
        Amravati.show_Amravati()
    elif st.session_state.page == "Nagpur":
        from screens import Nagpur
        Nagpur.show_Nagpur()
    elif st.session_state.page == "Akola":
        from screens import Akola
        Akola.show_Akola()
    elif st.session_state.page == "Yavatmal":
        from screens import Yavatmal
        Yavatmal.show_Yavatmal()
    elif st.session_state.page == "Aurangabad":
        from screens import Aurangabad
        Aurangabad.show_Aurangabad()                    

    elif st.session_state.page == "Datasets":
        Datasets.show_Datasets()