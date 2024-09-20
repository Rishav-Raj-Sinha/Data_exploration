import streamlit as st
import pandas as pd

# # Set page configuration and hide headers/footers
# st.set_page_config(page_title="Data Transformer", layout="wide", initial_sidebar_state="collapsed")
# hide_decoration_bar_style = '''<style>header {visibility: hidden;}
# </style><style>footer{visibility: hidden;}</style>'''
# st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# <style> .main {overflow: hidden} </style>
with st.container(border =True):
    cola,colb = st.columns([0.8,0.2],vertical_alignment="center")
    with cola:
        st.title("Data Exploration")
    with colb:
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
        cola,colb = st.columns([0.8,0.2],vertical_alignment="center")
        with cola:
            st.header("Table Joins :")
        with colb:
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


        # Display the result
        st.write(f"**Result of {join_type}:**")
        st.dataframe(result)

    with st.container(border =True):
        cola,colb = st.columns([0.8,0.2],vertical_alignment="center")
        with cola:
            st.header("Aggregate Results :")
        with colb:
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
        cola,colb = st.columns([0.8,0.2],vertical_alignment="center")
        with cola:
            st.header("Window Functions :")
        with colb:
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
            # Apply the selected operation
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
            # Apply the selected operation
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


else:
    st.warning("Please upload both CSV files to proceed.")
