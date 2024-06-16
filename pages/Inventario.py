import streamlit as st
import pandas as pd
from sidebar import buttons_difficulty_sidebar

#Sidebar
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = 'Easy'

buttons_difficulty_sidebar()

df = pd.read_excel('pages/BaseDatos_PreciosMexico.xlsx')

def create_html_button(index):
    return f'<button style="background-color: red; color:white; border-width: 0px; border-radius:10px" onclick="alert(\'Button {index} clicked\')"><b>Agregar al Carrito</b></button>'

def render_df_with_buttons(dataframe, keyMod):
    for index, row in dataframe.iterrows():
        col1, col2, col3 = st.columns([3, 1, 1])
        col1.write(row['Material.1'])
        col2.write(row['Precio Final'])
        if col3.button("Agregar al Carrito", key=index+keyMod):
            st.session_state[f'button_clicked_{index}'] = True

if 'name' not in st.session_state:
    st.session_state.name = "Invitado"








def custom_header(User, background_color):
    html_code = f"""
    <div style="background-color: {background_color}; padding: 10px; border-width:10px; border-color:#E88874;">
       <center> <img src="https://lasmasinnovadoras.com/wp-content/uploads/2023/10/arca.png" width="300" alt="Flowers in Chania"> </center>
        <h5 style="color: maroon; text-align:right;">Bienvenido {User}</h5>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

custom_header(f"{st.session_state.name}", "fffff")




if st.session_state.difficulty=="Hard":
    tab1, tab2 = st.tabs(["Palabras Claves", "Escribir"])
    with tab1: 
        st.write("Selecciona las palabras clave ara filtrar los productos que quiera pedir y agregar al carrito")
        keywords_options = ['Coca-Cola', 'Fanta', 'Joya', 'Sprite', 'Light', 
                            'Ciel', 'Fresca', 'Manzana Lift', 'Sidral', 'Powerade', 'Dell Valle', 
                            'Frutsi', 'Vitamin', 'Floria', 'Fuze Tea', 'Toronja']
        keywords = st.multiselect('Nombre', keywords_options, default=['Coca-Cola', 'Fanta', 'Joya'])

        keywords2_options = ['VID', 'PET', 'LAT']
        keywords2 = st.multiselect('Envase', keywords2_options, default=['VID', 'PET', 'LAT'])

        keywords3_options = ['192 ML', '355 ML', "473 ML","500ML", '1.00 L', "1.50 L", "2.00 L", "2.50 L", '5.00 L', "20.00 L"]
        keywords3 = st.multiselect('Litros', keywords3_options, default=[])

        if keywords or keywords2 or keywords3:
            filtered_df = df.copy()  # Start with a copy of the original DataFrame
            if keywords:
                filtered_df = filtered_df[filtered_df['Material.1'].str.contains('|'.join(keywords), case=False)]
            if keywords2:
                filtered_df = filtered_df[filtered_df['Material.1'].str.contains('|'.join(keywords2), case=False)]
            if keywords3:
                filtered_df = filtered_df[filtered_df['Material.1'].str.contains('|'.join(keywords3), case=False)]
        else:
            filtered_df = df.copy() 



        st.write("Productos Filtrados")
        render_df_with_buttons(filtered_df, 0)

        for index in range(len(filtered_df)):
            if f'button_clicked_{index}' in st.session_state and st.session_state[f'button_clicked_{index}']:
                st.text(f'Producto {index} Agregado!')

        # Display shopping cart
        if 'cart' not in st.session_state:
            st.session_state.cart = []

        st.header("Carrito de Compras")
        if st.session_state.cart:
            total = 0
            for item in st.session_state.cart:
                st.write(f"{item['name']} - ${item['price']}")
                total += float(item['price'])
            st.write(f"**Total: ${total:.2f}**")
        else:
            st.write("Tu carrito está vacío.")

        # Clear cart button
        if st.button("Limpiar Carrito", key = 6968):
            st.session_state.cart = []

        # Purchase button (mock functionality)
        if st.button("Compra tu carrito", key = 6969):
            if st.session_state.cart:
                st.success("Compra Exitosa!")
                st.session_state.cart = []
            else:
                st.error("Tu carrito está vacío")
    
    with tab2:
        search_query = st.text_input("Buscar en la base de datos", '')

        # Filter the DataFrame based on the search query
        if search_query:
            filtered_df = df[df['Material.1'].str.contains(search_query, case=False)]
        else:
            filtered_df = df.copy()  # If no search query, use the original DataFrame

        # Display filtered DataFrame with buttons
        st.write("Filtered DataFrame with Buttons:")
        render_df_with_buttons(filtered_df,1000)

        
        # Display text for each button clicked
        for index in range(len(filtered_df)):
            if f'button_clicked_{index}' in st.session_state and st.session_state[f'button_clicked_{index}']:
                st.text(f'Producto {index} Agregado!')

        # Display shopping cart
        if 'cart' not in st.session_state:
            st.session_state.cart = []

        st.header("Carrito de Compras")
        if st.session_state.cart:
  
            st.write(f"**Total: ${total:.2f}**")

            for item in st.session_state.cart:
                st.write(f"{item['name']} - ${item['price']}")
                total += float(item['price'])
            st.write(f"**Total: ${total:.2f}**")
        else:
            st.write("Tu carrito está vacío.")

        # Clear cart button
        if st.button("Limpiar Carrito", key = 69696968):
            st.session_state.cart = []

        # Purchase button (mock functionality)
        if st.button("Compra tu carrito", key = 69696969):
            if st.session_state.cart:
                st.success("Compra Exitosa!")
                st.session_state.cart = []
            else:
                st.error("Tu carrito está vacío")


elif st.session_state.difficulty=="Easy":
        st.write("Selecciona las palabras clave ara filtrar los productos que quiera pedir y agregar al carrito")
        keywords_options = ['Coca-Cola', 'Fanta', 'Joya', 'Sprite', 'Light', 
                            'Ciel', 'Fresca', 'Manzana Lift', 'Sidral', 'Powerade', 'Dell Valle', 
                            'Frutsi', 'Vitamin', 'Floria', 'Fuze Tea', 'Toronja']
        keywords = st.multiselect('Nombre', keywords_options, default=['Coca-Cola', 'Fanta', 'Joya'])

        keywords2_options = ['VID', 'PET', 'LAT']
        keywords2 = st.multiselect('Envase', keywords2_options, default=['VID', 'PET', 'LAT'])

        keywords3_options = ['192 ML', '355 ML', "473 ML","500ML", '1.00 L', "1.50 L", "2.00 L", "2.50 L", '5.00 L', "20.00 L"]
        keywords3 = st.multiselect('Litros', keywords3_options, default=[])

        if keywords or keywords2 or keywords3:
            filtered_df = df.copy()  # Start with a copy of the original DataFrame
            if keywords:
                filtered_df = filtered_df[filtered_df['Material.1'].str.contains('|'.join(keywords), case=False)]
            if keywords2:
                filtered_df = filtered_df[filtered_df['Material.1'].str.contains('|'.join(keywords2), case=False)]
            if keywords3:
                filtered_df = filtered_df[filtered_df['Material.1'].str.contains('|'.join(keywords3), case=False)]
        else:
            filtered_df = df.copy() 



        st.write("Productos Filtrados")
        render_df_with_buttons(filtered_df,2000)
      

        for index in range(len(filtered_df)):
            if f'button_clicked_{index}' in st.session_state and st.session_state[f'button_clicked_{index}']:
                st.text(f'Producto {index} Agregado!')

        # Display shopping cart
        if 'cart' not in st.session_state:
            st.session_state.cart = []

        st.header("Carrito de Compras")
        total = 0
        st.write(f"COCA-COLA 1.00 L NR PET 12 - $241.50")
        total += float(241.50)
        st.write(f"POWERADE LIMALIM 1.00 L NR PET 6 - $152.00")
        total += float(152.00)
        st.write(f"**Total: ${total:.2f}**")
        
        
        if st.session_state.cart:
            total = 0
            for item in st.session_state.cart:
                st.write(f"{item['name']} - ${item['price']}")
                total += float(item['price'])
            st.write(f"**Total: ${total:.2f}**")
        else:
            st.write("")

        # Clear cart button
        if st.button("Limpiar Carrito", key = 696968):
            st.session_state.cart = []

        # Purchase button (mock functionality)
        if st.button("Compra tu carrito", key= 696969):
            if st.session_state.cart:
                st.success("Compra Exitosa!")
                st.session_state.cart = []
            else:
                st.error("Tu carrito está vacío")
        
