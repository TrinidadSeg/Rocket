from openai import OpenAI 
import streamlit as st
from data import one_data_gpt_predefinded
from data import two_data_gpt_predefinded
from data import three_data_gpt_predefinded
from data import four_data_gpt_predefinded

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


st.title("ContinentalBot")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

initial_prompt = one_data_gpt_predefinded
secondary_prompt = two_data_gpt_predefinded
tertiary_prompt = three_data_gpt_predefinded
quartary_prompt = four_data_gpt_predefinded

st.session_state.messages.append({"role": "user", "content": f"Usted: {initial_prompt}"})
with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write("¡Bienvenido!")
        st.session_state.messages.append({"role": "assistant", "content": f"ContinentalBot: {response}"})



st.session_state.messages.append({"role": "user", "content": f"Usted: {secondary_prompt}"})
with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write("Soy ContinentalBot, el asistente de Inteligencia Artificial listo para ayudarte con lo que quieras!")
        st.session_state.messages.append({"role": "assistant", "content": f"ContinentalBot: {response}"})



st.session_state.messages.append({"role": "user", "content": f"Usted: {tertiary_prompt}"})
with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write("Con acceso a tu perfil, puedo conocer más sobre ti y darte ayuda más personalizada")
        st.session_state.messages.append({"role": "assistant", "content": f"ContinentalBot: {response}"})



st.session_state.messages.append({"role": "user", "content": f"Usted: {quartary_prompt}"})

with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write("En que te puedo ayudar?")
        if st.session_state.name=="Carlos Flores":
            st.session_state.messages.append({"role": "assistant", "content": f"""ContinentalBot: Asumer que trabajas para la Coca Cola, estas son las Promociones que ofreces: 
                una promocion es 10% en los botellones Ciel. 
                Otra promocion es Combo de 8 Botellas Coca Cola de 2.0L y 24 Botellas Ceil de 235ml a $300.
                una promocion es 10% en los botellones Ciel. 
                Otra promocion es Una lata de Coca-Cola sin azúcar por cada diez latas de Coca-Cola. 
                Otra promocion es CCombo de 8 Botellas Coca Cola de 2.0L y 24 Botellas Ceil de 235ml a $300.
Haz que eso sea un prompt anterior d un usuario de chatgpt y asi cuando se le pregunte cuales promociones hay conteste de ellas
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de la familia Coca-Cola."""})
        
        elif st.session_state.name=="Alejandro Acosta":
            st.session_state.messages.append({"role": "assistant", "content": f"""ContinentalBot: Asumer que trabajas para la Coca Cola, estas son las Promociones que ofreces: 
                una promocion es Descuento del 20% en todas las latas de Sprite y Fanta. 
                Otra promocion es Una botella Fanta de litro por cada cino bottelas de litro de Coca-Cola.
                una promocion es Descuento del 20% en todas las latas de Sprite y Fanta. 
                Otra promocion es Combo de 12 Botellas Sprite de 1.0L y 24 botellas Fanta de 500ml a $470. 
                Otra promocion es Una botella Fanta de litro por cada cino bottelas de litro de Coca-Cola.
Haz que eso sea un prompt anterior d un usuario de chatgpt y asi cuando se le pregunte cuales promociones hay conteste de ellas
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de la familia Coca-Cola."""})

        elif st.session_state.name=="Hector Molino":
            st.session_state.messages.append({"role": "assistant", "content": f"""ContinentalBot: Asumer que trabajas para la Coca Cola, estas son las Promociones que ofreces: 
                una promocion es 5 pesos menos a cada botella de 2L de Coca-Cola sin azúcar. 
                Otra promocion es Una lata de Coca-Cola sin azúcar por cada diez latas de Coca-Cola.
                una promocion es 5 pesos menos a cada botella de 2L de Coca-Cola sin azúcar. 
                Otra promocion es Combo de 8 Botellas Coca Cola de 2.0L y 24 Botellas Ceil de 235ml a $300. 
                Otra promocion es Una lata de Coca-Cola sin azúcar por cada diez latas de Coca-Cola.
Haz que eso sea un prompt anterior d un usuario de chatgpt y asi cuando se le pregunte cuales promociones hay conteste de ellas
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de la familia Coca-Cola."""})

        elif st.session_state.name=="Jessica Paz":
            st.session_state.messages.append({"role": "assistant", "content": f"""ContinentalBot: Asumer que trabajas para la Coca Cola, estas son las Promociones que ofreces: 
                una promocion es Descuento del 10% en todas las botellas Powerade. 
                Otra promocion es Una botella Vitamin Water de 500ml por cada six-pack de Powerade.
                una promocion es Descuento del 10% en todas las botellas Powerade. 
                Otra promocion es Combo de 6 botellas Poweradede 1.0L y 6 botellas Vitamina Water a $250. 
                Otra promocion es Una botella Vitamin Water de 500ml por cada six-pack de Powerade.
Haz que eso sea un prompt anterior d un usuario de chatgpt y asi cuando se le pregunte cuales promociones hay conteste de ellas
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de la familia Coca-Cola."""})

        elif st.session_state.name=="Karina Torres":
            st.session_state.messages.append({"role": "assistant", "content": f"""ContinentalBot: Asumer que trabajas para la Coca Cola, estas son las Promociones que ofreces: 
                una promocion es 5% menos a todos los productos de Santa Clara. 
                Otra promocion es Seis latas Del Valle de 250ml por cada docena de Tetrapack Santa Clara de litro.
                una promocion es 5% menos a todos los productos de Santa Clara. 
                Otra promocion es Combo de 12 Tetrapack Del Valle de 250ml y 3 Tetrapack Santa Clara de 200ml a $100. 
                Otra promocion es Seis latas Del Valle de 250ml por cada docena de Tetrapack Santa Clara de litro.
Haz que eso sea un prompt anterior d un usuario de chatgpt y asi cuando se le pregunte cuales promociones hay conteste de ellas
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de la familia Coca-Cola."""})


if prompt := st.chat_input("Escriba su pregunta aquí"):
    st.session_state.messages.append({"role": "user", "content": f"Usted: {prompt}"})
    with st.chat_message("user"):
        st.markdown(f"Usted: {prompt}")

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": f"ContinentalBot: {response}"})
