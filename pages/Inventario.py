import streamlit as st
import numpy as np
import pandas as pt

BaseDatos_PreciosMexico = "BaseDatos_PreciosMexico.xlsx"
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)



st.title("Tu inventario Actual")