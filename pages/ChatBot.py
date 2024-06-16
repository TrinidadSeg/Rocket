from openai import OpenAI 
import streamlit as st
from data import one_data_gpt_predefinded
from data import two_data_gpt_predefinded
from data import three_data_gpt_predefinded
from data import four_data_gpt_predefinded

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
        response = st.write("En que te puedo ayudar?")
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
        response = st.write("En que te puedo ayudar?")
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
        response = st.write("En que te puedo ayudar?")
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
        st.session_state.messages.append({"role": "assistant", "content": f"ContinentalBot: {response}"})







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
