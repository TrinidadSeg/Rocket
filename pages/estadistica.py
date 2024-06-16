import streamlit as st
import pandas as pd
import numpy as np
from sidebar import buttons_difficulty_sidebar

buttons_difficulty_sidebar()

if 'name' not in st.session_state:
    st.session_state.name = "Invitado"


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
st.dataframe(dataframe1)
sales = []
columns_to_select =['Semana1', 'Semana2','Semana3','Semana4','Semana5','Semana6','Semana7','Semana8',]
smaller_df = dataframe1[columns_to_select]

row_data = dataframe1['Carlos Flores']
st.line_chart(row_data)


chart_data = pd.DataFrame(list, columns=["Venta de productos", "Porcentaje de Ventas"])

st.line_chart(chart_data)