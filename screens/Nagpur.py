import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
import os
import matplotlib.pyplot as plt
from components.navbar import navbar
from pathlib import Path

def show_Nagpur():
    navbar("Nagpur")
    try:
        # Works in normal Python execution
        BASE_DIR = Path(__file__).resolve().parent.parent
    except NameError:
        # Fallback for Streamlit Cloud where __file__ is not available
        BASE_DIR = Path.cwd()
        
    #col1, col2= st.columns(2)

    #with col1:
    st.title("Nagpur Deforestation Data")
    st.write("This is the data of deforestation in Nagpur Region.")

    #with col2:
    if st.button("⬅ Back to all Cities"):
        st.session_state.page = "Cities"
        st.rerun()
    


    # Set the title of your app
    st.title("Map of Nagpur")

    # Approximate center coordinates for Nagpur, Maharashtra
    nagpur_center_lat = 21.15
    nagpur_center_lon = 79.09

    # Generate some random data points around the center of Nagpur
    data = pd.DataFrame(
        np.random.randn(50, 2) / [50, 50] + [nagpur_center_lat, nagpur_center_lon],
        columns=['latitude', 'longitude']
    )

    # Display the map using the DataFrame
    st.map(data)

    # Get the absolute path of the project root
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # Path to the data folder
    data_path = os.path.join(BASE_DIR, "forest_data", "Nagpur")

    datasets = {
    '2019': pd.read_csv(os.path.join(data_path, "ng2019.csv")),
    '2020': pd.read_csv(os.path.join(data_path, "ng2020.csv")),
    '2021': pd.read_csv(os.path.join(data_path, "ng2021.csv")),
    '2022': pd.read_csv(os.path.join(data_path, "ng2022.csv")),
    '2023': pd.read_csv(os.path.join(data_path, "ng2023.csv")),
    '2024': pd.read_csv(os.path.join(data_path, "ng2024.csv")),
    '2025': pd.read_csv(os.path.join(data_path, "ng2025.csv"))
    }


    # Load datasets from CSV files
    #datasets = {
        #'2019': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Nagpur\ng2019.csv"),
        #'2020': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Nagpur\ng2020.csv"),
        #'2021': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Nagpur\ng2021.csv"),
        #'2022': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Nagpur\ng2022.csv"),
        #'2023': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Nagpur\ng2023.csv"),
        #'2024': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Nagpur\ng2024.csv"),
        #"2025": pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Nagpur\ng2025.csv")
    #}

    # Sidebar dataset selection
    st.sidebar.title("Select Dataset")
    selected_option = st.sidebar.selectbox("Choose a dataset:", list(datasets.keys()))
    selected_data = datasets[selected_option]


# ✅way to show HTML
    components.html(
        """
         <style>
         p {
            font-size:18px;
            color:#444444;
            line-height:1.6;
            margin:10px 0;
            padding:8px;
            background-color:#f9f9f9;
            border-left:4px solid green;
            border-radius:5px;
        }
        </style>

        <h1 style="color:green;">🌳 Nagpur Forest Data</h1>
        <p>In 2020, Nagpur had 129 kha of natural forest, extending over 13% of its land area. In 2024, it lost 128 ha of natural forest, equivalent to 35.1 kt of CO₂ emissions.</p>
        """,
        height=200,
    )

    # Build path to images folder
    img_path = os.path.join(BASE_DIR, "images", "nagpur.webp")

    # Show image
    st.image(img_path, caption="Nagpur Maharashtra")

    # Use a relative path for the image
    #st.image(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\images\nagpur.webp", caption="Nagpur Maharashtra")

    components.html(
        """
         <style>
         p {
            font-size:18px;
            color:#444444;
            line-height:1.6;
            margin:10px 0;
            padding:8px;
            background-color:#f9f9f9;
            border-left:4px solid green;
            border-radius:5px;
        }
        </style>

        <h1 style="color:brown;">Tree cover loss in Nagpur, Maharashtra, India</h1>
        <p>From 2001 to 2024, Nagpur lost 471 ha of tree cover, equivalent to a 2.6% of the 2000 tree cover area, and 222 kt of CO₂e emissions. This does not account for gains in tree cover over the same period.</p>
        """,
        height=200,
    )


    st.subheader(f"📊 Visualizations for {selected_option}")

    # ✅ Bar Chart
    #with col3:
    st.markdown("### 📊 Bar Chart")
    bar_fig = px.bar(
            selected_data, 
            x="Month", 
            y="Loss", 
            title=""
        )
    st.plotly_chart(bar_fig, use_container_width=True)


    # ✅ Line Chart
    st.markdown("### 📈 Line Chart")
    line_fig = px.line(
            selected_data, 
            x="Month",   # Replace with your actual "Year" or "City"
            y="Loss",   # Replace with "Forest_Loss" or "CO2_Emissions"
            title=""
        )
    st.plotly_chart(line_fig, use_container_width=True)

    # ✅ Pie Chart
    st.markdown("### 🥧 Pie Chart")
    pie_fig = px.pie(
            selected_data, 
            names="Month",    # category (e.g., City)
            values="Loss",  # numeric (e.g., Forest_Loss)
            title=""
        )
    st.plotly_chart(pie_fig, use_container_width=True)

    # You can write HTML again like this ⬇
    components.html(
        """
        <style>
         p {
            font-size:18px;
            color:#444444;
            line-height:1.6;
            margin:10px 0;
            padding:8px;
            background-color:#f9f9f9;
            border-left:4px solid green;
            border-radius:5px;
        }
        </style>

        <h1 style="color:brown;">Tree cover loss by dominant driver in Nagpur, Maharashtra, India</h1>
        <p>In Nagpur from 2001 to 2024, 67% of tree cover loss occurred in areas where the dominant drivers of loss resulted in deforestation.</p>
        """,
        height=200,
    )

    # You can also use st.markdown for simple HTML
    st.markdown(
        """
        <div style="background:#eef;padding:15px;border-radius:10px;margin-top:20px;">
        <h3>📢 Note:</h3>
        <p>This dashboard visualizes <b>deforestation trends</b> in Nagpur over the years.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ✅ Scatter Plot
    st.markdown("### 🔵 Scatter Plot")
    scatter_fig = px.scatter(
            selected_data, 
            x="Month",   # Replace with one numeric column
            y="Loss",  # Replace with another numeric column
            size="Loss",  # Optional: bubble size
            color="Month",   # Optional: color by category
        )
    st.plotly_chart(scatter_fig, use_container_width=True)   
    


    components.html(
    """
    <style>
        p {
            font-size:18px;
            color:#444444;
            line-height:1.6;
            margin:10px 0;
            padding:8px;
            background-color:#f9f9f9;
            border-left:4px solid green;
            border-radius:5px;
        }
        ul {
            font-size:16px;
            color:#333;
            margin-left:20px;
        }
        li {
            padding:4px 0;
        }
    </style>

    <h1 style="color:brown;">Tree cover gain in Nagpur, Maharashtra, India compared to other areas</h1>
    <p>From 2000 to 2020, Nagpur gained 4.74 kha of tree cover region-wide equal to 9.0% of all tree cover gain in Maharashtra.</p>
    <ul>
        <li>Palghar - 5.37 kha</li>
        <li>Amravati - 4.85 kha</li>
        <li>Nagpur - 4.74 kha</li>
        <li>Raigad - 3.38 kha</li>
        <li>Chandrapur - 3.09 kha</li>
    </ul>
    """,
    height=380,  # increased height so content is visible
)
    
    components.html(
    """
    <style>
        p {
            font-size:18px;
            color:#444444;
            line-height:1.6;
            margin:10px 0;
            padding:8px;
            background-color:#f9f9f9;
            border-left:4px solid green;
            border-radius:5px;
        }
        ul {
            font-size:16px;
            color:#333;
            margin-left:20px;
        }
        li {
            padding:4px 0;
        }
    </style>

    <h1 style="color:brown;">Tree Cover in Nagpur, Maharashtra, India</h1>
    <p>As of 2000, 1.8% of Nagpur land cover was tree cover with >30% canopy density.</p>
    """,
    height=150,  # increased height so content is visible
    )

    components.html(
       """
        <style>
         p {
            font-size:18px;
            color:#444444;
            line-height:1.6;
            margin:10px 0;
            padding:8px;
            background-color:#f9f9f9;
            border-left:4px solid green;
            border-radius:5px;
        }
        </style>

        <h1 style="color:green;">Natural forest in Nagpur, Maharashtra, India</h1>
        <p>As of 2020, 13% of land cover in Nagpur was natural forests and 1.1% was non-natural tree cover.</p>
        """,
        height=200,
    )

    
    # ✅ Show dataset preview below charts
    st.subheader("📑 Dataset Preview")
    st.dataframe(selected_data.head())    

        


