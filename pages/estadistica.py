import streamlit as st
import pandas as pd
import numpy as np
from sidebar import buttons_difficulty_sidebar

buttons_difficulty_sidebar()
ind = 9
if 'name' not in st.session_state:
    st.session_state.name = "Invitado"

if st.session_state.name == "Carlos Flores":
    ind = 0
if st.session_state.name == "Alejandro Acosta":
    ind = 1
if st.session_state.name == "Hector Molino":
    ind = 2
if st.session_state.name == "Jessica Paz":
    ind = 3
if st.session_state.name == "Karina Torres":
    ind = 4

def custom_header(User, background_color):
    html_code = f"""
    <div style="background-color: {background_color}; padding: 10px; border-width:10px; border-color:#E88874;">
       <center> <img src="https://lasmasinnovadoras.com/wp-content/uploads/2023/10/arca.png"width = 300; alt="Flowers in Chania"> </center>
        <h5 style="color: maroon; text-align:right;">Bienvenido {User}</h5>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
custom_header(f"{st.session_state.name}", "fffff")

left, right = st.columns([3,1])


# Streamlit layout

with left:
    st.header("Mis Estadisticas")
with right:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Arca_Continental_logo.svg/800px-Arca_Continental_logo.svg.png")

dataframe1 = pd.read_excel('pages/BaseDatos_Usarios.xlsx')
sales = []
columns_to_select =[1,2,3,4,5,6,7,8]
years = [1,2,3,4,5,6,7,8]
expenditure = []
st.session_state.name
for i in range(4,12):
    expenditure.append(dataframe1.iloc[ind][i])


chart_data = pd.DataFrame(
    {
        "Gastos": columns_to_select,
        "Semanas": expenditure,
        })

st.line_chart(chart_data, x="Semanas", y="Gastos")