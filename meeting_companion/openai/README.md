# Audio Transcription and Summarization App

This application transcribes audio files using the Whisper model and then summarizes the transcribed text using OpenAI's GPT-4 model.

## How it Works

1. **Audio Input:** The user uploads an audio file.
2. **Transcription:** The audio file is transcribed using the Whisper model from OpenAI.
3. **Summarization:** The transcribed text is sent to the GPT-4 model, which generates a concise summary.
4. **Output:** The summary is displayed to the user.

## Usage

1. **Upload an audio file** using the interface.
2. **Click "Submit"** to start the transcription and summarization process.
3. **View the summary** in the output box.

## Requirements

- Python 3.10+
- Install the necessary packages using:

   ```bash
   pip install -r requirements.txt

## Deployment

This application is designed to be deployed to Hugging Face Spaces. The `requirements.txt` file lists all the necessary dependencies.

## Example Audio File

An example audio file (`example.wav`) is included for testing.

## Acknowledgments

- **Whisper:** [OpenAI](https://openai.com/research/whisper)
- **GPT-4:** [OpenAI](https://openai.com/research/gpt-4)
- **LangChain:** [LangChain](https://python.langchain.com/)
- **Gradio:** [Gradio](https://gradio.app/)