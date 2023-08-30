# 2. Write a Python program to count the number of characters (character frequency) in a string.
def count_characters(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

input_string = input("Enter a string: ")
character_frequency = count_characters(input_string)

print("Character frequency:")
for char, count in character_frequency.items():
    print(f"'{char}': {count}")