import streamlit as st

# Initialize the session state for the cart if it doesn't exist
if 'cart' not in st.session_state:
    st.session_state.cart = []

# List of products (name, price, description)
products = [
    {"id": 1, "name": "Product 1", "price": 10.0, "description": "Description of Product 1"},
    {"id": 2, "name": "Product 2", "price": 20.0, "description": "Description of Product 2"},
    {"id": 3, "name": "Product 3", "price": 30.0, "description": "Description of Product 3"}
]

# Function to add a product to the cart
def add_to_cart(product_id):
    for product in products:
        if product['id'] == product_id:
            st.session_state.cart.append(product)
            break

# Streamlit layout
st.title("E-Commerce Store")

# Display products
st.header("Products")
for product in products:
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(f"**{product['name']}** - ${product['price']:.2f}")
        st.write(product['description'])
    with col2:
        st.button("Add to Cart", key=product['id'], on_click=add_to_cart, args=(product['id'],))

# Display shopping cart
st.header("Shopping Cart")
if st.session_state.cart:
    total = 0
    for item in st.session_state.cart:
        st.write(f"{item['name']} - ${item['price']:.2f}")
        total += item['price']
    st.write(f"**Total: ${total:.2f}**")
else:
    st.write("Your cart is empty.")

# Clear cart button
if st.button("Clear Cart"):
    st.session_state.cart = []

# Purchase button (mock functionality)
if st.button("Purchase"):
    if st.session_state.cart:
        st.success("Purchase successful!")
        st.session_state.cart = []
    else:
        st.error("Your cart is empty.")
