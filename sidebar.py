import streamlit as st

def buttons_difficulty_sidebar():
    with st.sidebar:
        if st.button("Navegador simple"):
            st.session_state.difficulty = 'Easy'
        if st.button("Navegador completo"):
            st.session_state.difficulty = 'Hard'
