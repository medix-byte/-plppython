def read_and_modify_file():
    try:
        # Ask user for the file name to read
        input_filename = input("Enter the name of the file to read: ")

        # Open and read file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (example: make text uppercase)
        modified_content = content.upper()

        # Ask for new file name to save modified content
        output_filename = input("Enter the name of the new file to save: ")

        # Write the modified content into the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Modified file saved as '{output_filename}' successfully.")

    except FileNotFoundError:
        print("Error: The file you specified does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read/write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
