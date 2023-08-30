
    # 1. Write a Python program to read an entire text file.
    

def read_entire_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

file_name = 'q1.txt'
file_content = read_entire_file(file_name)
print("File content:")
print(file_content)
