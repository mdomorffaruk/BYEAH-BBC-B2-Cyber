#    9. Write a Python program to remove the nth index character from a nonempty string.

def remove_nth_char(string, n):
    if n < 0 or n >= len(string):
        return "Invalid index"
    else:
        return string[:n] + string[n+1:]

input_string = input("Enter a string: ")
index = int(input("Enter the index to remove:(Index start from 0): "))
result = remove_nth_char(input_string, index)
print("Result:", result)
