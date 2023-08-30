# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.

def longest_word_and_length(words):
    word_list = words.split()
    longest = max(word_list, key=len)
    
    return longest, len(longest)

input_words = input("Enter words separated by spaces: ")
longest_word, length = longest_word_and_length(input_words)
print("Longest word:", longest_word)
print("Length:", length)
