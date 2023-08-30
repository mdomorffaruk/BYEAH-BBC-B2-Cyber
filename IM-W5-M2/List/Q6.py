#  6. Write a Python program to find the second largest number in a list.

def find_second_largest(lst):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[1]

my_list = [17, 25, 10, 38, 4]
second_largest = find_second_largest(my_list)
print("Second largest number:", second_largest)
