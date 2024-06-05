import os
import csv

def merge_text_files_to_tsv(root_folder, output_tsv):
    # Open the output TSV file for writing
    with open(output_tsv, 'w', newline='', encoding='utf-8') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t')
        writer.writerow(['province', 'khum'])  # Write the header

        # Walk through the directory structure
        for foldername, subfolders, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.endswith('.txt'):
                    filepath = os.path.join(foldername, filename)
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()
                        lines = content.splitlines()
                        file_base_name = os.path.splitext(filename)[0]  # Remove file extension
                        for line in lines:
                            writer.writerow([file_base_name, line])

# Usage example
merge_text_files_to_tsv('province', 'province.tsv')
