import streamlit as st
import datetime
import streamlit as st

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

st.title("Pedidos y Calendario")

st.subheader("Lista de Pedidos")
st.write("Aquí se encuentra una lista con los pedidos futuros.")




calendario = st.date_input("¿Para cuando quieres agendar tu pedido?", datetime.date.today())
h = datetime.date.today()
st.write(h)
st.write("Tu siguiente pedido es para:", calendario)