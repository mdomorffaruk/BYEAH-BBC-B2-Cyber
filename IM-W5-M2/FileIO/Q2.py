
    # 2. Write a Python program to read first n lines of a file.
def read_first_n_lines(file_name, n):
    with open(file_name, 'r') as file:
        lines = [next(file) for _ in range(n)]
    return lines

file_name = 'q2.txt'
n = 3
first_n_lines = read_first_n_lines(file_name, n)
print(f"First {n} lines of the file:")
for line in first_n_lines:
    print(line, end='')
