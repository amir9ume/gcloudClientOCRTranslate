#!/bin/bash

# Check if a PDF path is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_pdf>"
    exit 1
fi

pdf_path=$1
pdf_name=$(basename "$pdf_path" .pdf)  # Extract the base name without the .pdf extension

# Run bookToImageBatch.py with the PDF path as an argument
python bookToImageBatch.py "$pdf_path"

# Check if the output_images directory exists
if [ -d "output_images" ]; then
    echo "The output_images directory exists."

    # Count the number of files in the directory
    num_files=$(ls -1 output_images | wc -l)
    echo "There are $num_files files in the output_images directory."

    # Get the name of the first file
    first_file=$(ls output_images | head -n 1)
    echo "The first file in the directory is: $first_file"

    # Run bookImagesTranslator.py
    python bookImagesTranslator.py

    # Run combineTextsToMakeBook.py
    python combineTextsToMakeBook.py

    # Rename combined_translations.txt to translated_{original_pdf_name}.txt
    mv combined_translations.txt "translated_${pdf_name}.txt"
    echo "Renamed combined_translations.txt to translated_${pdf_name}.txt"

else
    echo "Error: The output_images directory does not exist."
    exit 1  # Exit the script with an error code
fi

