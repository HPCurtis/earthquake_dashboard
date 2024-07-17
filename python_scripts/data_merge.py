import pandas as pd

def merge_df(df, QA):
    #
    max_df = QA.magnitude_max(df, by = "location")
    count_df = QA.quake_counter(df, by = "location")
    avg_df = QA.magnitude_avg(df, by = "location")
    # Merging max_df and count_df on the 'location' column
    merged_df = pd.merge(max_df, count_df, on='location')

    # Merging the resulting dataframe with avg_df on the 'location' column
    final_df = pd.merge(merged_df, avg_df, on='location')
    
    return(final_df)
