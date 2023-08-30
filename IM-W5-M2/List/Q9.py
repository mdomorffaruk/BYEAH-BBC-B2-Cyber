# 9. Write a Python program to clone or copy a list.

def clone_list(lst):
    return lst.copy()

original_list = [1, 2, 3, 4, 5]
copied_list = clone_list(original_list)
print("Original list:", original_list)
print("Copied list:", copied_list)
