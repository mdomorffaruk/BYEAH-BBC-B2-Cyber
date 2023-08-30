import time
from tabulate import tabulate
#Open your Linux terminal or shell. Type “ pip install tabulate ” if error.

ator_total = 0
tupi_total = 0
tosbi_total = 0
kitab_total = 0
hijab_total = 0
ator_qty = 0
tupi_qty = 0
tosbi_qty = 0
kitab_qty = 0
hijab_qty = 0
print("Shop Management (Ver X.0)")

while True:

    print("Availabele Item list")
    print("=====================")
    print("1. Ator - 100 Tk\n2. Tupi - 50 Tk \n3. Tosbi - 30 Tk\n4. Kitab - 250 Tk\n5. Hijab - 150 Tk")
    print("8. Invoice")
    print("9. Exit")

    choice = input("Place your order:")

    if choice == '1':
        ator_qty = int(input("Ator quantity:")) + ator_qty
        ator_total = ator_qty * 100
        print("Check More Availabe Items. Press 4 for invoice")
    elif choice == '2':
        tupi_qty = int(input("Tupi quantity:")) + tupi_qty
        tupi_total = tupi_qty * 50
        print("More Items are available. Press 4 for invoice")
    elif choice == '3':
        tosbi_qty = int(input("Tosbi Quantity:")) +tosbi_qty
        tosbi_total = tosbi_qty * 30
        print("More Items are available. Press 4 for invoice")
    elif choice == '4':
        kitab_qty = int(input("kitab Quantity:")) + kitab_qty
        kitab_total = kitab_qty * 30
        print("More Items are available. Press 4 for invoice")
    elif choice == '5':
        hijab_qty = int(input("Hijab Quantity:")) + hijab_qty
        hijab_total = hijab_qty * 30
        print("More Items are available. Press 4 for invoice")
    elif choice == '8':
        grand_total = ator_total + tupi_total + tosbi_total + kitab_total + hijab_total
        print("\n\n\n\n** Invoice No.-  **** \n=====================+")
        print("Date:",time.strftime("%d-%m-%y") + " Time:",time.strftime("%H:%M:%S"))

        invoice = [ ['Ator', ator_qty, ator_total], ['Tupi', tupi_qty, tupi_total],
                   ['Tosbi', tosbi_qty, tosbi_total], ['Kitab', kitab_qty, kitab_total],
                   ['Hijab', hijab_qty, hijab_total]]

        #Add more item

        print(tabulate(invoice, headers=["ITEM", "QTY", "PRICE"]))

        print("========================")
        print(" \t  \t Total : ", grand_total, "Tk")
        print('\nShop Management (Ver X.0)\n@Copyright validon IT ')
        break

    elif choice == '9':
        print("Good bye ...")
        time.sleep(2)
        exit(0)
    else:
        print("Invalid choice, try again")

