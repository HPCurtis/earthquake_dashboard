def quake_percentages(df, by):

    '''
       Calculate the percentage of categorical data 
        specified the by paramter of a dataframe.

       Returns: 
              DataFrame: Cleaned pandas dataframe of users data.  
    '''

    # Group the data by the 'Group' column
    grouped = df.groupby(by).size()

    # Calculate the size of each group
    group_sizes = grouped.reset_index(name='Count')

    #Calculate the percentage of each group
    total_count = group_sizes['Count'].sum()
    
    # Convert to integer values
    group_sizes['%'] = ((group_sizes['Count'] / total_count) * 100).astype(int)
    # Sort value in descening order then convert to string and add the '%' sign. 
    group_sizes = group_sizes[[by, '%']].sort_values(by="%", ascending=False).astype(str) + '%'
    
    return(group_sizes)

def top_10(df):

    '''
       Calculate the top of 10 magnitude of earthquake dataset 

       Returns: 
              DataFrame: pandas dataframe of top 10 magnitude earthquakes.  
    '''

    df = df[["location", "magnitude"]].sort_values(by="magnitude", ascending=False).head(10)
    return(df)

