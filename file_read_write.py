# Step 1: Read teh file content

try: 
    with open('original.txt', 'r') as infile:
        content = infile.read()
        print("File content read successfully.")

# Step 2: Modify the content
        modified_content = content.replace('old text', 'new text')

# Step 3: Write the modified content to a new file
    with open('modified.txt', 'w') as outfile:
        outfile.write(modified_content)
        print("File content written successfully.")

except FileNotFoundError:
    print("Error: The file 'original.txt' was not found.")
except  Exception as e:
    print(f"An error occurred: {e}")

