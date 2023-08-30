
   
    # 4. Write a Python program to read last n lines of a file.

def read_last_n_lines(file_name, n):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines[-n:]

file_name = 'q4.txt'
n = 3
last_n_lines = read_last_n_lines(file_name, n)
print(f"Last {n} lines of the file:")
for line in last_n_lines:
    print(line, end='')
