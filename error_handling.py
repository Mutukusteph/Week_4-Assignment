# Error_handling_lab.py

filename = input('Enter the filename to read:')

try:
    with open(filename, 'r') as infile:
        content = infile.read()
        print("File content read successfully.")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: Permission denied when trying to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")