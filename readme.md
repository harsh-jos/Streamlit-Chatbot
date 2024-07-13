# Streamlit Chatbot with Google Generative AI

This project is a Streamlit application that integrates with Google Generative AI to create a conversational chatbot. It includes user authentication, chat history management, and context-based responses.

## Features

- **User Authentication**: Register and log in to use the chatbot.
- **Chat Context**: Maintains context of the conversation for more accurate responses.
- **Chat History**: Save and display chat history for each user.
- **Clear History**: Option to clear the chat history.
- **Logout**: Option to log out of the application.

## Requirements

- Python 3.7+
- Streamlit
- Langchain
- Google Generative AI
- SQLite (used for local database)
- `python-dotenv` (for managing environment variables)


The app will be accessible at http://localhost:8501 in your web browser.

## Project Structure
- app.py: Main application file where the Streamlit app is defined.
- database.py: Contains database functions for user authentication and chat history.
- .env: Environment variables file (not included in version control).
- requirements.txt: List of required Python packages.


## Code Explanation

### app.py:
- Handles the Streamlit UI, user authentication, and chat interactions.
Uses st.columns to arrange the layout with title and buttons in a row.
Manages chat history and context with Google Generative AI.

### database.py:

- Manages database operations using SQLite.
Includes functions to register users, validate credentials, save, and clear chat history.
