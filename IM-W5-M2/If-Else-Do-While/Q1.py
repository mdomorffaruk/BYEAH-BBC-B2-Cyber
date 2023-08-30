    # 1. If you are not adult, you can't view the website, write a program that will take age as input and if age > 18, will visit the page. Also prevent them if anyone gives input negative/invalid 
input_age=input("Looking for something? Enter your age to continue: ")
adult_age=18
if(int(input_age)<adult_age):
    print("\nyou can't see or visit the website,\nTell your parents or \nCome back after 18 child.\n")
else:
    print("\nwelcome to nothing..\nContents..")
