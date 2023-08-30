#write a program that will calculate GPA.

#write a program that will calculate GPA.

maths = float(input("Enter values of maths: "))
english = float(input("Enter values of english: "))
bangla = float(input("Enter values of bangla: "))

avg_marks = (maths + english + bangla) / 3

if avg_marks > 100:
  print("the marks cannot be above 100")
elif avg_marks > 79:
  print("You got GPA 5.0")
elif avg_marks > 59 and avg_marks < 80:
  print("You got GPA 4.0")
elif avg_marks > 39 and avg_marks < 60:
  print("You got GPA 3.0")
else:
  print("Sorry you failed")
