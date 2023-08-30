while True:
    print("=============MEAL MANAGEMENT=============")
    print("1. Add Money")
    print("2. Add Meal")
    print("3. Count")
    choice = int(input("Enter your choice: "))

    name1 = "Rashed"
    name2 = "Alfaj"
    name3 = "Nadim"
    name4 = "Asad"
    name5 = "Badhon"
    name6 = "Sajib"

    rashed_money = 0
    alfaj_money = 0
    nadim_money = 0
    asad_money = 0
    badhon_money = 0
    sajib_money = 0

    rashed_meal = 0
    alfaj_meal = 0
    nadim_meal = 0
    asad_meal = 0
    badhon_meal = 0
    sajib_meal = 0

    if choice == 1:
        print(f"1. {name1}")
        print(f"2. {name2}")
        print(f"3. {name3}")
        print(f"4. {name4}")
        print(f"5. {name5}")
        print(f"6. {name6}")
        print("7. See total per person")

        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            amount1 = int(input("Enter amount: "))
            rashed_money += amount1
        elif choice1 == 2:
            amount2 = int(input("Enter amount: "))
            alfaj_money += amount2
        elif choice1 == 3:
            amount3 = int(input("Enter amount: "))
            nadim_money += amount3
        elif choice1 == 4:
            amount4 = int(input("Enter amount: "))
            asad_money += amount4
        elif choice1 == 5:
            amount5 = int(input("Enter amount: "))
            badhon_money += amount5
        elif choice1 == 6:
            amount6 = int(input("Enter amount: "))
            sajib_money += amount6
        elif choice1 == 7:
            print("=============MONEY SPENT=============")
            print(f"{name1} spent total == {rashed_money}")
            print(f"{name2} spent total == {alfaj_money}")
            print(f"{name3} spent total == {nadim_money}")
            print(f"{name4} spent total == {asad_money}")
            print(f"{name5} spent total == {badhon_money}")
            print(f"{name6} spent total == {sajib_money}")
            print("=====================================")
        else:
            print("Invalid Choice")

    elif choice == 2:
        print(f"1. {name1}")
        print(f"2. {name2}")
        print(f"3. {name3}")
        print(f"4. {name4}")
        print(f"5. {name5}")
        print(f"6. {name6}")
        print("7. See total :")

        choice2 = int(input("Enter your choice: "))
        if choice2 == 1:
            meal_1 = int(input("Enter meal amount: "))
            rashed_meal += meal_1
        elif choice2 == 2:
            meal_2 = int(input("Enter amount: "))
            alfaj_meal += meal_2
        elif choice2 == 3:
            meal_3 = int(input("Enter amount: "))
            nadim_meal += meal_3
        elif choice2 == 4:
            meal_4 = int(input("Enter meal amount: "))
            asad_meal += meal_4
        elif choice2 == 5:
            meal_5 = int(input("Enter meal amount: "))
            badhon_meal += meal_5
        elif choice2 == 6:
            meal_6 = int(input("Enter meal amount: "))
            sajib_meal += meal_6
        elif choice2 == 7:
            print("=============MEAL COUNT=============")
            print(f"{name1} total meal == {rashed_meal}")
            print(f"{name2} total meal == {alfaj_meal}")
            print(f"{name3} total meal == {nadim_meal}")
            print(f"{name4} total meal == {asad_meal}")
            print(f"{name5} total meal == {badhon_meal}")
            print(f"{name6} total meal == {sajib_meal}")
            print("====================================")
        else:
            print("Invalid Choice")

    elif choice == 3:
        print("=============FULL STATISTICS=============")
        total_money = rashed_money + alfaj_money + nadim_money + asad_money + badhon_money + sajib_money
        total_meal = rashed_meal + alfaj_meal + nadim_meal + asad_meal + badhon_meal + sajib_meal
        if total_meal == 0:
            meal_rate = 1
        else:
            meal_rate = total_money / total_meal
        rashed = meal_rate * rashed_meal
        alfaj = meal_rate * alfaj_meal
        nadim = meal_rate * nadim_meal
        asad = meal_rate * asad_meal
        badhon = meal_rate * badhon_meal
        sajib = meal_rate * sajib_meal
        print(f"Total money spent = {total_money}")
        print(f"Meal rate = {meal_rate}")
        print("-----------------------------------------")
        print(f"{name1} ate {rashed_meal} meals and have to pay {rashed_money - rashed} Taka.")
        print(f"{name2} ate {alfaj_meal} meals and have to pay {alfaj_money - alfaj} Taka.")
        print(f"{name2} ate {nadim_meal} meals and have to pay {nadim_money - nadim} Taka.")
        print(f"{name4} ate {asad_meal} meals and have to pay {asad_money - asad} Taka.")
        print(f"{name5} ate {badhon_meal} meals and have to pay {badhon_money - badhon} Taka.")
        print(f"{name6} ate {sajib_meal} meals and have to pay {sajib_money - sajib} Taka.")
        print("==========================================")
        break
    else:
        print("Invalid Choice")