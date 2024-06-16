import streamlit as st
import datetime

st.title("Pedidos y Calendario")

st.subheader("Lista de Pedidos")
st.write("Aquí se encuentra una lista con los pedidos futuros.")




calendario = st.date_input("¿Para cuando quieres agendar tu pedido?", datetime.date.today())
h = datetime.date.today()
st.write(h)
st.write("Tu siguiente pedido es para:", calendario)