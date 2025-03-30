import streamlit as st
from langchain.chat_models import HuggingFaceHub
from langchain.schema import HumanMessage, AIMessage

# Initialize the Hugging Face model (use a conversational model like 'facebook/blenderbot-400M-distill')
st.title("🤖 LangChain + Hugging Face Chatbot")

# Get your Hugging Face token from https://huggingface.co/settings/tokens
HUGGINGFACEHUB_API_TOKEN = "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"

# Load model from Hugging Face Hub
chat_model = HuggingFaceHub(
    repo_id="facebook/blenderbot-400M-distill",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        st.markdown(f"**You:** {message.content}")
    elif isinstance(message, AIMessage):
        st.markdown(f"**Bot:** {message.content}")

# User input
user_input = st.text_input("Type your message:")

if user_input:
    # Append user's message
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Get bot's response
    bot_response = chat_model([HumanMessage(content=user_input)])
    st.session_state.messages.append(AIMessage(content=bot_response.content))

    # Display bot's response
    st.markdown(f"**Bot:** {bot_response.content}")
