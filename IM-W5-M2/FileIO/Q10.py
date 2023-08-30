
    # 10. Write a Python program to get the file size of a plain file.

import os

def get_file_size(file_name):
    return os.path.getsize(file_name)

file_name = 'q10.txt'
file_size = get_file_size(file_name)
print(f"File size of '{file_name}': {file_size} bytes")
