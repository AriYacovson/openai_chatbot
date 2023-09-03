# OpenAI Chatbot

This repository contains a chatbot application powered by OpenAI's GPT-3.5-turbo model. The chatbot is designed to interact with users through a web interface, allowing them to send messages and receive responses from the model.

## Features

- **Chat Interface**: Users can send messages to the chatbot and view the chat history.
- **Image Generation**: The application also supports generating images based on user prompts.
- **Docker Support**: The repository includes a Dockerfile for easy deployment.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AriYacovson/openai_chatbot.git
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up OpenAI API Key:
Ensure you have your OpenAI API key set up in an environment variable or a .env file.

Run the Application:
You can run the application using FastAPI. The main entry point is main.py.

Usage
Navigate to the root endpoint / to access the chat interface.
For image generation, navigate to the /image endpoint.
Dependencies
The project relies on several Python packages, including:

FastAPI
Jinja2
Mangum
OpenAI
and others...
Docker Deployment
The repository includes a Dockerfile for deploying the application using Docker. You can build and run the Docker container using the provided Dockerfile.
