# Image Captioning Project

This project demonstrates how to generate captions for images using the BLIP model (`Salesforce/blip-image-captioning-base`) from Hugging Face. It includes scripts for local image captioning, a Gradio-based web app, and automated captioning of images scraped from web pages.

- Link to hugging face spaces Gradio app: https://huggingface.co/spaces/Kelex83/Caption_images

## Features

- **Gradio Web App**: Provides an easy-to-use interface for image captioning.
- **Web Image Captioning**: Automates the process of scraping images from a webpage and generating captions for them.
- **Local Image Captioning**: Generate captions for locally stored images.
- **Hugging Face Space**: Try out the Gradio app live: [Image Captioning App](https://huggingface.co/spaces/Kelex83/Caption_images).

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
   pip install langchain==0.1.11 gradio==4.44.0 transformers==4.38.2 bs4==0.0.2 requests==2.31.0 torch==2.2.1

## File Overview

1. image_captioning.ipynb: Google colab implementation.

2. image_cap.py

A script to generate captions for a single image file.

- Usage: Update img_path with the path to your image and run the script:
   ```bash
   python image_cap.py

- Example Output:
   ```bash
   "A horse running in a grassy field."

3. image_captioning_app.py

A Gradio-based web app for captioning images interactively.

- Usage: Run the script:
   ```bash
   python image_captioning_app.py

Open the displayed URL in your browser to upload an image and generate a caption.

4. automate_url_captioner.py

A script to scrape images from a webpage, caption them, and save the captions to a text file.

- Usage: Update the url variable with the webpage URL and run:
   ```bash
   python automate_url_captioner.py

Captions will be saved to captions.txt.

5. img_cap_local_files.py

A script to scrape images from your local files, caption them, and save the captions to a text file.

- Usage: Update the url variable with the path to your local images and run:
   ```bash
   python img_cap_local_files.py


## Testing the Application

You can test the app directly via the Hugging Face Space where you can upload an image or enter an image url and it will generate a downloadable caption:

[Hugging Face Space - Caption Images](https://huggingface.co/spaces/Kelex83/Caption_images).

Alternatively, clone this repository and run any of the scripts locally as per the instructions above.

## Hugging Face Space

The app has been deployed on Hugging Face Spaces, providing an easy way to interact with the model online. The configuration for the Space is defined in the README.md file and associated metadata.

## Acknowledgements

This project uses the BLIP (Bootstrapped Language-Image Pretraining) model from Salesforce:

- [BLIP on Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/blip).

Additionally, the Gradio library powers the interactive web app:

- [Gradio Documentation](https://www.gradio.app/).

Feel free to contribute or provide feedback to improve this project. Happy coding! 😊