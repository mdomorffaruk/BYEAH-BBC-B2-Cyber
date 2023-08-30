
    # 5. Write a Python program to read a file line by line and store it into a list.
    
def read_file_into_list(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

file_name = 'q5.txt'
lines_list = read_file_into_list(file_name)
print("Lines of the file stored in a list:")
print(lines_list)

