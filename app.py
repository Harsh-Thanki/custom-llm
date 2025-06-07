# app.py
import streamlit as st
from rag_chain import answer_question

st.set_page_config(page_title="Company LLM Assistant", page_icon="💬")
st.title("💬 Company Assistant Chat")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Create a form to wrap input + submission
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask something about the company:", key="input_box")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    # Add user's message
    st.session_state.chat_history.append(("user", user_input))

    # Get assistant response
    with st.spinner("Thinking..."):
        try:
            answer = answer_question(user_input)
        except Exception as e:
            answer = f"⚠️ Error: {str(e)}"

    st.session_state.chat_history.append(("bot", answer))

# Display the chat history
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Assistant:** {message}")
