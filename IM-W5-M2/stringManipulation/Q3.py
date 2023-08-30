# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.

def extract_chars(string):
    if len(string) < 2:
        return "String length is less than 2"
    else:
        return string[:2] + string[-2:]

input_string = input("Enter a string: ")
result = extract_chars(input_string)
print("Result:", result)
