# 8. Take string input and delete a middle element of it.
import math
input_string=input("Enter a string: ")


middle_element_index=math.ceil(len(input_string)/2)
print(middle_element_index)
new_string=""

for index in range(len(input_string)):
    if index==middle_element_index-1:
        continue
    new_string=new_string+input_string[index]  

print(new_string)

