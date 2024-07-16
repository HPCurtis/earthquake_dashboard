# import libraries
import streamlit  as st
import pandas as pd
#import plotly.express
from utility import quake_percentages, top_10

# read in the dataset for eearthqaukes from github
df = pd.read_csv("https://raw.githubusercontent.com/HPCurtis/Datasets/main/earthquake-data.csv")
df['datetime'] = pd.to_datetime(df['datetime'], format= '%d/%m/%Y %H:%M')

# Center the title using HTML and CSS
#st.markdown("<h1 style='text-align: center;'>Earthquake Tracker</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    st.title("Earthquake Analysis Dashboard")

# Create an date input.
with col2:
    selected_date = st.date_input(
        "Analysis date",
        value=df["datetime"].min(),
        min_value=df["datetime"].min(),
        max_value = df["datetime"].max()
    )

# Create columns for layout
left_column, middle_column, right_column = st.columns([3, 3, 3])


# Filter dataframe based on the selected date (considering only the date part)
df = df[df['datetime'].dt.date == pd.to_datetime(selected_date).date()]

# Display the sorted dataframe in the left column
with left_column:
    st.subheader("Top 10 Largest Earthquakes")
    st.table(top_10(df))
    # Date picker for selecting a single date

with right_column:
    st.subheader('% of Earthquakes by Continent')
    st.table(quake_percentages(df, by="location-broad"))

with middle_column:
    st.subheader('Earthquake map')
    st.map(df)