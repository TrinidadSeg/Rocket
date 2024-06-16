import streamlit as st
from sidebar import buttons_difficulty_sidebar
import streamlit.components.v1 as components
image_urls = [
    "https://imagenes.razon.com.mx/files/image_940_470/uploads/2023/04/27/644ab7813fde9.jpeg",
    "https://cdn.forbes.com.mx/2018/05/Arca-continental-05.jpg",
    "https://www.lapoliticaonline.com/files/image/108/108489/61f4097cb7e5e_940_529!.jpg?s=da6fbe5577255a2f7e93c3166f70ae84&d=1644336459",
    "https://d100mj7v0l85u5.cloudfront.net/s3fs-public/Arca-Continental-abrira-una-nueva-planta-en-Estados-Unidos-GR.jpg",
]

# Slideshow HTML
slideshow_html = f"""
<div class="slideshow-container">
    {' '.join(f'<div class="mySlides fade"><img src="{url}" style="width:100%"></div>' for url in image_urls)}
    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<br>
<div style="text-align:center">
    {' '.join(f'<span class="dot" onclick="currentSlide({i+1})"></span>' for i in range(len(image_urls)))}
</div>
<style>
    .slideshow-container {{
        max-width: 1000px;
        position: relative;
        margin: auto;
    }}
    .mySlides {{
        display: none;
    }}
    .fade {{
        -webkit-animation-name: fade;
        -webkit-animation-duration: 1.5s;
        animation-name: fade;
        animation-duration: 1.5s;
    }}
    @-webkit-keyframes fade {{
        from {{opacity: .4}} 
        to {{opacity: 1}}
    }}
    @keyframes fade {{
        from {{opacity: .4}} 
        to {{opacity: 1}}
    }}
    .prev, .next {{
        cursor: pointer;
        position: absolute;
        top: 50%;
        width: auto;
        padding: 16px;
        margin-top: -22px;
        color: white;
        font-weight: bold;
        font-size: 18px;
        transition: 0.6s ease;
        border-radius: 0 3px 3px 0;
        user-select: none;
    }}
    .next {{
        right: 0;
        border-radius: 3px 0 0 3px;
    }}
    .prev:hover, .next:hover {{
        background-color: rgba(0,0,0,0.8);
    }}
    .dot {{
        cursor: pointer;
        height: 15px;
        width: 15px;
        margin: 0 2px;
        background-color: #bbb;
        border-radius: 50%;
        display: inline-block;
        transition: background-color 0.6s ease;
    }}
    .active, .dot:hover {{
        background-color: #717171;
    }}
</style>
<script>
    var slideIndex = 1;
    showSlides(slideIndex);

    function plusSlides(n) {{
        showSlides(slideIndex += n);
    }}

    function currentSlide(n) {{
        showSlides(slideIndex = n);
    }}

    function showSlides(n) {{
        var i;
        var slides = document.getElementsByClassName("mySlides");
        var dots = document.getElementsByClassName("dot");
        if (n > slides.length) {{slideIndex = 1}}    
        if (n < 1) {{slideIndex = slides.length}}
        for (i = 0; i < slides.length; i++) {{
            slides[i].style.display = "none";  
        }}
        for (i = 0; i < dots.length; i++) {{
            dots[i].className = dots[i].className.replace(" active", "");
        }}
        slides[slideIndex-1].style.display = "block";  
        dots[slideIndex-1].className += " active";
    }}
</script>
"""

# Embed the slideshow HTML, CSS, and JavaScript

# Custom CSS to style the square icon
st.markdown("""
    <style>
    .square-icon {
        width: 200px;
        height: 100px;
        background-color: #fff;
        border: 2px solid #b30000;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px auto;
    }
    .square-icon-text {
        color: #fff6666;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

#Sidebar
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = 'Easy'

buttons_difficulty_sidebar()

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
st.title("Arca Continental")


#Easy
if st.session_state.difficulty=="Easy":
    st.subheader("¡Bienvenido!")
    st.write("En los siguientes botónes, podrás accedar a las diferentes páginas del navegador y obtener más información")
  
    if st.button("Inventario", use_container_width=True):
        st.switch_page("pages/Inventario.py")
    if st.button("Pedidos/Calendario", use_container_width=True):
        st.switch_page("pages/Pedidos-Calendario.py")
    if st.button("Promociones", use_container_width=True):
        st.switch_page("pages/Promociones.py")
    if st.button("Ayuda al Usuario", use_container_width=True):
        st.switch_page("pages/ChatBot.py")
    if st.button("Estadísticas", use_container_width=True):
        st.switch_page("pages/Inventario.py")
    if st.button("Perfil", use_container_width=True):
        st.switch_page("pages/perfil.py")


#Hard
elif st.session_state.difficulty=="Hard":
    st.subheader("¡Bienvenido!")
    components.html(slideshow_html, height=600)
    left, right = st.columns(2)
    with left:
        if st.button("Ayuda al Usuario", use_container_width=True):
                st.switch_page("pages/ChatBot.py")
        if st.button("Estadísticas", use_container_width=True):
            st.switch_page("pages/Inventario.py")
        if st.button("Perfil", use_container_width=True):
            st.switch_page("pages/perfil.py")    
    with right:
        if st.button("Inventario", use_container_width=True):
            st.switch_page("pages/Inventario.py")
        if st.button("Pedidos/Calendario", use_container_width=True):
            st.switch_page("pages/Pedidos-Calendario.py")
        if st.button("Promociones", use_container_width=True):
            st.switch_page("pages/Promociones.py")
   