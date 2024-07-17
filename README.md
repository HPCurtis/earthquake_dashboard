# Earthquake Tracking Dashboard Streamlit

In this project 30 days of raw earthquake data is being visualised using a dashboard using the streamlit ecosystem of application generation.

## Project file structure

- **README.md**: The file you are currently reading.
- **data**: Contains 30 days of earthquake data stored in a CSV file.
  - `earthquake_data.csv`: The CSV file with earthquake data.
- **python_scripts**: Contains all the Python scripts used in the project.
  - `app.py`: Streamlit application to creat dashboard of earthquake data to clients specifications.
  - `quake_analytics.py`: script contains the QuakeAnalytics class for defining anakytical function for absrtation out of the streamlit app script.
  - `data_merge.py`: contains python code for merging of dataframe for plot generation. Potential for refactoring into plotting class. 

# Overview

## Context
A client has requested an earthquake tracking dashboard for insight generation from 30 days of global Earthquake data. The client requested that:

- It must have a map showing where Earthquakes took place, and this also needs to show their magnitude.
- It must have a list of the top 10 biggest earthquakes.
- It must have a breakdown of the percentage of earthquakes that occurred, by continent.
- For more granular locations, it must show how many earthquakes took place, the average magnitude and the maximum magnitude.
We need all these elements on one dashboard so that we can easily see patterns. They all need to be attached to the same date filter, where we can track earthquakes day by day, and have the ability to view the data one day at a time.

## Results

A fast response-time application interactive dashboard to present the data the client requested.

Looking at our analysis, we can quickly see that over the 30 day period:

- The Philippines had the biggest earthquake, followed by Chile and Oklahoma.
- However, the locations with the largest earthquakes on average were Samoa, Svalbard & Jan Mayen, and Vanuatu
- Most of the earthquakes were in North America by a large margin
- At a more granular level, Puerto Rico, Hawaii and Alaska had the most frequent earthquakes.
- Visually we can see the earthquake fault lines on the map

[use dashboard here](https://hpcurtis-earthquake-dashboard-python-scriptsapp-5mt9wm.streamlit.app/)
