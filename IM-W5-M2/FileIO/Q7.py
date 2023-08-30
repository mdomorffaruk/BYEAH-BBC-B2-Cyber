
    # 7. Write a Python program to read a file line by line store it into an array.
 
def read_file_into_array(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

file_name = 'q7.txt'
lines_array = read_file_into_array(file_name)
print("Lines of the file stored in an array:")
print(lines_array)
