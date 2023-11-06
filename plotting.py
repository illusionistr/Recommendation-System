import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)  # Use pd.read_excel for Excel files
    st.write("Data Preview:")
    st.write(data.head())

    selected_columns = st.multiselect("Select columns to plot", data.columns)

if selected_columns:
    plot_type = st.selectbox("Select plot type", ["bar", "scatter", "line"])

    if plot_type == "bar":
        st.subheader("Bar Plot")
        x_column = st.selectbox("Select x-axis column", selected_columns)
        y_column = st.selectbox("Select y-axis column", selected_columns)

        if st.button("Generate Bar Plot"):
            st.pyplot(sns.barplot(x=x_column, y=y_column, data=data))

    elif plot_type == "scatter":
        st.subheader("Scatter Plot")
        x_column = st.selectbox("Select x-axis column", selected_columns)
        y_column = st.selectbox("Select y-axis column", selected_columns)

        if st.button("Generate Scatter Plot"):
            st.pyplot(sns.scatterplot(x=x_column, y=y_column, data=data))

    elif plot_type == "line":
        st.subheader("Line Plot")
        x_column = st.selectbox("Select x-axis column", selected_columns)
        y_column = st.selectbox("Select y-axis column", selected_columns)

        if st.button("Generate Line Plot"):
            st.pyplot(sns.lineplot(x=x_column, y=y_column, data=data))


if __name__ == '__main__':
    st.title("Data Visualizer")
    main()
