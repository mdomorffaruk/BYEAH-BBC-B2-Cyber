5# 3. take a string line as input and print true if it contains "Bangladesh"
input_string=input("Enter a line: ")
constant_string="bangladesh"
if (constant_string.lower() in input_string.lower()):
  print("Input contains the word", constant_string)
else:
  print("Nothing found.. !")