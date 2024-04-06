import pandas as pd
import streamlit as st
import requests

st.title('M-AI')

prompt: str = st.chat_input("Enter a prompt here")

USER = "user"
ASSISTANT = "assistant"

if prompt:
    st.chat_message(USER).write(prompt)
    message = requests.get('https://blab-backend.onrender.com/')
    st.chat_message(ASSISTANT).write(f"You wrote {message.status_code}")
