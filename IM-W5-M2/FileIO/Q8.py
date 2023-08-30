
    # 8. Write a python program to find the longest words.
 

def find_longest_words(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words, max_length

file_name = 'q8.txt'
longest_words, max_length = find_longest_words(file_name)
print(f"Longest word(s) with length {max_length}:")
print(', '.join(longest_words))
