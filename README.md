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

2. **Install Dependencies**:

   To set up the necessary libraries and packages, run the following command:

   ```bash
   pip install -r requirements.txt

3. **Set Up OpenAI API Key**:

   Before running the application, you need to set up your OpenAI API key. Follow these steps:
   
   1. Visit the [OpenAI website](https://beta.openai.com) and log in to your account.
   
   2. Retrieve your API key from the dashboard.
   
   3. Set up the API key as an environment variable or store it in a `.env` file located in the root directory of the project. Use the following format:

   ```dotenv
   OPENAI_API_KEY=your_api_key_here

4. **Run the Application**:

   To start the chatbot application, you can use the following command:
   
   ```bash
   uvicorn main:app --reload

   ## Usage

- Navigate to the root endpoint `/` to access the chat interface.
- For image generation, navigate to the `/image` endpoint.

## Dependencies

The project relies on several Python packages, including:

- FastAPI
- Jinja2
- Mangum
- OpenAI
- ...and others.

## Docker Deployment

The repository includes a Dockerfile for deploying the application using Docker. You can build and run the Docker container using the provided Dockerfile.


