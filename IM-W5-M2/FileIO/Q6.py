
    # 6. Write a Python program to read a file line by line store it into a variable.
def read_file_into_variable(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

file_name = 'q6.txt'
file_content = read_file_into_variable(file_name)
print("File content stored in a variable:")
print(file_content)
