import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from database import init_db, register_user, validate_user, get_chat_history, save_chat_history, clear_chat_history

# Initialize database
init_db()

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

# Ensure the API key is loaded
if api_key is None:
    st.error("GOOGLE_API_KEY is not set. Please add it to your .env file.")
else:
    # Configure the Google Generative AI
    from google.generativeai import configure
    configure(api_key=api_key)

    def get_conversational_chain():
        prompt_template = """
        You are a helpful chat assistant.End every answer with \n\n . Below is the conversation history:
        {history}

        Question: {question}

        Answer:
        """
        prompt = PromptTemplate(template=prompt_template, input_variables=["history", "question"])
        model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=api_key)
        chain = LLMChain(llm=model, prompt=prompt)
        return chain

    def user_input(user_question, username):
        chain = get_conversational_chain()
        history = st.session_state.history
        response = chain({"history": history, "question": user_question})

        # Update the chat history
        st.session_state.history += f"User: {user_question}\nBot: {response['text']}\n"
        save_chat_history(username, st.session_state.history)

        return response["text"]

    def login():
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if validate_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.history = get_chat_history(username)
                st.success("Logged in successfully")
            else:
                st.error("Invalid credentials")

    def register():
        st.title("Register")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            register_user(username, password)
            st.success("Registered successfully. Please log in.")

    def main():
        st.set_page_config(page_title="Chatbot from Kishiva")

        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
            st.session_state.history = ""
            st.session_state.username = ""

        if st.session_state.logged_in:
            col1, col2, col3 = st.columns([5, 1, 1])
            
            with col1:
                st.header(f"Welcome, {st.session_state.username}")
            
            with col2:
                if st.button("Clear History", key="clear_history"):
                    clear_history(st.session_state.username)
                
            with col3:
                if st.button("Logout", key="logout"):
                    logout()

            # Layout with single column for history, current answer, and user input
            
            with col1:
                st.write("### Input")
                user_question = st.text_input("Ask a Question")

            if st.button("Ask", key="ask") and user_question:
                answer = user_input(user_question, st.session_state.username)
                #st.write("### Current Answer")
                st.write(answer)

            st.write("### Chat History")
            if "history" in st.session_state:
                st.write(st.session_state.history.strip())

        else:
            mode = st.sidebar.selectbox("Mode", ["Login", "Register"])
            if mode == "Login":
                login()
            else:
                register()

    def logout():
        st.session_state.logged_in = False
        st.session_state.history = ""
        st.session_state.username = ""

    def clear_history(username):
        clear_chat_history(username)
        st.session_state.history = ""
        st.success("Chat history cleared.")

    if __name__ == "__main__":
        main()
