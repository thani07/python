import streamlit as st
from bytez import Bytez
import time
import re

# ------------------- Setup Bytez -------------------
sdk = Bytez("01e652718e0e753c64c35d90498e03da")
model = sdk.model("Qwen/Qwen3-4B-Instruct-2507")

SYSTEM_PROMPT = """You are an AI medical assistant chatbot.
Rules:
1. Respond only to the specific question.
2. Use clear, simple sentences.
3. List symptoms or steps in bullet points.
4. Bold key terms like **Headache**, **Fever**.
5. No extra comments unless asked.
"""

def ask_medical_chatbot(user_message):
    output, error = model.run([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ])
    if error:
        return f"⚠️ Error: {error}"
    if isinstance(output, dict) and "content" in output:
        return output["content"].strip()
    return str(output).strip()

# ------------------- Streamlit Page Config -------------------
st.set_page_config(page_title="🩺 AI Medical Assistant", page_icon="🩺", layout="wide")
st.title("🩺 AI Medical Assistant")
st.caption("💡 Ask your health-related question. Bot messages are left, your messages are right.")

# ------------------- Light/Dark Mode Toggle -------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

with st.sidebar:
    st.session_state.theme = st.radio("Choose Theme", ["light", "dark"])
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            ("assistant", "👋 Hello! I'm your AI medical assistant. ")
        ]

# ------------------- Theme CSS -------------------
if st.session_state.theme == "dark":
    st.markdown("""
    <style>
    body { background-color:#0e1117; color:white; }
    .chat-box { background-color:#1b1e23; padding:10px; max-height:550px; overflow-y:auto; border-radius:10px; }
    .bot-msg { background-color:#343a40; color:white; padding:12px 15px; border-radius:15px; max-width:70%; }
    .user-msg { background-color:#0d6efd; color:white; padding:12px 15px; border-radius:15px; max-width:70%; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .chat-box { background-color:#f0f2f6; padding:10px; max-height:550px; overflow-y:auto; border-radius:10px; }
    .bot-msg { background-color:#fff3cd; padding:12px 15px; border-radius:15px; max-width:70%; }
    .user-msg { background-color:#d1e7dd; padding:12px 15px; border-radius:15px; max-width:70%; }
    </style>
    """, unsafe_allow_html=True)

# ------------------- Initialize Messages -------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        ("assistant", "👋 Hello! I'm your AI medical assistant. ")
    ]

bot_avatar = "https://i.ibb.co/7W3J0Yk/ai-bot.png"  # AI bot image
user_avatar = "https://share.google/images/xkZqk4mawtHakRmyp"  # User image

# ------------------- Quick Suggestion Buttons -------------------
quick_buttons = ["Fever Symptoms", "Cold Remedies", "COVID-19 Symptoms", "Headache Tips"]
st.markdown("**💡 Quick Questions:**")
cols = st.columns(len(quick_buttons))
for idx, q in enumerate(quick_buttons):
    if cols[idx].button(q):
        st.session_state.messages.append(("user", q))

# ------------------- Chat Display -------------------
chat_container = st.container()
with chat_container:
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    for role, content in st.session_state.messages:
        # Highlight keywords (bold medical terms)
        content = re.sub(r"\b(Fever|Headache|Cough|Nausea|Fatigue|Symptoms|Recovery)\b",
                         r"**\1**", content, flags=re.IGNORECASE)
        if role == "user":
            st.markdown(f'''
                <div style="display:flex; justify-content:flex-end; margin-bottom:8px;">
                    <div class="user-msg">{content}</div>
                    <img src="{user_avatar}" width="40" height="40" style="border-radius:50%; margin-left:8px;">
                </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown(f'''
                <div style="display:flex; justify-content:flex-start; margin-bottom:8px;">
                    <img src="{bot_avatar}" width="40" height="40" style="border-radius:50%; margin-right:8px;">
                    <div class="bot-msg">{content}</div>
                </div>
            ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------- Chat Input -------------------
prompt = st.chat_input("Type your question...")
if prompt:
    st.session_state.messages.append(("user", prompt))
    # Display user message immediately
    with chat_container:
        st.markdown(f'''
            <div style="display:flex; justify-content:flex-end; margin-bottom:8px;">
                <div class="user-msg">{prompt}</div>
                <img src="{user_avatar}" width="40" height="40" style="border-radius:50%; margin-left:8px;">
            </div>
        ''', unsafe_allow_html=True)

    # Typing animation for bot
    placeholder = st.empty()
    for i in range(3):
        placeholder.markdown(f'''
            <div style="display:flex; justify-content:flex-start; margin-bottom:8px;">
                <img src="{bot_avatar}" width="40" height="40" style="border-radius:50%; margin-right:8px;">
                <div class="bot-msg">Typing{'.'* (i+1)}</div>
            </div>
        ''', unsafe_allow_html=True)
        time.sleep(0.5)

    # Replace placeholder with actual bot reply
    response = ask_medical_chatbot(prompt)
    response = re.sub(r"\b(Fever|Headache|Cough|Nausea|Fatigue|Symptoms|Recovery)\b",
                      r"**\1**", response, flags=re.IGNORECASE)
    st.session_state.messages.append(("assistant", response))
    placeholder.markdown(f'''
        <div style="display:flex; justify-content:flex-start; margin-bottom:8px;">
            <img src="{bot_avatar}" width="40" height="40" style="border-radius:50%; margin-right:8px;">
            <div class="bot-msg">{response}</div>
        </div>
    ''', unsafe_allow_html=True)
