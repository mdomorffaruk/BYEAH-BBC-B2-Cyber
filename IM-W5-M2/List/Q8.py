#  8. Write a Python program to check if a list is empty or not.

def is_list_empty(lst):
    return len(lst) == 0

my_list = []
if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")
