import streamlit as st
import numpy as np
import pandas as pd


st.write("Inventario de Productos")
image_path = "pages/Cocacola_01.png"
st.image(image_path, caption="Your Image Caption", width=300)




#st.title("Tu inventario Actual")

file = "pages/BaseDatos_PreciosMexico.xlsx"
df = pd.read_excel(file)


#x = st.slider('x')  # 👈 this is a widget

#st.write(x, 'squared is', x * x)



