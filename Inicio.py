import streamlit as st
from sidebar import buttons_difficulty_sidebar

#Sidebar
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = 'Easy'

buttons_difficulty_sidebar()


st.title("Arca Continental")


#Easy
if st.session_state.difficulty=="Easy":
    st.subheader("¡Bienvenido!")
    st.write("En los siguientes botónes, podrás accedar a las diferentes páginas del navegador y obtener más información")
  
    if st.button("Inventario", use_container_width=True):
        st.switch_page("pages/Inventario.py")


#Hard
elif st.session_state.difficulty=="Hard":
    st.write("Harddd")

