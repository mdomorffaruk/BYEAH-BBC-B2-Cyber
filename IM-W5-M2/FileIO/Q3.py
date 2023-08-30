
    # 3. Write a Python program to append text to a file and display the text.
def read_entire_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content
def append_to_file(file_name, text):
    with open(file_name, 'a') as file:
        file.write(text)

file_name = 'q3.txt'
text_to_append = "\nThis text is appended."
append_to_file(file_name, text_to_append)

# Display the updated file content
file_content = read_entire_file(file_name)
print("Updated file content:")
print(file_content)
