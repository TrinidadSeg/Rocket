import streamlit as st
import pandas as pd

# Create a sample DataFrame
data = {
    'Year': [2017, 2018, 2019, 2020, 2021],
    'Alice': [24, 27, 30, 35, 40],
    'Bob': [20, 25, 29, 33, 35],
    'Charlie': [22, 24, 26, 30, 32],
    'David': [28, 29, 32, 34, 36],
    'Eve': [25, 26, 28, 31, 34]
}
df = pd.DataFrame(data)

# Display the original DataFrame
st.write("Original DataFrame:")
st.dataframe(df)

# Row selection
selected_row = st.selectbox("Select a person to plot", df.columns[1:])

# Extract data for the selected row
row_data = df[['Year', selected_row]]

# Set 'Year' as the index
row_data.set_index('Year', inplace=True)

# Plot the data as a line chart
st.write(f"Line Chart for {selected_row}:")
st.line_chart(row_data)

# Display the row data
st.write("Data for the selected row:")
st.dataframe(row_data)
