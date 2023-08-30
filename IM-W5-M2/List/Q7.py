    # 7. Write a Python program to remove duplicates from a list.

def remove_duplicates(lst):
    return list(set(lst))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print("List with duplicates removed:", unique_list)
