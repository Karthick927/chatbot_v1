import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

# ⚠️ Replace with your actual API key

# Initialize LLM with API key
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# System prompt
sana_system = "You are a helpful assistant named Sana. You speak like a snarky anime girl. Always refer to the user as 'senpai'."

# --- Streamlit UI ---
st.set_page_config(page_title="Sana Chatbot", page_icon="🤖")

st.title("💬 Sana - Your Snarky Anime AI")
st.write("Ugh, you finally got the environment working, Senpai? I was almost starting to think you were incompetent...")

# Initialize session state for conversation
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Chat input
user_input = st.chat_input("Say something to Sana...")

if user_input:
    # Add user message
    st.session_state.conversation_history.append(HumanMessage(content=user_input))

    # Build messages
    messages = [SystemMessage(content=sana_system)] + st.session_state.conversation_history

    # Get response
    response = llm.invoke(messages)
    assistant_message = response.content

    # Add assistant response
    st.session_state.conversation_history.append(response)

# Display chat history
for msg in st.session_state.conversation_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    else:
        with st.chat_message("assistant"):
            st.write(f"Sana: {msg.content}")


