from openai import OpenAI 
import streamlit as st

st.title("ContinentalBot")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

initial_prompt = """"Once upon a time, in a quaint village nestled between rolling hills and whispering woods, there lived a young girl named Elara. Elara was known far and wide for her kindness and her uncanny ability to understand the language of animals.

One crisp autumn morning, as she wandered through the forest collecting herbs, she heard a faint cry for help. Following the sound, she stumbled upon a wounded deer trapped in a hunter's snare. Without hesitation, Elara approached the frightened creature and began soothing it with gentle words.

"Stay calm, dear friend," she whispered, her voice carrying a magical warmth. With steady hands, she carefully freed the deer from the trap, tending to its injuries with herbal salves and a touch that seemed to heal more than just flesh.

As the deer bounded away into the safety of the forest, Elara felt a strange tingling sensation in her fingertips. Little did she know, her act of kindness had caught the attention of the forest spirits. That night, as she slept beneath a canopy of stars, she dreamed of a great oak tree with leaves shimmering like emeralds.

The next morning, Elara awoke to find herself surrounded by woodland creatures—birds, squirrels, even a wise old fox—all waiting patiently as if expecting her. She soon realized they were asking for her help, their silent pleas echoing in her mind. A drought had gripped the forest, and water had become scarce.

With a newfound sense of purpose, Elara set out on a quest to find the source of the drought. Through her conversations with animals and her deep connection to nature, she discovered that an ancient spell, cast by a forgotten sorcerer, had disturbed the balance of the forest.

Guided by the wisdom of the creatures she helped, Elara embarked on a journey to reverse the spell. Along the way, she faced challenges that tested her courage and resolve. Yet, with each obstacle overcome, her bond with the natural world grew stronger.
Finally, standing before the great oak tree from her dream, Elara performed a ritual of renewal. Her voice rose in a melodic chant, carrying the essence of hope and healing. Slowly, drops of rain began to fall, quenching the parched earth and bringing life back to the forest.
In the aftermath, as the animals rejoiced and the leaves of the oak tree shimmered once more, Elara understood the true power of compassion and connection. Her journey had not only saved the forest but had also awakened a deeper magic within herself.
From that day forward, Elara became known not only as the girl who could speak to animals but also as the guardian of the forest—a testament to the extraordinary things that happen when kindness and courage join forces. And so, her legend spread far beyond the village, inspiring others to cherish and protect the natural world around them."

"""


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
