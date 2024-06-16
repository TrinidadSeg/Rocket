import streamlit as st
import pandas as pd
import numpy as np

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


chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["Venta de productos", "Porcentaje de Ventas"])

st.line_chart(chart_data)