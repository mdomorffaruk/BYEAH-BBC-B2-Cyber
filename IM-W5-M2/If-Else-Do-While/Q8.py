# 8. make a simple program to determine that you can pass a road or not. the road has traffic signals, red, green and blue.

x = input("what is the signal? 1.red 2.green or 3.bule? :(type: 1,2,3): ")

if x == "1":
  print("You can't pass the road")
elif x=="2":
  print("you can pass the road")
elif x == "3":
  print("wait for the green signal")
else:
  print("Invalid input")
