#take 5 number and if any of the number is duplicate, print "can not enter a duplicate number.
def check_duplicates(numbers):
    if len(numbers) == len(set(numbers)):
        return True
    else:
        return False

def main():
    try:
        input_str = input("Enter 5 numbers comma separated: ")
        numbers = [int(num) for num in input_str.split(",")]

        if len(numbers) != 5:
            print("Please enter exactly 5 numbers separated by commas.")
            return

        if check_duplicates(numbers):
            print("True")
        else:
            print("Cannot enter duplicate numbers.")
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by commas.")

if __name__ == "__main__":
    main() 
  