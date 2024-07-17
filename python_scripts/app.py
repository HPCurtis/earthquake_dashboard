# import libraries
import streamlit  as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from quake_analytics import QuakeAnalytics
from data_merge import merge_df

QA = QuakeAnalytics()

# Read in the dataset for earthqaukes from github
df = pd.read_csv("../data/earthquake-data.csv")
df['datetime'] = pd.to_datetime(df['datetime'], format= '%d/%m/%Y %H:%M')

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
left_column_u, middle_column_u, right_column_u = st.columns([3, 4, 3])

# Filter dataframe based on the selected date (considering only the date part)
df = df[df['datetime'].dt.date == pd.to_datetime(selected_date).date()]

# Display the sorted dataframe in the left column
with left_column_u:
    st.subheader("Top 10 Largest Earthquakes")
    st.table(QA.top_10(df))
    # Date picker for selecting a single date

with middle_column_u:
    st.subheader('Earthquake map')
    st.map(df)

with right_column_u:
    st.subheader('% of Earthquakes by Continent')
    st.table(QA.quake_percentages(df, by="location-broad"))

st.subheader("Eathquake Frequency and Magnitude Analytics")

# Create columns for layout
left_column_l, middle_column_l, right_column_l = st.columns([3, 3, 3])

with left_column_l:
    # Get user input for plotting adaption.
    sorting_option = st.selectbox(
        "Location",
        options=["Alphabetical", "Source order"],
        index=0
    )
# Check use input to change output of plot.
if sorting_option == "Alphabetical":  
   df = merge_df(df, QA)
   df = df.sort_values(by="location", ascending=False).reset_index(drop=True)
   print(df)
else:
    df = merge_df(df, QA) 


fig = make_subplots(rows=1, cols=3, specs=[[{}, {}, {}]], shared_xaxes=False,
                    shared_yaxes=True, vertical_spacing=0.001)

fig.append_trace(go.Bar(
    x=df["Count"],
    y=df["location"],
    orientation='h',
),  row=1, col=1)

fig.append_trace(go.Bar(
    x=df["avg_magnitude"],
    y=df["location"],
    orientation='h',
),  row=1, col=2)

fig.append_trace(go.Bar(
    x=df["max_magnitude"],
    y=df["location"],
    orientation='h',
),  row=1, col=3)

# Update figure layout.
fig.update_layout(
    showlegend=False,  # Disable legend for the entire figure
    height=400,
    width=800,
    xaxis_title="Count of earthquakes",  # X-axis title for the first subplot
    xaxis2_title="AVG. Magnitude", 
    xaxis3_title="MAX. Magnitude" 
)

with st.container():
    st.plotly_chart(fig, use_container_width=True)
