import streamlit as st
import pandas as pd
import os
from components.navbar import navbar

def show_Datasets():
    navbar("Datasets")
    st.title("Maharashtra Deforestation Data")


    # Get project root directory (folder where app.py lives)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # --- Sub Page 1 ---
    col1, col2 = st.columns([1,2])
    with col1:
        st.title("Data Analysis")
    with col2:
        # Build correct image path
        img_path = os.path.join(BASE_DIR, "images", "mh.webp")

        # Display image
        st.image(img_path, caption="Primary Forest Loss in Maharashtra")

        

    df = pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Maharashtra\MH-combine.csv")

    # Show only the first 10 rows
    st.subheader("CSV Preview (first 10 rows)")
    st.dataframe(df.head(10))

    # Optionally show dataset info
    st.write("Shape:", df.shape)
    st.write("Columns:", df.columns.tolist())
    st.write("State:", df.State.unique())
    st.write("Null Values:", df.isnull().sum())

    st.write("Month:", df.Month.unique())
