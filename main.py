import streamlit as st
from bytez import Bytez

# Initialize Bytez SDK
sdk = Bytez("01e652718e0e753c64c35d90498e03da")
model = sdk.model("Qwen/Qwen3-4B-Instruct-2507")

SYSTEM_PROMPT = """You are an AI medical assistant chatbot.
Rules for answering:
1. Respond **only** to the specific question asked, do not provide extra explanations.
2. Use clear, simple sentences.
3. If listing symptoms or steps, give them in a clean bullet-point or numbered list without markdown headers.
4. Use light bolding for key terms (e.g., **Headache**, **Fever**).
5. Do not add notes, comments, or disclaimers unless asked.
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


# ---------------- Streamlit Chat UI ----------------
st.set_page_config(page_title="AI Medical Assistant", page_icon="🩺", layout="wide")

st.markdown("""
<style>
.chat-box {
    max-height: 550px;
    overflow-y: auto;
    padding: 10px;
}
.bot-container, .user-container {
    display: flex;
    margin-bottom: 10px;
}
.bot-container img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 8px;
}
.user-container img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-left: 8px;
}
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
.bot-container { justify-content: flex-start; }
.user-container { justify-content: flex-end; }
</style>
""", unsafe_allow_html=True)

# Custom hint/signature for your project
st.markdown('<div style="text-align:right; font-size:12px; color:gray;">Created by: SEC</div>', unsafe_allow_html=True)

st.title("🩺 AI Medical Assistant")
st.caption("💡 Ask your health-related question. Bot messages are left, your messages are right.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(("assistant", "👋 Hello! I'm your AI medical assistant. Ask me about symptoms, recovery, or health tips."))

# Sidebar to clear chat
with st.sidebar:
    if st.button("🗑️ Clear Chat"):
        # Reset messages to initial state
        st.session_state.messages = [
            ("assistant", "👋 Hello! I'm your AI medical assistant. Ask me about symptoms, recovery, or health tips.")
        ]


# Chat display
chat_container = st.container()
bot_avatar = "https://i.ibb.co/Xx7QxKwx/image.png"  # AI bot-looking avatar placeholder
user_avatar = "https://i.ibb.co/1GxPZ8R4/image.png"  # your user avatar


with chat_container:
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    for role, content in st.session_state.messages:
        if role == "user":
            st.markdown(f'''
                <div class="user-container">
                    <div class="user-msg">{content}</div>
                    <img src="{user_avatar}">
                </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown(f'''
                <div class="bot-container">
                    <img src="{bot_avatar}">
                    <div class="bot-msg">{content}</div>
                </div>
            ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Type your question..."):
    # Add user message
    st.session_state.messages.append(("user", prompt))
    with chat_container:
        st.markdown(f'''
            <div class="user-container">
                <div class="user-msg">{prompt}</div>
                <img src="{user_avatar}">
            </div>
        ''', unsafe_allow_html=True)

    with st.spinner("Thinking..."):
        response = ask_medical_chatbot(prompt)
        response = response.replace("\\n", "\n").replace("{", "").replace("}", "")
        st.session_state.messages.append(("assistant", response))
        with chat_container:
            st.markdown(f'''
                <div class="bot-container">
                    <img src="{bot_avatar}">
                    <div class="bot-msg">{response}</div>
                </div>
            ''', unsafe_allow_html=True)
