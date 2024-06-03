import os
import pandas as pd

def convert_csv_to_txt(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return
    
    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            csv_path = os.path.join(folder_path, file_name)
            
            # Read the CSV file
            df = pd.read_csv(csv_path)
            
            # Create the TXT file path
            txt_file_name = file_name.rsplit('.', 1)[0] + '.txt'
            txt_path = os.path.join(folder_path, txt_file_name)
            
            # Write the DataFrame to a TXT file with tab as the delimiter
            df.to_csv(txt_path, sep='\t', index=False)
            print(f"Converted {csv_path} to {txt_path}")
            
            # Remove the original CSV file
            os.remove(csv_path)
            print(f"Removed original CSV file: {csv_path}")


# folder_path = 'phum'
folder_path = 'srok'
convert_csv_to_txt(folder_path)
