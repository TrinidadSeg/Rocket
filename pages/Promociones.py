import streamlit as st
def custom_header(User, background_color):
    html_code = f"""
    <div style="background-color: {background_color}; padding: 10px; border-width:10px; border-color:#E88874;">
       <center> <img src="https://lasmasinnovadoras.com/wp-content/uploads/2023/10/arca.png"width = 300; alt="Flowers in Chania"> </center>
        <h5 style="color: maroon; text-align:right;">Bienvenido {User}</h5>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
custom_header("Trini", "fffff")

st.header("Promociones")


col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Descuento")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)


with col2:
    st.subheader("Regalo")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Flag_of_Argentina.png/1200px-Flag_of_Argentina.png", width=50)

with col3:
    st.subheader("Combo")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Flag_of_Peru_%28state%29.svg/2560px-Flag_of_Peru_%28state%29.svg.png", width=50)