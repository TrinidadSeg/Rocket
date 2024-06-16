import streamlit as st
import pandas as pt
if 'name'  not in st.session_state:
    st.session_state.name = "Usuario no definido"
if 'location' not in st.session_state:
    st.session_state.location = "Tec Digital Hub"
left, right = st.columns([3,1])
name ="tu mama"

with left:
    st.title(f"Perfil de {st.session_state.name}")

with right:
    st.image('https://cdn-icons-png.flaticon.com/512/1144/1144760.png', width=100,)

cuenta = ["", "", ""]
numero = 818188181
with st.popover("Crea tu cuenta o Inscribete"):
    name = st.text_input("Cual es tu nombre")
    email = st.text_input("Escribe tu correo electronico")
    password = st.text_input("Escribe tu contrasena")
    if name and email and password:
        if st.button("Inscribete"):
            if name == st.session_state.name:
                st.text("Ya estas dentro de esta cuenta")
            else:
                cuenta = [st.session_state.name, email, password]
                st.session_state.name = name
                st.text("Has accesado a tu cuenta exitosamente")


st.header(f"Mi ubicacion es {st.session_state.location}")
with st.expander("Deseo cambiar mi ubicacion"):
    new_location = st.text_input("Escibe tu nueva ubicacion")
    if new_location and password:
        with st.popover("Cambiar ubicacion"):
            check_password = st.text_input("Por favor escribe tu contrasena otra vez")
            if check_password == password and password:
                st.session_state.location = new_location
                st.text("Tu ubicacion ha sido cambiada exitosamente")
    else:
        if new_location: 
            st.text("Por favor accesa tu cuenta")

st.header(f"Mi numero de contacto es {numero}")
st.expander("Cambiar mi numero de telefono")
with st.expander("Deseo cambiar mi telefono"):
    new_location = st.text_input("Escibe tu nuevo numero de telefono")
    if new_location and password:
        with st.popover("Cambiar numero"):
            check_password = st.text_input("Por favor escribe tu contrasena otra vez")
            if check_password == password and password:
                st.session_state.location = new_location
                st.text("Tu numero ha sido cambiada exitosamente")
    else:
        if new_location: 
            st.text("Por favor accesa tu cuenta")


