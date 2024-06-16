import streamlit as st
from sidebar import buttons_difficulty_sidebar


if 'name' not in st.session_state:
    st.session_state.name = "Invitado"

buttons_difficulty_sidebar()

def custom_header(User, background_color):
    html_code = f"""
    <div style="background-color: {background_color}; padding: 10px; border-width:10px; border-color:#E88874;">
       <center> <img src="https://lasmasinnovadoras.com/wp-content/uploads/2023/10/arca.png"width = 300; alt="Flowers in Chania"> </center>
        <h5 style="color: maroon; text-align:right;">Bienvenido {User}</h5>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
custom_header(f"{st.session_state.name}", "fffff")

st.header("Promociones")
st.write(f"{st.session_state.name}, aquí te dejamos una promociones personalizadas para ti. Inicia sesión o crea una cuenta para acceder a ellas")

if "popover_clicked_col1" not in st.session_state:
    st.session_state.popover_clicked_col1 = False

if "popover_clicked_col2" not in st.session_state:
    st.session_state.popover_clicked_col2 = False

if "popover_clicked_col3" not in st.session_state:
    st.session_state.popover_clicked_col3 = False

def clear_col1():
    st.session_state.popover_clicked = True

def clear_col2():
    st.session_state.popover_clicked_col2 = True

def clear_col3():
    st.session_state.popover_clicked_col3 = True

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Descuentos")
    
    if not st.session_state.popover_clicked_col1:
        if st.session_state.name == "Carlos Flores":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("10% en los botellones Ciel")
        elif st.session_state.name == "Alejandro Acosta":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Descuento del 20% en todas las latas de Sprite y Fanta")
        elif st.session_state.name == "Hector Molino":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("5 pesos menos a cada botella de 2L de Coca-Cola sin azúcar")
        elif st.session_state.name == "Jessica Paz":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Descuento del 10% en todas las botellas Powerade")
        elif st.session_state.name == "Karina Torres":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("5% menos a todos los productos de Santa Clara")
        else:
            st.write("Inicie sesión para mas promociones personalizadas")
        with st.popover("Usar promocion"):
            st.markdown("Seguro que quieres usar esta promoción?")
            st.button("Si", on_click=clear_col1, key=1)
    else:
        st.write("¡Promoción utilizada exitosamente!")


with col2:
    st.subheader("Regalo")
    if not st.session_state.popover_clicked_col2:
        if st.session_state.name=="Carlos Flores":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Una lata de Coca-Cola sin azúcar por cada diez latas de Coca-Cola")
        elif st.session_state.name=="Alejandro Acosta":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Una botella Fanta de litro por cada cino bottelas de litro de Coca-Cola")
        elif st.session_state.name=="Hector Molino":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Una lata de Coca-Cola sin azúcar por cada diez latas de Coca-Cola")
        elif st.session_state.name=="Jessica Paz":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Una botella Vitamin Water de 500ml por cada six-pack de Powerade")
        elif st.session_state.name=="Karina Torres":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Seis latas Del Valle de 250ml por cada docena de Tetrapack Santa Clara de litro.")
        else:
            st.write("Inicie sesión para mas promociones personalizadas")
        with st.popover("Usar promocion"):
            st.markdown("Seguro que quieres usar esta promoción?")
            st.button("Si", on_click=clear_col2, key=2)
    else:
        st.write("¡Promoción utilizada exitosamente!")

with col3:
    st.subheader("Combo")
    if not st.session_state.popover_clicked_col3:
        if st.session_state.name=="Carlos Flores":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Combo de 8 Botellas Coca Cola de 2.0L y 24 Botellas Ceil de 235ml a $300")
        elif st.session_state.name=="Alejandro Acosta":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Combo de 12 Botellas Sprite de 1.0L y 24 botellas Fanta de 500ml a $470")
        elif st.session_state.name=="Hector Molino":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Combo de 8 Botellas Coca Cola de 2.0L y 24 Botellas Ceil de 235ml a $300")
        elif st.session_state.name=="Jessica Paz":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Combo de 6 botellas Poweradede 1.0L y 6 botellas Vitamina Water a $250 ")
        elif st.session_state.name=="Karina Torres":
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Mexico.png", width=50)
            st.write("Combo de 12 Tetrapack Del Valle de 250ml y 3 Tetrapack Santa Clara de 200ml a $100")
        else:
            st.write("Inicie sesión para mas promociones personalizadas")
        with st.popover("Usar promocion"):
            st.markdown("Seguro que quieres usar esta promoción?")
            st.button("Si", on_click=clear_col3, key=3)
    else:
        st.write("¡Promoción utilizada exitosamente!")

