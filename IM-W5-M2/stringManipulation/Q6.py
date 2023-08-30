#  6. Write a Python program to add 'ing' at the end of a given string.

def add_ing(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'

input_string = input("Enter a string: ")
result = add_ing(input_string)
print("Result:", result)
