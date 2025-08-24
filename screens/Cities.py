import streamlit as st
from components.navbar import navbar

def show_Cities():
    navbar("Cities")
    st.title("All Cities in Maharashtra")
    st.write("Click on button to open the deforestation data of cities in Maharashtra.")

    # --- First Row (3 columns) ---
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\images\Amt.webp",caption="Amravati Maharashtra")
        if st.button("➡ Amravati Data", key="btn1"):
            st.session_state.page = "Amravati"
            st.rerun()

    with col2:
        st.image(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\images\nagpur.webp",caption="Nagpur Maharashtra")
        if st.button("➡ Nagpur Data", key="btn2"):
            st.session_state.page = "Nagpur"
            st.rerun()

    with col3:
        #st.image(r"C:\Users\parvi\OneDrive\Documents\streamlit-deforest\Multipage\images\mah1.webp",caption="Back to Main")
        if st.button("⬅ Back to Main", key="btn3"):
            st.session_state.page = "main"
            st.rerun()

    # --- Second Row (3 columns) ---
    col4, col5, col6 = st.columns(3)

    with col4:
        st.image(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\images\akola.jpg",caption="Akola Maharashtra")
        if st.button("➡ Akola Data", key="btn4"):
            st.session_state.page = "Akola"
            st.rerun()

    with col5:
        st.image(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\images\yml.jpg",caption="Yavatmal Amravati")
        if st.button("➡ Yavatmal Data", key="btn5"):
            st.session_state.page = "Yavatmal"
            st.rerun()

    with col6:
        st.image(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\images\arg.webp",caption="Aurangabad amravati")
        if st.button("⬅ Aurangabad Data", key="btn6"):
            st.session_state.page = "Aurangabad"
            st.rerun()
