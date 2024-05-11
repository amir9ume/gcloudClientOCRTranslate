import os
import re

def natural_sort_key(s):
    """Sort strings containing numbers naturally."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def combine_files(directory, output_filename):
    """Combine text files in a directory into a single file."""
    # Get all text files and sort them naturally based on page numbers
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    files.sort(key=natural_sort_key)

    # Create or overwrite the output file
    with open(output_filename, 'w') as outfile:
        for filename in files:
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as readfile:
                # Read the content of the file and write it to the output file
                outfile.write(f"--- {filename} ---\n")
                outfile.write(readfile.read() + "\n")

if __name__ == "__main__":
    input_directory = 'output_text'  # Directory containing translation text files
    output_file = 'combined_translations.txt'  # File to store all combined translations
    combine_files(input_directory, output_file)
    print(f"All files have been combined into {output_file}.")

