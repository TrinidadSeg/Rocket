import streamlit as st
import pandas as pt
is_login = False

user_data = pt.read_excel('pages/BaseDatos_Usarios.xlsx')

def compare_user_credentials(username, email, password):
    user_row = user_data[user_data['Username'] == username]
    if not user_row.empty:
        stored_email = user_row.iloc[0]['Email']
        stored_password = user_row.iloc[0]['Password']
        if email == stored_email and password == stored_password:
           st.text("Has ingresado exitosmanete")
           is_login = True
        else:
            st.text("Nombre, correo o contraseña incorrecta")
    else:
        st.text("Usario no encontrado.")



def custom_header(User, background_color):
    html_code = f"""
    <div style="background-color: {background_color}; padding: 10px; border-width:10px; border-color:#E88874;">
       <center> <img src="https://lasmasinnovadoras.com/wp-content/uploads/2023/10/arca.png"width = 300; alt="Flowers in Chania"> </center>
        <h5 style="color: maroon; text-align:right;">Bienvenido {User}</h5>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
custom_header("Trini", "fffff")

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
column1,column2 = st.columns(2)
with column1:
    with st.popover("Crea tu cuenta o Inscribete"):
        name = st.text_input("Cual es tu nombre")
        email = st.text_input("Escribe tu correo electronico")
        password = st.text_input("Escribe tu contrasena")
        if name and email and password:
            if st.button("Inscribete"):
                if name == st.session_state.name:
                    st.text("Ya estas dentro de esta cuenta")
                else:
                    try:
                        existing_data = pt.read_excel('pages/BaseDatos_Usarios.xlsx')
                    except FileNotFoundError:
                        existing_data = pt.DataFrame(columns=['Username','Email','Password'])
                    new_row = pt.DataFrame({'Username': [name], 'Email': [email], 'Password' : [password]})
                    user_data = pt.concat([existing_data, new_row], ignore_index=True)
                    user_data.to_excel('pages/BaseDatos_Usarios.xlsx',index = False)
                    cuenta = [st.session_state.name, email, password]
                    st.session_state.name = name
                    st.text("Has accesado a tu cuenta exitosamente. Porfavor Ingrese con su cuenta")
with column2:
    with st.popover("Ingresa a su cuenta"):
        name = st.text_input("Nombre")
        email = st.text_input("Correo electronico")
        password = st.text_input("Contrasena")
        if st.button("Ingresar"):   
                user_data = pt.read_excel('pages/BaseDatos_Usarios.xlsx')    
                compare_user_credentials(name, email, password)

st.subheader(f"Mi ubicacion es {st.session_state.location}")


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

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("Mexico")
        st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)

    with col2:
        st.button("Argentina")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Flag_of_Argentina.png/1200px-Flag_of_Argentina.png", width=50)

    with col3:
        st.button("Peru")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Flag_of_Peru_%28state%29.svg/2560px-Flag_of_Peru_%28state%29.svg.png", width=50)

    with col4:
        st.button("Ecuador")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Flag_of_Ecuador.svg/2560px-Flag_of_Ecuador.svg.png", width=50)

st.subheader(f"Mi numero de contacto es {numero}")
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


