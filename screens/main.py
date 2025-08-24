import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from components.navbar import navbar


def show_main():
    navbar("main")
    st.set_page_config(
    page_title = "Deforestation Detection",
    page_icon = "🌳",
    )
    st.title("🌴Maharashtra Forest Watch")
    st.write(f"Hello, **{st.session_state.username}** 👋, welcome!")
    st.sidebar.success("Select a page above.")

    


    st.title("Map of Maharashtra")

    # Approximate center coordinates for Maharashtra
    maharashtra_center_lat = 19.7515
    maharashtra_center_lon = 75.7139

    # Generate random data points for cities in Maharashtra
    num_points = 50
    df = pd.DataFrame({
        "latitude": np.random.randn(num_points) / 2.5 + maharashtra_center_lat,
        "longitude": np.random.randn(num_points) / 2.5 + maharashtra_center_lon
    })

    # Display the map in Streamlit
    st.map(df)


    # Get the absolute path of the project root
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # Path to the data folder
    data_path = os.path.join(BASE_DIR, "forest_data", "Maharashtra")

    datasets = {
    '2019': pd.read_csv(os.path.join(data_path, "mh2019.csv")),
    '2020': pd.read_csv(os.path.join(data_path, "mh2020.csv")),
    '2021': pd.read_csv(os.path.join(data_path, "mh2021.csv")),
    '2022': pd.read_csv(os.path.join(data_path, "mh2022.csv")),
    '2023': pd.read_csv(os.path.join(data_path, "mh2023.csv")),
    '2024': pd.read_csv(os.path.join(data_path, "mh2024.csv")),
    '2025': pd.read_csv(os.path.join(data_path, "mh2025.csv"))
    }



    # Load datasets from CSV files
    #datasets = {
        #'2019': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Maharashtra\mh2019.csv"),
        #'2020': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Maharashtra\mh2020.csv"),
        #'2021': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Maharashtra\mh2021.csv"),
        #'2022': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Maharashtra\mh2022.csv"),
        #'2023': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Maharashtra\mh2023.csv"),
        #'2024': pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Maharashtra\mh2024.csv"),
        #"2025": pd.read_csv(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\forest_data\Maharashtra\mh2025.csv")
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

        <h1 style="color:green;">🌳 Maharashtra Forest Data</h1>
        <p>In 2020, Maharashtra had 3.43 Mha of natural forest, extending over 11% of its land area. In 2024, it lost 3.14 kha of natural forest, equivalent to 936 kt of CO₂ emissions.</p>
        """,
        height=200,
    )

    # Use a relative path for the image
    st.image(r"C:\Users\parvi\OneDrive\Documents\stream--deforestation\images\mh.webp", caption="Primary Forest Loss in Maharashtra")

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

        <h1 style="color:brown;">Primary Forest Loss</h1>
        <p>From 2002 to 2024, Maharashtra lost 882 ha of humid primary forest, making up 4.1% of its total tree cover loss in the same time period. Total area of humid primary forest in Maharashtra decreased by 1.0% in this time period.</p>
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

        <h1 style="color:brown;">🌲 Tree Cover Loss</h1>
        <p>From 2001 to 2024, Maharashtra lost 22.4 kha of tree cover, equivalent to a 2.1% of the 2000 tree cover area, and 10.8 Mt of CO₂e emissions. This does not account for gains in tree cover over the same period.</p>
        """,
        height=200,
    )

    # You can also use st.markdown for simple HTML
    st.markdown(
        """
        <div style="background:#eef;padding:15px;border-radius:10px;margin-top:20px;">
        <h3>📢 Note:</h3>
        <p>This dashboard visualizes <b>deforestation trends</b> in Maharashtra over the years.</p>
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

    <h1 style="color:brown;">Location of Tree Cover Loss in Maharashtra, India</h1>
    <p>In Maharashtra, the top 1 regions were responsible for 53% of all tree cover loss between 2001 and 2024. 
    This region had the most tree cover loss at 11.8 kha compared to an average of 659 ha.</p>
    <ul>
        <li>Gadchiroli - 11.8 kha</li>
        <li>Sindhudurg - 3.02 kha</li>
        <li>Chandrapur - 3.08 kha</li>
        <li>Gondhiya - 1.20 kha</li>
        <li>Bhandara - 1.13 kha</li>
    </ul>
    """,
    height=400,  # increased height so content is visible
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

    <h1 style="color:brown;">Location of tree cover in Maharashtra, India</h1>
    <p>In Maharashtra as of 2010, the top 1 regions represent 61% of all tree cover. Garhchiroli had the most tree cover at 532 kha compared to an average of 24.4 kha.</p>
    <ul>
        <li>Gadchiroli - 532 kha</li>
        <li>Gondiya - 67.0 kha</li>
        <li>Sindhudurg - 50.6 kha</li>
        <li>Kolhapur - 50.2 kha</li>
        <li>Satara - 26.3 kha</li>
    </ul>
    """,
    height=330,  # increased height so content is visible
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

        <h1 style="color:green;">Tree cover loss due to fires in Maharashtra, India</h1>
        <p>From 2001 to 2024, Maharashtra lost 670 ha of tree cover from fires and 21.7 kha from all other drivers of loss. The year with the most tree cover loss due to fires during this period was 2011 with 85 ha lost to fires — 4.2% of all tree cover loss for that year.</p>
        """,
        height=200,
    )

    
    # ✅ Show dataset preview below charts
    st.subheader("📑 Dataset Preview")

    st.dataframe(selected_data.head())
