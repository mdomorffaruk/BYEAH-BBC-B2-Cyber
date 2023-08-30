#  5. Write a Python program to count the number of strings from a given list

def count_strings(lst):
    count = 0
    for item in lst:
        if isinstance(item, str):
            count += 1
    return count

my_list = [1, "apple", 3, "banana", "cherry"]
string_count = count_strings(my_list)
print("Number of strings:", string_count)
