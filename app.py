import os
import sys

def main():
    # Check if the user provided exactly one argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    # Get the file name from command-line arguments
    file_name = sys.argv[1]

    # Check if the filename is valid (not empty and does not contain directory separators)
    if not file_name or os.path.sep in file_name:
        print("Error: Invalid filename. Please provide a valid filename without path separators.")
        sys.exit(1)

    # Create a new folder
    folder_name = "new_folder"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Folder '{folder_name}' created.")

    # Create the new file inside the folder
    file_path = os.path.join(folder_name, file_name)
    try:
        with open(file_path, 'w') as file:
            pass  # Create an empty file
        print(f"Blank file '{file_name}' created inside '{folder_name}'.")
    except Exception as e:
        print(f"Error creating file: {e}")
        sys.exit(1)

    # Change file permissions to 755
    try:
        os.chmod(file_path, 0o755)
        print(f"Permissions of '{file_name}' set to 755.")
    except Exception as e:
        print(f"Error changing file permissions: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
