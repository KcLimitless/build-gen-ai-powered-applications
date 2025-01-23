import gradio as gr
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def fetch_image(url: str) -> np.ndarray:
    """Fetch an image from a given URL and return it as a numpy array."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        image = Image.open(response.raw).convert('RGB')
        return np.array(image)
    except Exception as e:
        raise ValueError(f"Failed to fetch image: {str(e)}")

def caption_image(input_image=None, image_url=None):
    """Generate captions for the input image or image fetched from a URL."""
    try:
        if image_url:
            image_array = fetch_image(image_url)
        elif input_image is not None:
            image_array = input_image
        else:
            raise ValueError("Please provide either an image or an image URL.")

        # Ensure the image is in RGB format
        pil_image = Image.fromarray(image_array).convert('RGB')

        # Process the image and generate caption
        inputs = processor(pil_image, return_tensors="pt")
        out = model.generate(**inputs, max_length=50)
        caption = processor.decode(out[0], skip_special_tokens=True)

        # Save caption as a downloadable .txt file
        caption_path = "caption.txt"
        with open(caption_path, "w") as f:
            f.write(caption)

        return caption, caption_path
    except Exception as e:
        return f"Error: {str(e)}", None

iface = gr.Interface(
    fn=caption_image, 
    inputs=[
        gr.Image(type="numpy", label="Upload Image"),
        gr.Textbox(label="Image URL (Optional)", placeholder="Enter an image URL here")
    ], 
    outputs=[
        gr.Textbox(label="Generated Caption"),
        gr.File(label="Download Caption")
    ],
    examples = [
        ["model.jpg"],
        ["horse.jpeg"],
        ["panda.jpg"]
    ],
    title="Advanced Image Captioning with the BLIP model",
    description="Upload an image or provide a URL to generate a caption. Download the generated caption as a .txt file.",
    live=True,
    theme="compact"
)

iface.launch()
