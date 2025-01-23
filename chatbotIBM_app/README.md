# Chatbot with Open-Source LLMs

## Project Overview

This project focuses on building a chatbot using open-source large language models (LLMs). By integrating **Facebook's Blenderbot** with **Hugging Face's Transformers library**, a conversational AI that is both functional and user-friendly was created. The chatbot could be embedded in a web interface, offering a seamless experience for users.

### Key Features

- **Open-Source LLM Integration**: Leverages Facebook's Blenderbot to deliver responsive and context-aware conversations.
- **User-Friendly Web Interface**: Incorporates an intuitive front-end for smooth and accessible interaction.
- **Hugging Face Transformers**: Utilizes the state-of-the-art Transformers Python library to manage and deploy powerful NLP models.
- **Customizable and Scalable**: Provides a foundation to adapt and expand the chatbot for various use cases and domains.

### Objectives

- Gain practical experience in working with open-source LLMs.
- Build a conversational AI system using Facebook's Blenderbot.
- Develop a scalable and user-friendly chatbot application with a modern web interface.
- Explore the functionality and flexibility of Hugging Face's Transformers library for NLP tasks.

---

## Getting Started

To run this project, follow these steps to set up the environment and install the required dependencies.

### Environment Setup

1. **Install `virtualenv`**:
   ```bash
   pip3 install virtualenv

2. **Create and Activate a Virtual Environment:**:
   ```bash
   virtualenv my_env
   source my_env/bin/activate  # On Linux/Mac
   my_env\Scripts\activate     # On Windows

3. **Install the required libraries**:
   ```bash
   python3 -m pip install transformers==4.30.2 torch

## File Overview

1. chatbot.py

The chatbot script that takes a query and returns a response from the llm.

- Usage: 
   ```bash
   python chatbot.py
   ```

2. chatbot_colabApp.ipynb
This file contains the gradio and FastAPI implementations of the chatbot. It is self explanatory, easy to follow and provides hands-on practical implementation and visualization.

3. chatbotFastAPI.py
The FastAPI implementation script

- Usage: Update the url variable with the webpage URL and run:
   ```bash
   pip install fastapi uvicorn transformers pydantic pyngrok nest-asyncio
   ```

   ```bash
   ngrok.set_auth_token("YOUR_AUTHTOKEN")
   ```

   ```bash
   python chatbotFastAPI.py
   ```

After running the field above, you should see a public URL in the output(e.g., http://<ngrok_id>.ngrok.io).

- Use the public URL to access the app.
- Append /docs to view the auto-generated Swagger UI (e.g., http://<ngrok_id>.ngrok.io/docs).
- Use the /chatbot endpoint in the Swagger UI or Postman to test the chatbot.
- Alternatively use curl to query the chatbot as seen below. 

```bash
curl -X POST \
  "https://8edb-35-201-240-180.ngrok-free.app/chatbot" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is the capital of France?"}'
```

```
{ "response": "I am good. I am from france. The capital of france is paris." }
```

4. chatbotFlask
The Flask implementation

- Usage: 
   ```bash
   pip install flask flask-cors transformers
   ```

   ```bash
   cd chatbotFlask
   ```

   ```bash
   python app.py
   ```

Feel free to contribute or provide feedback to improve this project.