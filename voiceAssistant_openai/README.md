# Voice Assistant with OpenAI GPT-3 and IBM Watson

This project involves creating a voice assistant using OpenAI's GPT-3 for natural language understanding and IBM Watson services for speech processing. The assistant can understand and respond to user queries in a conversational manner.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a working development environment set up with the IBM Skills Network Cloud IDE. You can also run the code locally with minor adjustments.
- You have access to OpenAI's GPT-3 API. Note that using this API may incur charges.
- You have an IBM Cloud account to access Watson services.
- Basic knowledge of Python programming.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone the rpository
   ```

   ```bash
   cd into the cloned repo.
   ```

2. Install the required Python packages:
   
   ```bash
   pip install -r requirements.txt
   ``` 

## Usage

Set up your environment variables for OpenAI and IBM Watson credentials. You can do this by creating a .env file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key
IBM_WATSON_API_KEY=your_ibm_watson_api_key
IBM_WATSON_URL=your_ibm_watson_url

### Run the application with Docker:

Run these commands with a single click to fulfill some of the prerequisites:

```bash
mkdir /home/project/chatapp-with-voice-and-openai/certs/
cp /usr/local/share/ca-certificates/rootCA.crt /home/project/chatapp-with-voice-and-openai/certs/
```

### Starting the application

```bash
docker build . -t voice-chatapp-powered-by-openai
docker run -p 8000:8000 voice-chatapp-powered-by-openai
```

The application must be opened on a new tab since the minibrowser in this environment cannot support certain required features.

Your browser may deny “pop-ups” but please allow them for the new tab to open up.

## Contributing

Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes and commit them (git commit -m 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
