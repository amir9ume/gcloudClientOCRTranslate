**Project Documentation**

This project provides a series of scripts designed to convert a PDF file into images, translate text from those images, and then compile the translated text into a single document. This process is particularly useful for translating documents while preserving the layout and structure found in the original PDF.

**Setup Instructions**

Install google-cloud-translate for translating text using Google Cloud's Translation API. 
pip install google-cloud-translate

Install the remaining necessary Python libraries using pip, based on the errors which show up.


**Google Cloud Credentials:**

To use the Google Translate API, you need to set up a Google Cloud project and enable the Google Cloud Translation API.
1. Go to the Google Cloud Console (https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to "APIs & Services" > "Dashboard" and enable the "Cloud Translation API".
4. Go to "APIs & Services" > "Credentials" and click "Create Credentials" to generate a new service account key.
5. Download the JSON key file. This file contains your credentials.
6. Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the JSON key file. This allows the Google Cloud SDK to authenticate your requests.
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials-file.json"


The **pdfTranslate.sh** script takes a PDF file as an input and converts each page into an image.
Run this script by passing the path to the PDF file:

**bash pdfTranslate.sh path_to_your_pdf.pdf**

**Translate Images and Compile Translations:**

After converting the PDF to images, the script automatically calls the translation script which uses OCR (Optical Character Recognition) to extract text from images and translates it using Google Translate. The translated texts are then compiled into a single file, with a "translated_" prefix and name of the original PDF.

These are the different tasks happening under the hood:

1. bookToImageBatch.py: Converts the PDF document into a series of images stored in an output folder.
2. bookImagesTranslator.py: Processes the images to extract text and translates it using the Google Cloud Translation API.
3. combineTextsToMakeBook.py: Compiles all translated texts into a single file.
