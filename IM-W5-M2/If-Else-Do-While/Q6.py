# 6. Write a program that will guess a secret string, maximum 3 guess only. with do while emulation.
string = "hello world"
attempts = 0
max_attempts=3
print("Secret String Guessing Game!")
while True:
    guess = input("Guess string: ")

    if guess == string:
        print("Congratulations! You won.")
        break
    else:
        attempts += 1
        if attempts == max_attempts:
            print(f"Sorry, you entered maximum time. The ans was :{string}")
            break
        else:
            print("Incorrect guess. Try again.")