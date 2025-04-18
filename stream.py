import streamlit as st
from chatbot import Chatbot

st.set_page_config(page_title="SSM Chatbot", layout="centered")

# Custom styling and animation
st.markdown("""
    <style>
    body {
        font-family: Arial, sans-serif;
        background: #f3f4f6;
    }
    .chatbox {
        width: 100%;
        max-width: 600px;
        background: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        height: 400px;
        overflow-y: auto;
        margin: 1rem auto;
        display: flex;
        flex-direction: column;
    }
    .message {
        margin: 10px 0;
        padding: 10px 15px;
        border-radius: 10px;
        max-width: 80%;
        word-wrap: break-word;
        font-size: 16px;
    }
    .user {
        align-self: flex-end;
        background-color: #cce0ff;
        # background-color: #e0ecff;
        # color: blue;
        text-align: right;
    }
    .bot {
        align-self: flex-start;
        # background-color: #e6ffe6;
        # color: green;
        background-color: #ccffcc;
        text-align: left;
    }

    /* 🟢 Style for latest message pair */
    .latest-user {
        background-color: #e0ecff;
        color: blue;
        animation: highlight 0.7s ease-in-out;
    }
    .latest-bot {
        background-color: #e6ffe6;
        color: green;
        animation: highlight 0.7s ease-in-out;
    }
    @keyframes highlight {
        from { transform: scale(1.02); box-shadow: 0 0 8px rgba(0, 0, 0, 0.15); }
        to { transform: scale(1); }
    }

    .input-container {
        width: 100%;
        max-width: 600px;
        margin: auto;
        display: flex;
        gap: 10px;
    }
    .input-container input {
        flex: 1;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    .input-container button {
        padding: 10px 15px;
        border: none;
        background-color: #4f46e5;
        color: white;
        border-radius: 5px;
        cursor: pointer;
    }
    .input-container button:hover {
        background-color: #3730a3;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>SSM Learning Excellence Centre Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Write Exit to close the Chat</h5>", unsafe_allow_html=True)

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input form
with st.form("chat_input", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    user_input = col1.text_input("", placeholder="Type your message…", label_visibility="collapsed")
    send = col2.form_submit_button("Send")

# Process input
if send and user_input:
    st.session_state.messages.append(("user", user_input))
    bot = Chatbot()
    response = bot.chat(user_input)
    st.session_state.messages.append(("bot", response))

# Show messages in reverse order with animation on latest
chat_html = '<div class="chatbox" id="chatbox">'

reversed_messages = st.session_state.messages[::-1]
for i, (sender, message) in enumerate(reversed_messages):
    role_class = "user" if sender == "user" else "bot"
    # Highlight latest pair
    if i < 2:
        role_class = f"latest-{role_class}"
    chat_html += f'<div class="message {role_class}">{message}</div>'

chat_html += '</div>'

# Optional JS to auto-scroll to top (not needed now as chatbox is column-reverse)
st.markdown(chat_html, unsafe_allow_html=True)
