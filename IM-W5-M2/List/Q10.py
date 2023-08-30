# 10. Write a Python program to select an item randomly from a list.

import random

def random_item(lst):
    return random.choice(lst)

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
random_choice = random_item(my_list)
print("Randomly selected item:", random_choice)
