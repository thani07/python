import streamlit as st
from bytez import Bytez
import time
from gtts import gTTS
import io

# ------------------- Setup Bytez -------------------
sdk = Bytez("01e652718e0e753c64c35d90498e03da")
model = sdk.model("Qwen/Qwen3-4B-Instruct-2507")

SYSTEM_PROMPT = """You are an AI medical assistant chatbot.
Rules for answering:
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

# ------------------- Streamlit Page -------------------
st.set_page_config(page_title="🩺 AI Medical Assistant", page_icon="🩺", layout="wide")
st.title("🩺 AI Medical Assistant")
st.caption("💡 Ask your health-related question. Bot messages are left, your messages are right.")

# ------------------- CSS -------------------
st.markdown("""
<style>
.chat-box {
    max-height: 550px;
    overflow-y: auto;
    padding: 10px;
}
.bot-container, .user-container {
    display: flex;
    margin-bottom: 5px;
}
.bot-container img, .user-container img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
}
.bot-container img { margin-right: 8px; }
.user-container img { margin-left: 8px; }
.bot-msg {
    background-color: #fff3cd;
    padding: 12px 15px;
    border-radius: 15px;
    max-width: 70%;
}
.user-msg {
    background-color: #d1e7dd;
    padding: 12px 15px;
    border-radius: 15px;
    max-width: 70%;
}
.bot-container { justify-content: flex-start; flex-direction: column; }
.user-container { justify-content: flex-end; flex-direction: column; }
.speaker-btn {
    background-color: #ffeeba;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    text-align: center;
    cursor: pointer;
    font-size: 20px;
    line-height: 40px;
    margin-left: 48px;
}
</style>
""", unsafe_allow_html=True)

# ------------------- Custom Project Hint -------------------
st.markdown('<div style="text-align:right; font-size:12px; color:gray;">Created by: SEC</div>', unsafe_allow_html=True)

# ------------------- Initialize Session -------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        ("assistant", "👋 Hello! I'm your AI medical assistant. Ask about symptoms, recovery, or health tips.")
    ]

bot_avatar = "https://i.ibb.co/Xx7QxKwx/image.png"
user_avatar = "https://i.ibb.co/1GxPZ8R4/image.png"

# ------------------- Sidebar -------------------
with st.sidebar:
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            ("assistant", "👋 Hello! I'm your AI medical assistant. Ask about symptoms, recovery, or health tips.")
        ]

# ------------------- Chat Display Function -------------------
def display_chat():
    chat_container = st.container()
    with chat_container:
        st.markdown('<div class="chat-box">', unsafe_allow_html=True)
        for idx, (role, content) in enumerate(st.session_state.messages):
            if role == "user":
                st.markdown(f'''
                    <div class="user-container">
                        <div class="user-msg">{content}</div>
                        <img src="{user_avatar}">
                    </div>
                ''', unsafe_allow_html=True)
            else:
                # Bot message bubble
                st.markdown(f'''
                    <div class="bot-container">
                        <img src="{bot_avatar}">
                        <div class="bot-msg">{content}</div>
                    </div>
                ''', unsafe_allow_html=True)

                # Generate TTS audio
                tts_fp = io.BytesIO()
                tts = gTTS(content)
                tts.write_to_fp(tts_fp)
                tts_fp.seek(0)

                # Unique key for each speaker button using idx + hash(content)
                unique_key = f"speaker{idx}_{hash(content)}"

                # Speaker button
                if st.button("🔊", key=unique_key):
                    st.audio(tts_fp, format="audio/mp3")
        st.markdown('</div>', unsafe_allow_html=True)

# Initial chat display
display_chat()

# ------------------- Chat Input -------------------
if prompt := st.chat_input("Type your question..."):
    # Add user message
    st.session_state.messages.append(("user", prompt))
    display_chat()  # refresh display to show user message

    # Typing animation
    with st.spinner("Thinking..."):
        time.sleep(1)
        # Get bot response
        response = ask_medical_chatbot(prompt)
        response = response.replace("\\n", "\n").replace("{", "").replace("}", "")
        st.session_state.messages.append(("assistant", response))
        display_chat()  # refresh display to show bot reply
