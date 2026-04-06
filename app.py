import streamlit as st
import uuid
from auth.auth import login, register
from chatbot.graph import chatbot_graph
from chatbot.memory import save_chat, load_chats, load_messages
from utils.helpers import generate_chat_title


st.write("✅ App started")

st.set_page_config(page_title="AI Chatbot", layout="wide")


try:

    if "user" not in st.session_state:
        st.session_state.user = None

    if "chat_id" not in st.session_state:
        st.session_state.chat_id = None

    if "messages" not in st.session_state:
        st.session_state.messages = []

    
    if not st.session_state.user:
        st.markdown("<h2 style='text-align:center;'>🔐 Login / Register</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            tab1, tab2 = st.tabs(["Login", "Register"])

            with tab1:
                username = st.text_input("Username", key="login_user")
                password = st.text_input("Password", type="password", key="login_pass")

                if st.button("Login"):
                    if login(username, password):
                        st.session_state.user = username
                        st.session_state.chat_id = str(uuid.uuid4())
                        st.session_state.messages = []
                        st.success("Login successful")
                        st.rerun()
                    else:
                        st.error("Invalid credentials")

            with tab2:
                new_user = st.text_input("New Username", key="reg_user")
                new_pass = st.text_input("New Password", type="password", key="reg_pass")

                if st.button("Register"):
                    if register(new_user, new_pass):
                        st.success("Registered successfully. Please login.")
                    else:
                        st.error("User already exists")

   
    else:
        st.sidebar.title(f"👤 {st.session_state.user}")

        if st.sidebar.button("➕ New Chat"):
            st.session_state.chat_id = str(uuid.uuid4())
            st.session_state.messages = []
            st.rerun()

        st.sidebar.subheader("📜 Previous Chats")

        chats = load_chats(st.session_state.user)

        if chats:
            for i, (cid, title) in enumerate(chats):
                if st.sidebar.button(title, key=f"chat_{i}"):
                    st.session_state.chat_id = cid
                    st.session_state.messages = load_messages(st.session_state.user, cid)
                    st.rerun()
        else:
            st.sidebar.info("No previous chats")

        st.title("💬 AI Chatbot")

        if not st.session_state.messages:
            st.info("Start a new conversation...")

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        user_input = st.chat_input("Ask anything...")

        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

         
            st.write("⚡ Generating response...")

            with st.spinner("🤖 Thinking... Please wait..."):
                response = chatbot_graph(st.session_state.messages)

            
            st.write("✅ Response received")

            st.session_state.messages.append({"role": "assistant", "content": response})

            title = generate_chat_title(st.session_state.messages[0]["content"])

            save_chat(
                st.session_state.user,
                st.session_state.chat_id,
                title,
                st.session_state.messages
            )

            st.rerun()


except Exception as e:
    st.error("❌ App crashed")
    st.exception(e)