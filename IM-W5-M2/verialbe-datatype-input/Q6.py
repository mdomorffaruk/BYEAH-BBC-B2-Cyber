#6. Take string input and delete 3rd and last element of it. (input must be greater than 3)
input_string=input("Enter a string: ")

if(len(input_string)>3):
    third_element=input_string[2]
    last_element=input_string[len(input_string)-1]
    new_string=""
    
    for index in range(len(input_string)-1):
        if index==2:
            continue
        if index==len(input_string)-1:
            continue
        new_string=new_string+input_string[index]  

    print(new_string)
else:
    print("Please input a string that is more than 3 character long")
