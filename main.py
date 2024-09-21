import streamlit as st
import pandas as pd

# # Set page configuration and hide headers/footers
st.set_page_config(page_title="Data Transformer", layout="wide", initial_sidebar_state="collapsed")
hide_decoration_bar_style = '''<style>header {visibility: hidden;}
</style><style>footer{visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# <style> .main {overflow: hidden} </style>
with st.container(border =True):
    cola,colb,colc = st.columns([0.4,0.4,0.2],gap="medium")
    with cola:
        st.title("Data Exploration")
        st.write("Data exploration in the context of machine learning refers to the initial phase of analyzing a dataset to understand its structure, characteristics, and underlying patterns before building any predictive models. This step is crucial because it helps to identify important insights, detect anomalies, and determine the best approach for preparing the data for modeling.")
    with colb:
        st.header("The Explorer's Guide")
        st.write("Imagine you're in a dungeon, searching for valuable information. You stumble upon two old maps that seem incomplete individually.")
    with colc:
        st.image("_2ab7699c-321f-42d0-bff2-68c186ce3568.jpeg")

col1, col2 = st.columns(2)

with col1:
    with st.container(border =True):
        # Upload file for DataFrame 1
        uploaded_file1 = st.file_uploader("Upload your first CSV data", type=["csv"])
        if uploaded_file1 is not None:
            df1 = pd.read_csv(uploaded_file1)
            st.subheader("First Dataset Preview:")
            st.dataframe(df1)
        else:
            st.error("Please upload the first CSV file.")
            df1 = pd.DataFrame()
with col2:
    with st.container(border =True):
        # Upload file for DataFrame 2
        uploaded_file2 = st.file_uploader("Upload your second CSV data", type=["csv"])
        if uploaded_file2 is not None:
            df2 = pd.read_csv(uploaded_file2)
            st.subheader("Second Dataset Preview:")
            st.dataframe(df2)
        else:
            st.error("Please upload the second CSV file.")
            df2 = pd.DataFrame()


# Proceed only if both files are uploaded
if not df1.empty and not df2.empty:
    with st.container(border =True):
        cola,colb,colc = st.columns([0.4,0.4,0.2],gap="medium")
        with cola:
            st.header("Table Joins :")
            st.write('Table joins are operations in relational databases used to combine data from two or more tables based on a related column, often referred to as a "key." Joins allow you to query and analyze data that is spread across multiple tables by merging relevant records into a single dataset.')
        with colb:
            st.header("Merging the Maps: Uniting Clues for a Clearer Path")
            st.write("Upon closer inspection, you notice that both maps share similar symbols or landmarks, so you decide to join them. This process represents table joins, where you merge two separate pieces of information (tables) based on common elements (keys) to get a more complete view of the world (data).")

        with colc:
            st.image("join.jpeg")

    with st.container(border =True):

    # Select join type
        join_type = st.selectbox(
            "Select Join Type",
            ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"]
        )

        # Select columns for joining (if not doing a CROSS JOIN)
        if join_type != "CROSS JOIN":
            # Get list of columns for each dataframe
            df1_columns = df1.columns.tolist()
            df2_columns = df2.columns.tolist()

            # User selects the columns to join on
            col1 = st.selectbox("Select column from Table 1 to join on", df1_columns)
            col2 = st.selectbox("Select column from Table 2 to join on", df2_columns)
        else:
            col1, col2 = None, None  # No need for columns in CROSS JOIN

        # Perform the join based on the selected options
        if join_type == "INNER JOIN":
            result = pd.merge(df1, df2, left_on=col1, right_on=col2, how='inner')
        elif join_type == "LEFT JOIN":
            result = pd.merge(df1, df2, left_on=col1, right_on=col2, how='left')
        elif join_type == "RIGHT JOIN":
            result = pd.merge(df1, df2, left_on=col1, right_on=col2, how='right')
        elif join_type == "FULL OUTER JOIN":
            result = pd.merge(df1, df2, left_on=col1, right_on=col2, how='outer')

        st.write(f"**Result of {join_type}:**")
        st.dataframe(result)

    with st.container(border =True):
        cola,colb,colc = st.columns([0.4,0.4,0.2],gap="medium")
        with cola:
            st.header("Aggregate Results :")
            st.write("Aggregate results in databases refer to the summary statistics or computations performed on a set of values, returning a single result for each group of data. These operations are crucial for summarizing large datasets, providing insights by computing metrics such as sums, averages, counts, or other statistical values.")
        with colb:
            st.header("Unveiling Insights: The Power of Aggregate Results")
            st.write("Once the maps are joined, you start carefully analyzing the connections between different landmarks, identifying patterns and drawing insights. This part is similar to aggregating data, where you look for trends or important relationships by summarizing data—like counting treasures in each section of the dungeon or finding the most traveled routes.")


        with colc:
            st.image("aggregate.jpeg")
    col11,col22 = st.columns(2)
    with col11:
        with st.container(border =True):
            st.subheader("For table 1 :")
            df1_results = df1.describe()
            st.dataframe(df1_results)
    with col22:
        with st.container(border =True):
            st.subheader("For table 2 :")
            df2_results = df2.describe()
            st.dataframe(df2_results)

    with st.container(border =True):
        cola,colb,colc = st.columns([0.4,0.4,0.2],gap="medium")
        with cola:
            st.header("Window Functions :")
            st.write('Window functions are advanced tools used in data analysis to perform calculations across a subset of data, referred to as a "window," while preserving individual records. Unlike standard aggregation methods that summarize entire datasets into a single result for each group, window functions allow you to compute values like running totals, ranks, and comparisons without collapsing the underlying data.')

        with colb:
            st.header("Navigating the Details: Unearthing Insights with Window Functions")
            st.write("But you're not done yet. To truly understand the dungeon, you begin reviewing the detailed paths across different sections of the map—comparing one path to the next, tracing routes from one point to another. This mirrors the role of window functions, where you analyze data row by row, comparing each element with its neighbors to extract deeper insights, such as tracking how treasure accumulates or how paths rank against each other. ")

        with colc:
            st.image("window.jpeg")
    with st.container(border =True):

        # Choose window function
        operation = st.selectbox(
            "Select Window Function",
            ["ROW_NUMBER", "RANK", "LAG", "LEAD"]
        )

        # Select the column to perform the operation on
        column = st.selectbox("Select the column to apply the function on", df1.columns)

        # Optional: Select a column for grouping (partitioning) if necessary
        partition_col = st.selectbox("Select a column for partitioning (optional)", [None] + df1.columns.tolist())
        col111,col222 = st.columns(2)

        with col111:
            if operation == "ROW_NUMBER":
                if partition_col:
                    df1['row_number'] = df1.groupby(partition_col).cumcount() + 1
                else:
                    df1['row_number'] = df1.reset_index().index + 1
                st.write("Result after applying ROW_NUMBER():")
                st.dataframe(df1)

            elif operation == "RANK":
                if partition_col:
                    df1['rank'] = df1.groupby(partition_col)[column].rank(ascending=False, method='min')
                else:
                    df1['rank'] = df1[column].rank(ascending=False, method='min')
                st.write("Result after applying RANK():")
                st.dataframe(df1)

            elif operation == "LAG":
                if partition_col:
                    df1['lag'] = df1.groupby(partition_col)[column].shift(1)
                else:
                    df1['lag'] = df1[column].shift(1)
                st.write("Result after applying LAG():")
                st.dataframe(df1)

            elif operation == "LEAD":
                if partition_col:
                    df1['lead'] = df1.groupby(partition_col)[column].shift(-1)
                else:
                    df1['lead'] = df1[column].shift(-1)
                st.write("Result after applying LEAD():")
                st.dataframe(df1)
        with col222:
            if operation == "ROW_NUMBER":
                if partition_col:
                    df2['row_number'] = df2.groupby(partition_col).cumcount() + 1
                else:
                    df2['row_number'] = df2.reset_index().index + 1
                st.write("Result after applying ROW_NUMBER():")
                st.dataframe(df2)

            elif operation == "RANK":
                if partition_col:
                    df2['rank'] = df2.groupby(partition_col)[column].rank(ascending=False, method='min')
                else:
                    df2['rank'] = df2[column].rank(ascending=False, method='min')
                st.write("Result after applying RANK():")
                st.dataframe(df2)

            elif operation == "LAG":
                if partition_col:
                    df2['lag'] = df2.groupby(partition_col)[column].shift(1)
                else:
                    df2['lag'] = df2[column].shift(1)
                st.write("Result after applying LAG():")
                st.dataframe(df2)

            elif operation == "LEAD":
                if partition_col:
                    df2['lead'] = df2.groupby(partition_col)[column].shift(-1)
                else:
                    df2['lead'] = df2[column].shift(-1)
                st.write("Result after applying LEAD():")
                st.dataframe(df2)

    with st.container(border =True):
        cola,colb,colc = st.columns([0.4,0.4,0.2],gap="medium")
        with cola:
             st.header("Dates :")
             st.write('In data exploration, handling dates effectively allows for meaningful temporal analysis, such as identifying trends and seasonality. Converting date columns to datetime objects enables easy extraction of components (year, month, day) and facilitates filtering and resampling. Proper date manipulation enhances insights into patterns over time, making it crucial for time series analysis.')
        with colb:
            st.header("Sands of time")
            st.write("You notice dates etched into the corners, marking significant events and discoveries. You start sorting the information by these dates, revealing a timeline of events that uncovers trends in path popularity over time. This reflects the data exploration phase, where organizing temporal data helps identify patterns and relationships, guiding deeper insights and understanding for your journey ahead.")
        with colc:
            st.image("time.jpeg")
    with st.container(border=True):

        col1111,col2222 = st.columns(2)
        with col1111:
            date_col1 = st.selectbox("select the date column if any", df1.columns)
            df1[date_col1] = pd.to_datetime(df1[date_col1])
            x,y = df1[date_col1].min(), df1[date_col1].max()
            st.write(f"min = {x}, max = {y}")
            st.write("Date Info added to table")
            df1['year'] = df1[date_col1].dt.year
            df1['month'] = df1[date_col1].dt.month
            df1['day'] = df1[date_col1].dt.day
            df1['weekday'] = df1[date_col1].dt.weekday
            st.dataframe(df1)
        with col2222:
            date_col2 = st.selectbox("select the date column if any", df2.columns)
            df2[date_col2] = pd.to_datetime(df2[date_col2])
            s, t = df2[date_col2].min(), df2[date_col2].max()
            st.write(f"min = {x}, max = {y}")
            st.write("Date Info added to table")
            df2['year'] = df2[date_col2].dt.year
            df2['month'] = df2[date_col2].dt.month
            df2['day'] = df2[date_col2].dt.day
            df2['weekday'] = df2[date_col2].dt.weekday
            st.dataframe(df2)

else:
    st.warning("Please upload both CSV files to proceed.")
