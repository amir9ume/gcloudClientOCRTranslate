import os
import time
import logging
from google.cloud import vision
from google.cloud import translate_v2 as translate
import re

def natural_keys(text):
    """ Helper function to produce a list of keys for sorting strings that include numerical parts. """
    return [int(c) if c.isdigit() else c for c in re.split('(\d+)', text)]


def pic_to_text(infile: str) -> str:
    """Detects text in an image file using Google Vision API."""
    vision_client = vision.ImageAnnotatorClient()
    with open(infile, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = vision_client.document_text_detection(image=image)
    return response.full_text_annotation.text

def translate_text(text: str, target_language="en") -> str:
    """Translates text to a specified language using Google Translate API."""
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def ensure_directory(directory):
    """Ensure the directory exists. If not, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def process_images(input_directory, output_directory, target_language="en"):
    """Processes images in a directory, translating detected text and saving to another directory."""
    ensure_directory(output_directory)  # Make sure the output directory exists
    files = sorted(os.listdir(input_directory),  key=natural_keys)  # Sort files to ensure they are processed in order
    for i, filename in enumerate(files):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"translated_text_page_{i+1}.txt")
            logging.info(f"Processing {image_path}...")
            try:
                detected_text = pic_to_text(image_path)
                logging.debug(f"Detected text for {image_path}: {detected_text}")
                translated_text = translate_text(detected_text, target_language=target_language)
                logging.debug(f"Translated text for {image_path}: {translated_text}")
                with open(output_path, "w") as file:
                    file.write(f"Original Text (Page {i+1}):\n{detected_text}\n")
                    file.write(f"Translated Text (Page {i+1}):\n{translated_text}\n")
                logging.info(f"Successfully saved {output_path}")
                time.sleep(1)  # Sleep to avoid hitting rate limits
            except Exception as e:
                logging.error(f"Failed to process {image_path}: {str(e)}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    input_directory = "output_images"  # Directory containing images
    output_directory = "output_text"   # Directory to store translated texts
    process_images(input_directory, output_directory, target_language="en")

