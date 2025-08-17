import os

def concatenate_files_recursively():
    """
    Recursively finds all files in a user-specified folder (relative to this script),
    and concatenates their content into a single .txt file.
    """
    try:
        # Get the directory where this script is located.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Get user input
        folder_name = input("Enter the folder name (relative to the script's location): ")
        output_filename = input("Enter the name for the output .txt file (e.g., 'combined.txt'): ")

        # Construct the full path to the target folder
        target_folder_path = os.path.join(script_dir, folder_name)

        # Validate the folder path
        if not os.path.isdir(target_folder_path):
            print(f"Error: The folder '{target_folder_path}' does not exist.")
            return

        # Ensure the output file has a .txt extension
        if not output_filename.endswith('.txt'):
            output_filename += '.txt'
            
        # The output file will be saved in the same directory as the script
        output_filepath = os.path.join(script_dir, output_filename)

        print(f"\nProcessing files in '{target_folder_path}'...")

        # Open the output file in write mode
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            # os.walk() recursively visits all directories and subdirectories
            for dirpath, _, filenames in os.walk(target_folder_path):
                for filename in filenames:
                    # Construct the full path to the current file
                    full_filepath = os.path.join(dirpath, filename)
                    
                    # Skip the output file itself if it's in the scanned path
                    if full_filepath == output_filepath:
                        continue

                    try:
                        with open(full_filepath, 'r', encoding='utf-8', errors='ignore') as infile:
                            content = infile.read()
                            
                            # Get the path relative to the target folder for the header
                            relative_path = os.path.relpath(full_filepath, target_folder_path)
                            
                            # Write file header with its relative path
                            outfile.write(f"--- START OF FILE: {relative_path} ---\n\n")
                            # Write file content
                            outfile.write(content)
                            # Write file footer
                            outfile.write(f"\n\n--- END OF FILE: {relative_path} ---\n\n")
                            
                            print(f"Successfully added '{relative_path}'.")
                    except Exception as e:
                        print(f"Could not read file '{relative_path}': {e}")
        
        print(f"\nSuccess! All files have been concatenated into '{output_filepath}'.")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    concatenate_files_recursively()
