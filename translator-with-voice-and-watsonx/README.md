# Voice Translation Assistant

## Project Overview

This project focuses on building a **Voice Translation Assistant** using IBM watsonx and Watson Speech Libraries for Embed. The application transforms voice input into text, processes the text using watsonx's FLAN-UL2 model for multilingual translation, and converts the translated text back into speech for playback.

### Key Features
- **🗣️ Speech-to-Text Conversion**: Captures voice input and converts it to text.
- **Language Translation**: Utilizes watsonx's FLAN-UL2 model for multilingual responses.
- **🔊 Text-to-Speech Output**: Converts translated text into speech for user playback.
- **🖥️ Responsive Front-End**: Built with HTML, CSS, and JavaScript for an intuitive user experience.
- **Robust Back-End**: Developed using Flask for seamless integration and processing.
- **🌍 Multi-Language Support**: Translate voice inputs into multiple target languages with high accuracy using **watsonx** and **IBM Watson Language Translator**.

### Lab Environment
This project is implemented within the **IBM Skills Network Labs (SN Labs)** virtual lab environment, providing a robust framework for building and testing AI-powered applications.

---

## Project Workflow

1. **Voice Input**: User provides a voice input.
2. **Speech-to-Text Conversion**: Input is processed and converted into text.
3. **Language Translation**: Text is translated into the desired target language using **watsonx's flan-ul2 model**.
4. **Text-to-Speech Conversion**: Translated text is converted into speech and played back to the user.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **APIs**:
  - IBM Watson Speech-to-Text
  - IBM Watson Language Translator
  - IBM Watson Text-to-Speech
  - Watsonx AI (flan-ul2)

---

## Prerequisites

- **Python**: Version 3.6 or higher
- **IBM Cloud Account**: [Sign up here](https://cloud.ibm.com/registration)
- **API Keys and Credentials** for:
  - IBM Watson Speech-to-Text
  - IBM Watson Language Translator
  - IBM Watson Text-to-Speech
  - Watsonx AI

---

## Setup Instructions

1. set up the environment:
   ```bash
   python3.11 -m venv my_env
   source my_env/bin/activate # activate my_env
   ```

1. Clone the repository:
   ```bash
   git clone the repo
   cd into the cloned repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables with your IBM Cloud credentials:
     ```env
     SPEECH_TO_TEXT_APIKEY=your-speech-to-text-apikey
     SPEECH_TO_TEXT_URL=your-speech-to-text-url

     LANGUAGE_TRANSLATOR_APIKEY=your-language-translator-apikey
     LANGUAGE_TRANSLATOR_URL=your-language-translator-url

     TEXT_TO_SPEECH_APIKEY=your-text-to-speech-apikey
     TEXT_TO_SPEECH_URL=your-text-to-speech-url

     WATSONX_APIKEY=your-watsonx-apikey
     WATSONX_URL=your-watsonx-url
     ```

4. Start the Flask server:
   ```bash
   python server.py
   ```

5. Access the application in your browser:
   ```
   http://localhost:5000
   ```
---

## Usage

1. Open the application in your browser.
2. Select your desired target language.
3. Select a voice based on the language.
3. Speak into your microphone to provide input.
4. The application processes the input and plays back the translation in audio format.

---

## Contributing

We welcome contributions to improve this project! Please feel free to submit issues or pull requests.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to:
- [IBM Watson AI Services](https://www.ibm.com/watson)
- [Cognitive Class Labs](https://labs.cognitiveclass.ai)

