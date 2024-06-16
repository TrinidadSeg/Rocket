import streamlit as st
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Function to render the DataFrame with buttons
def render_df_with_buttons(dataframe):
    for index, row in dataframe.iterrows():
        col1, col2, col3, col4 = st.columns(4)
        col1.write(row['Name'])
        col2.write(row['Age'])
        col3.write(row['City'])
        if col4.button("Click Me", key=index):
            st.session_state[f'button_clicked_{index}'] = True

# Display the original DataFrame
st.write("Original DataFrame:")
st.dataframe(df)  # Display the DataFrame

# Search bar
search_query = st.text_input("Search the DataFrame")

# Filter the DataFrame based on the search query
if search_query:
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
else:
    filtered_df = df

# Display the filtered DataFrame with buttons
st.write("Filtered DataFrame with Buttons:")
render_df_with_buttons(filtered_df)

# Display text for each button clicked
for index in range(len(df)):
    if f'button_clicked_{index}' in st.session_state and st.session_state[f'button_clicked_{index}']:
        st.text(f'Button {index} clicked!')
