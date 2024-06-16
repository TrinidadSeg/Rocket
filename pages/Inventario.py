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

# read by default 1st sheet of an excel file
df = pd.read_excel('pages/BaseDatos_PreciosMexico.xlsx')
    # Inputs for row index and column name
row_index = st.number_input("Enter row index", min_value=0, max_value=len(df)-1, step=1)
column_name = st.text_input("Enter column name")
list_of_products = []
list_of_prices = []
for counter in range(0,511):
    list_of_products.append(df.loc[counter, "Material.1"])
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
        st.write(f"**{product['name']}** - ${product['price']}")
        st.write("hi")
    with col2:
        st.button("Add to Cart", key=product['id'], on_click=add_to_cart, args=(product['id'],))


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
