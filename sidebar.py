import streamlit as st


def buttons_difficulty_sidebar():
    # Custom CSS to set the height of the sidebar
    sidebar_css = """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        height: 100% ;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        height: 0%
    }
    </style>
    """
    
    # Inject the custom CSS into the Streamlit app
    st.markdown(sidebar_css, unsafe_allow_html=True)

    with st.sidebar:
        if st.button("Navegador simple"):
            st.session_state.difficulty = 'Easy'
        if st.button("Navegador completo"):
            st.session_state.difficulty = 'Hard'
