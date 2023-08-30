#  2. Write a Python program to multiply all the items in a list.

def multiply_list_items(lst):
    result = 1
    for item in lst:
        result *= item
    return result

my_list = [2, 3, 4, 5]
total_product = multiply_list_items(my_list)
print("Product of list items:", total_product)
