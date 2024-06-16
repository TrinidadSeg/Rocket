import streamlit as st
import numpy as np
import pandas as pd

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

nav_simple = True


# read by default 1st sheet of an excel file
df = pd.read_excel('pages/BaseDatos_PreciosMexico.xlsx')
    # Inputs for row index and column name
columns_to_select =['Material.1', 'Precio Final']

if nav_simple == True:
    smaller_df = df[columns_to_select]
    def create_html_button(index):
        return f'<button style = "background-color: red; color:white; border-width: 0px; border-radius:10px "; onclick="alert(\'Button {index} clicked\')"><b>Agregar al Carrito</b></button>'

        # Add a column with buttons to the DataFrame
        smaller_df['Action'] = smaller_df.index.map(lambda x: create_html_button(x))

    # Function to render the DataFrame with buttons
    def render_df_with_buttons(dataframe):
        for index, row in dataframe.iterrows():
            col1, col2, col3 = st.columns(3)
            col1.write(row['Material.1'])
            col2.write(row['Precio Final'])
            if col3.button("Agregar al Carrito", key=index):
                st.session_state[f'button_clicked_{index}'] = True

    # Search bar
    search_query = st.text_input("Search the DataFrame")

    # Filter the DataFrame based on the search query
    if search_query:
        filtered_df = smaller_df[smaller_df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
    else:
        filtered_df = smaller_df

    # Display the filtered DataFrame with buttons
    st.write("Filtered DataFrame with Buttons:")
    render_df_with_buttons(filtered_df)

    # Display text for each button clicked
    for index in range(len(smaller_df)):
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
        st.write("Tu carrito esta vacio.")

        # Clear cart button
    if st.button("Limpiar Carrito"):
        st.session_state.cart = []

        # Purchase button (mock functionality)
    if st.button("Compra tu carrito"):
        if st.session_state.cart:
            st.success("Compra Exitosa!")
            st.session_state.cart = []
        else:
            st.error("Tu carrito esta vacio")

  




if nav_simple == False:
    list_of_products = []
    list_of_prices = []
    for counter in range(0,511):
        name = df.loc[counter, "Material.1"]
        name = name[:-9]
        list_of_products.append(name)
        list_of_prices.append(df.loc[counter, "Precio Final"])
        counter+=1



    if 'cart' not in st.session_state:
        st.session_state.cart = []

    # List of products (name, price, description)
    products = []

    for nCounter in range(0,511):
        products.append({"id": nCounter, 'name': list_of_products[nCounter], 'price': list_of_prices[nCounter]})

    # Function to add a product to the cart
    def add_to_cart(product_id):
        for product in products:
            if product['id'] == product_id:
                st.session_state.cart.append(product)
                break

    # Streamlit layout



    # Display products
    st.header("Productos")
    for product in products:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"{product['name']} - ${product['price']}")
            st.write("hi")
        with col2:
            st.button("Agrega al Carrito", key=product['id'], on_click=add_to_cart, args=(product['id'],))


    # Display shopping cart
    st.header("Carrito de Compras")
    if st.session_state.cart:
        total = 0
        for item in st.session_state.cart:
            st.write(f"{item['name']} - ${item['price']}")
            total += float(item['price'])
        st.write(f"**Total: ${total:.2f}**")
    else:
        st.write("Tu carrito esta vacio.")

    # Clear cart button
    if st.button("Limpiar Carrito"):
        st.session_state.cart = []

    # Purchase button (mock functionality)
    if st.button("Compra tu carrito"):
        if st.session_state.cart:
            st.success("Compra Exitosa!")
            st.session_state.cart = []
        else:
            st.error("Tu carrito esta vacio")
