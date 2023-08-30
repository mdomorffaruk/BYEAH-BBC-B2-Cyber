
    # 9. Write a Python program to count the number of lines in a text file.
def count_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return len(lines)

file_name = 'q9.txt'
line_count = count_lines(file_name)
print(f"Number of lines in the file: {line_count}")
