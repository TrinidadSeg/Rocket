import streamlit as st
import numpy as np
import pandas as pd
def custom_header(User, background_color):
    html_code = f"""
    <div style="background-color: {background_color}; padding: 10px; border-width:10px; border-color:#E88874;">
       <center> <img src="https://lasmasinnovadoras.com/wp-content/uploads/2023/10/arca.png"width = 300; alt="Flowers in Chania"> </center>
        <h5 style="color: maroon; text-align:right;">Bienvenido {User}</h5>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
custom_header("Trini", "fffff")


st.write("Inventario de Productos")
image_path = "assets/Cocacola_01.png"
st.image(image_path, caption="Your Image Caption", width=300)




#st.title("Tu inventario Actual")

file = "pages/BaseDatos_PreciosMexico.xlsx"
df = pd.read_excel(file)


#x = st.slider('x')  # 👈 this is a widget

#st.write(x, 'squared is', x * x)



