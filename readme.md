# Streamlit Chatbot for Kishiva Internship
Tech-Stack: Google Gemini API, Langchain, Streamlit

This project is a Streamlit application that integrates with Google Generative AI to create a conversational chatbot. It includes user authentication, chat history management, and context-based responses.

## Features

- **User Authentication**: Register and log in to use the chatbot.
- **Chat Context**: Maintains context of the conversation for more accurate responses.
- **Chat History**: Save and display chat history for each user.
- **Clear History**: Option to clear the chat history.
- **Logout**: Option to log out of the application.

## Requirements

- Python
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

### database.py:
- This file contains many functions to add, delete and validate users.
- It uses sqlite3 module of python.
- This file is responsible for all the database features, We just have to call these functions in our main file.
- Further explanation can be found in the comments.

### main.py:
- This is the main python file of our project.
- We have used streamlit for building the front-end using python.
- The entry-point of the project is the login page.
- If login is successful, then the chat page gets launched.
- Users can see their own chat history.
- This file contains code for Langchain, Google-Genai and Streamlit.

### .env:
- This file has my API key for Google's Gemini API.
- I have erased the key from github for privacy and confidential nature of the API keys.
- Anyone can get their own API key from Google's AI studio for free.


## Instructions to Use

- Clone this repository on your device.
- Get your own API key from https://aistudio.google.com/app/apikey
- Paste your API key in ".env" file between the quotes.
- You have to install python virtual environment using this command on terminal:
    
        pip install virtualenv
- From here on, all the commands are to run on terminal of the project directory.
- Activate the virtual environment inside the directory using this command on terminal:
      
        .\venv\Scripts\activate
- Install python-dotenv on this virtual environment:
    
        pip install python-dotenv
- Install other dependencies of the project using this command on terminal:

        pip install -r requirements.txt
- Run the streamlit app using this command on terminal at your project directory:

        streamlit run main.py

## Bonus points activity:
There are at least 2 ways deploy our app to cloud.

### Deploy on Popular cloud services like AWS, Azure and GCP
- To deploy production applications, It is advised to use these cloud services which provides better options of reliablity and scalability.
- I have learned how to deploy our project using AWS.
#### Steps to deploy on AWS:
- Set up a free-tier account on aws.
- Setup an EC2 instance.
- Clone this git repository.
- Install every dependency mentioned above.
- run the app using:

        streamlit run main.py
- You will get the IP address where the application is served.
- To make it persistent, that means to make this app available all the times even when you close the aws window in your browser: use nohup command.

### Deploy feature of Streamlit:
- We can use community version for free.
- We can get a url of our project as well.
- I have deployed our app using this feature and you can use it directly here: https://kishiva-chatbot.streamlit.app/
- This method is not recommended for production grade applications.

## Note
Here's the link to demo video: https://drive.google.com/file/d/1ufGY7ETL74q4iWDaCJsGxQyijZn_QugR/view?usp=drive_link  
