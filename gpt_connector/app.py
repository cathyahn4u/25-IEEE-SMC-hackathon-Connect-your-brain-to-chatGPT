# app.py
import streamlit as st
import numpy as np
import time
import json
from gpt_service import create_conversation, send_message
from prompts import CONTEXTS

# ---------------------------
# Load test cases
# ---------------------------
with open("test.txt", "r") as f:
    TEST_CASES = json.load(f)

# ---------------------------
# Streamlit setup
# ---------------------------
st.set_page_config(page_title="EEG → ChatGPT UI", layout="wide")

# ---------------------------
# Sidebar (EEG + context)
# ---------------------------
with st.sidebar:
    st.title("🧠 MindBridge")

    # EEG chart
    eeg_placeholder = st.empty()
    chart_data = np.random.randn(20, 1)
    eeg_chart = eeg_placeholder.line_chart(chart_data)

    # Animate EEG briefly
    for _ in range(5):
        new_data = np.random.randn(1, 1)
        chart_data = np.vstack([chart_data[1:], new_data])
        eeg_chart.line_chart(chart_data)
        time.sleep(0.05)

    # Context and test case selectors
    st.subheader("Select Context")
    context_option = st.selectbox(
        "Conversation Context",
        ["default", "supportive", "control"],
        index=0
    )

    st.subheader("Select Test Case")
    test_case_name = st.selectbox(
        "Test Case",
        [t["name"] for t in TEST_CASES],
    )

    start_btn = st.button("▶️ Start Test")

# ---------------------------
# Initialize session state
# ---------------------------
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "running" not in st.session_state:
    st.session_state.running = False

# ---------------------------
# Main chat area
# ---------------------------
st.title("EEG → ChatGPT Conversation")
chat_box = st.container()  # where messages will be appended

# ---------------------------
# When Start Test is clicked
# ---------------------------
if start_btn:
    # Reset session state
    st.session_state.messages = []
    st.session_state.running = True

    # Get selected test
    selected_test = next((t for t in TEST_CASES if t["name"] == test_case_name), None)
    if not selected_test:
        st.error("⚠️ Test case not found!")
    else:
        context_option = selected_test["context"]
        st.session_state.conversation_id = create_conversation()

        # Send context system prompt first
        send_message(st.session_state.conversation_id, CONTEXTS[context_option])

        # Process exactly 3 message pairs
        for user_text in selected_test["messages"][:3]:
            # 1️⃣ Add user message
            st.session_state.messages.append(("🧍 You", user_text))
            with chat_box:
                st.markdown(f"**🧍 You:** {user_text}")

            # 2️⃣ Get GPT reply
            gpt_reply = send_message(st.session_state.conversation_id, user_text)

            # 3️⃣ Add GPT message
            st.session_state.messages.append(("🤖 GPT", gpt_reply))
            with chat_box:
                st.markdown(f"<div style='margin-left:20px;'>**🤖 GPT:** {gpt_reply}</div>", unsafe_allow_html=True)

            # Pause briefly for readability
            time.sleep(1.5)

        st.session_state.running = False
        with chat_box:
            st.markdown("---")
            st.success("✅ Test finished!")

# ---------------------------
# Show any existing messages (after rerun)
# ---------------------------
elif st.session_state.messages:
    with chat_box:
        for sender, msg in st.session_state.messages:
            if sender == "🧍 You":
                st.markdown(f"**{sender}:** {msg}")
            else:
                st.markdown(f"<div style='margin-left:20px;'>**{sender}:** {msg}</div>", unsafe_allow_html=True)
