# 9. Take an array of number input and print Ascending and Descending order 
numbers=input("input number array separated by space: ")
arrayofnumbers=numbers.split()
arrayofnumbers.sort(reverse=False)
print("Ascending Order: ")
print(arrayofnumbers)
arrayofnumbers.sort(reverse=True)
print("Descending order: ")
print(arrayofnumbers)