import os
import sys
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader

if len(sys.argv) < 2:
    print("Usage: python bookToImageBatch.py <path_to_pdf>")
    sys.exit(1)

pdf_path = sys.argv[1]  # Take the PDF path from the first command-line argument
output_folder = 'output_images'
dpi = 300  # Lower DPI for less memory usage
batch_size = 5  # Number of pages to process at a time

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def convert_batch(pdf_path, first_page, lastpage):
    pages = convert_from_path(pdf_path, dpi=dpi, first_page=first_page, last_page=lastpage)
    for i, page in enumerate(pages, start=first_page):
        output_path = os.path.join(output_folder, f'page_{i}.jpg')
        page.save(output_path, 'JPEG')
        print(f"Saved {output_path}")

# Determine number of pages
with open(pdf_path, 'rb') as file:
    reader = PdfFileReader(file)
    total_pages = reader.numPages

# Process in batches
for start in range(1, total_pages + 1, batch_size):
    end = min(start + batch_size - 1, total_pages)
    convert_batch(pdf_path, start, end)

