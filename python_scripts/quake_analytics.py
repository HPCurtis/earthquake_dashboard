
class QuakeAnalytics:

    def __init__(self):
        pass

    def quake_percentages(self, df, by):

        '''
        Calculate the percentage of categorical data 
        specified the by parameter of a dataframe.

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
        group_sizes = group_sizes[[by, '%']].sort_values(by="%", ascending=False)
        group_sizes['%'] = group_sizes['%'].astype(str) + '%'
        return(group_sizes)

    def quake_counter(self, df, by):
        '''
        Calculate the percentage of categorical data 
        specified the by parameter of a dataframe.

        Returns: 
                DataFrame: pandas dataframe of count of earth quakes
        '''

        # Group the data by the 'Group' column
        grouped = df.groupby(by).size()

        # Calculate the size of each group
        group_sizes = grouped.reset_index(name='Count')

        return(group_sizes)

    def magnitude_avg(self, df, by):
        df = df[[by,"magnitude"]]
        grouped_df = df.groupby(by).mean().reset_index()
        grouped_df["magnitude"] = grouped_df["magnitude"].round(1)
        grouped_df = grouped_df.rename(columns={by: "location", "magnitude": "avg_magnitude"})
        return(grouped_df)

    def magnitude_max(self, df, by):
        df = df[[by,"magnitude"]]
        grouped_df = df.groupby(by).max().reset_index()
        grouped_df = grouped_df.rename(columns={by: "location", "magnitude": "max_magnitude"})
        return(grouped_df)

    def top_10(self, df):
        '''
            Calculate the top of 10 magnitude of earthquake dataset 

            Returns: 
                    DataFrame: pandas dataframe of top 10 magnitude earthquakes.  
        '''

        df = df[["location", "magnitude"]].sort_values(by="magnitude", ascending=False).head(10)
        return(df)

