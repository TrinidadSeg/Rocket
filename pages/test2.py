print("Hello World")
import streamlit as st
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Function to create HTML buttons
def create_html_button(index):
    return f'<button onclick="alert(\'Button {index} clicked\')">Click Me</button>'

# Add a column with buttons to the DataFrame
df['Action'] = df.index.map(lambda x: create_html_button(x))

# Function to render the DataFrame with buttons
def render_df_with_buttons(dataframe):
    # Convert DataFrame to HTML
    html = dataframe.to_html(escape=False)
    # Render the HTML in Streamlit
    st.markdown(html, unsafe_allow_html=True)

# Display the original DataFrame
st.write("Original DataFrame:")
st.dataframe(df.drop(columns=['Action']))  # Display without the buttons column for comparison

# Display the DataFrame with buttons
st.write("DataFrame with Buttons:")
render_df_with_buttons(df)
