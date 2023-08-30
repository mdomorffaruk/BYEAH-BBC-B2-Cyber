# 9. is it vegetable or fruit? can you determine it with a programme?
vegetable ={
  "apple" : "Fruit",
  "banana" : "Fruit",
  "orange" : "Fruit",
  "carrot" : "Vegetable",
  "broccoli" : "Vegetable",
  "spinach" : "Vegetable"
}

input_value = input("Please input a name: ").lower()

if input_value in vegetable.keys():
    print (vegetable.get(input_value))
else:
    print("input is not in the list")
