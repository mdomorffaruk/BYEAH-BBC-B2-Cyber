#   10. Write a Python program to change a given string to a new string.

def replace_string(original, target, replacement):
    return original.replace(target, replacement)

input_string = input("Enter the original string: ")
target_substring = input("Enter the substring to replace: ")
replacement_string = input("Enter the replacement string: ")

result = replace_string(input_string, target_substring, replacement_string)
print("Result:", result)
