import streamlit as st
import requests

st.title("Local LLM Chatbot")

# chat history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask something:")

if st.button("Send") and user_input:

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "tinyllama",
        "prompt": user_input,
        "stream": False
    }

    response = requests.post(url, json=data)
    answer = response.json()["response"]

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("AI", answer))

# show history
for role, msg in st.session_state.history:
    st.write(f"**{role}:** {msg}")

# reset button
if st.button("Reset Chat"):
    st.session_state.history = []