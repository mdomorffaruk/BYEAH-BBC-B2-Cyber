# 4. Write a Python program to get a string from a given string where all occurrences of 'S' have been changed to '$'.

def replace_s_with_dollar(string):
    return string.replace('s', '$')

input_string = input("Enter a string: ")

result = replace_s_with_dollar(input_string.lower())
print("Result:", result)
