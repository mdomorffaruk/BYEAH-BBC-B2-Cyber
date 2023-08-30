# 7. if you get 40% in exam , you'll pass.. write a program that if you are pass or not. Input will be your python exam result.
print('Input your result')
result = input()
result = int(result)
if result >= 40:
  print('You passed')
elif result < 40:
  print("You failed")
else:
  print("Invalid input")