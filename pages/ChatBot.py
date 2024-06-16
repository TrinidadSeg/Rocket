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
    <div style="background-color: #{background_color}; padding: 10px; border-width:10px; border-color:#E88874;">
       <center> <img src="https://lasmasinnovadoras.com/wp-content/uploads/2023/10/arca.png" width=300 alt="Flowers in Chania"> </center>
        <h5 style="color: maroon; text-align:right;">Bienvenido {User}</h5>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

if st.session_state.name == "Invitado":
    custom_header(f"{st.session_state.name}", "ffffff")
    st.write("Para acceder a ContinentalBot, inicia sesión antes para recibir ayuda personalizada de nuestra IA :)")
    if st.button("Haz click aquí para iniciar sesión", use_container_width=True):
        st.switch_page("pages/perfil.py")


else:
    st.title("ContinentalBot")
    custom_header(f"{st.session_state.name}", "ffffff")

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    initial_prompt = one_data_gpt_predefinded
    secondary_prompt = two_data_gpt_predefinded
    tertiary_prompt = three_data_gpt_predefinded
    quartary_prompt = four_data_gpt_predefinded

    def send_message(prompt):
        st.session_state.messages.append({"role": "user", "content": f"Usted: {prompt}"})
        with st.chat_message("assistant"):
            stream = client.chat_completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = ""
            for chunk in stream:
                response += chunk['choices'][0]['delta']['content']
                st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": f"ContinentalBot: {response}"})

    send_message(initial_prompt)
    send_message(secondary_prompt)
    send_message(tertiary_prompt)
    send_message(quartary_prompt)

    if prompt := st.chat_input("Escriba su pregunta aquí"):
        st.session_state.messages.append({"role": "user", "content": f"Usted: {prompt}"})
        with st.chat_message("user"):
            st.markdown(f"Usted: {prompt}")

        with st.chat_message("assistant"):
            stream = client.chat_completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = ""
            for chunk in stream:
                response += chunk['choices'][0]['delta']['content']
                st.write(response)
        
        st.session_state.messages.append({"role": "assistant", "content": f"ContinentalBot: {response}"})
