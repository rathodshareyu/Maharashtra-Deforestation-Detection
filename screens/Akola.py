import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import os
from components.navbar import navbar


def show_Akola():
    navbar("Akola")
    try:
        # Works in normal Python execution
        BASE_DIR = Path(__file__).resolve().parent.parent
    except NameError:
        # Fallback for Streamlit Cloud where __file__ is not available
        BASE_DIR = Path.cwd()
        
    #col1, col2= st.columns(2)

    #with col1:
    st.title("Akola Deforestation Data")
    st.write("This is the data of deforestation in Akola Region.")

    #with col2:
    if st.button("⬅ Back to all Cities"):
        st.session_state.page = "Cities"
        st.rerun()
    


    # Set the title of your app
    st.title("Map of Akola")

    # Approximate center coordinates for Akola, Maharashtra
    akola_center_lat = 20.70
    akola_center_lon = 77.01

    # Generate some random data points around the center of Akola
    data = pd.DataFrame(
        np.random.randn(50, 2) / [50, 50] + [akola_center_lat, akola_center_lon],
        columns=['latitude', 'longitude']
    )

    # Display the map using the DataFrame
    st.map(data)


    # Get the absolute path of the project root
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # Path to the data folder
    data_path = os.path.join(BASE_DIR, "forest_data", "Akola")

    datasets = {
    '2019': pd.read_csv(os.path.join(data_path, "akola2019.csv")),
    '2020': pd.read_csv(os.path.join(data_path, "akola2020.csv")),
    '2021': pd.read_csv(os.path.join(data_path, "akola2021.csv")),
    '2022': pd.read_csv(os.path.join(data_path, "akola2022.csv")),
    '2023': pd.read_csv(os.path.join(data_path, "akola2023.csv")),
    '2024': pd.read_csv(os.path.join(data_path, "akola2024.csv")),
    '2025': pd.read_csv(os.path.join(data_path, "akola2025.csv"))
    }


    # Load datasets from CSV files
    #datasets = {
        #'2019': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Akola\akola2019.csv"),
        #'2020': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Akola\akola2020.csv"),
        #'2021': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Akola\akola2021.csv"),
        #'2022': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Akola\akola2022.csv"),
        #'2023': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Akola\akola2023.csv"),
        #'2024': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Akola\akola2024.csv"),
        #"2025": pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Akola\akola2025.csv")
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

        <h1 style="color:green;">🌳 Akola Forest Data</h1>
        <p>In 2020, Akola had 0.00 ha of natural forest, extending over 0 of its land area, equivalent to 0.00 t of CO₂ emissions.</p>
        """,
        height=200,
    )

    # Use a relative path for the image
    st.image(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\images\akola.jpg", caption="Akola Maharashtra")

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

        <h1 style="color:brown;">Tree cover loss in Akola, Maharashtra, India</h1>
        <p>From 2001 to 2024, Akola lost 12 ha of tree cover, equivalent to a 9.6% of the 2000 tree cover area, and 6.00 kt of CO₂e emissions. This does not account for gains in tree cover over the same period.</p>
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

        <h1 style="color:brown;">Tree cover loss by dominant driver in Akola, Maharashtra, India</h1>
        <p>In Akola from 2001 to 2024, 100% of tree cover loss occurred in areas where the dominant drivers of loss resulted in deforestation.</p>
        """,
        height=200,
    )

    # You can also use st.markdown for simple HTML
    st.markdown(
        """
        <div style="background:#eef;padding:15px;border-radius:10px;margin-top:20px;">
        <h3>📢 Note:</h3>
        <p>This dashboard visualizes <b>deforestation trends</b> in Akola over the years.</p>
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

    <h1 style="color:brown;">Tree cover gain in Akola, Maharashtra, India compared to other areas</h1>
    <p>From 2000 to 2020, Akola gained 330 ha of tree cover region-wide equal to 0.63% of all tree cover gain in Maharashtra.</p>
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

    <h1 style="color:brown;">Tree Cover in Akola, Maharashtra, India</h1>
    <p>As of 2000, < 0.1% of Akola land cover was tree cover with >30% canopy density.</p>
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

        <h1 style="color:green;">Natural forest in Akola, Maharashtra, India</h1>
        <p>As of 2020, 0.21% of land cover in Akola was natural forests and 0.11% was non-natural tree cover.</p>
        """,
        height=200,
    )

    
    # ✅ Show dataset preview below charts
    st.subheader("📑 Dataset Preview")
    st.dataframe(selected_data.head())    

        


