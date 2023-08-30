# 5. Write a Python program to get a single string from two given strings, separated by a comma.

def combine_strings_with_comma(str1, str2):
    return str1 + ',' + str2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = combine_strings_with_comma(string1, string2)
print("Result:", result)
