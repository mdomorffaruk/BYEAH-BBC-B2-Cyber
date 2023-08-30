#   7. Write a Python program that accepts a comma-separated sequence of words as input and print the shortest word.

def shortest_word(words):
    word_list = words.split(',')
    shortest = min(word_list, key=len)
    return shortest

input_words = input("Enter comma-separated words: ")
result = shortest_word(input_words)
print("Shortest word:", result)
