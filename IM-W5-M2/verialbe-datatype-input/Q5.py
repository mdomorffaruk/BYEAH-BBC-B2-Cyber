# 5. Take string input and print 3rd and last element of it. (input must be greater than 3)
string_input=input("Enter a string: ")

if(len(string_input)>3):
    third_element=string_input[2]
    last_element=string_input[len(string_input)-1]
    # print(len(string_input))
    print("third element: "+third_element+"\nlast element: "+last_element)
else:
    print("Please input a string that is more than 3 character long")