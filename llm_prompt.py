import streamlit as st
from groq import Groq

st.markdown("""
<style>
    .stApp { background: linear-gradient(90deg,rgba(2, 0, 36, 1) 75%, rgba(9, 9, 121, 1) 100%, rgba(0, 212, 255, 1) 50%); }
</style>
""", unsafe_allow_html=True)

st.title("---Zaara---")

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages: # 
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Type a message...")

if prompt:
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)


    
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[ 
            {"role": "system", "content": "You are an advance level ai assisstant bot, giving suggestions on every topic, and you are specialized in coding,algorithms and programming "},
            *st.session_state.messages
        ]
    )
    reply = response.choices[0].message.content.strip()
    
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
