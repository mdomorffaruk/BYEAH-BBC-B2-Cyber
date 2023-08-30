import time
import platform
import os

import shutil
terminal_width = shutil.get_terminal_size().columns

def center_input(prompt):
    terminal_width = shutil.get_terminal_size().columns
    padding = (terminal_width - len(prompt)) // 2
    user_input = input(" " * padding + prompt)
    return user_input

class Weapon:
    def __init__(self, name, price, ammo=None):
        self.name = name
        self.price = price
        self.ammo = ammo

class Shop:
    def __init__(self):
        self.weapons = []
        self.ammo = []

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_ammo(self, ammo):
        self.ammo.append(ammo)
      
    def generate_invoice(self, cart):
        
        try:
            # total = sum(item[3] for item in cart)
            if len(cart)==0:
                print("Nothing to invoice, bye for now.\nBTW, thanks for visiting...".center(terminal_width))
            else:
                with open("invoice.txt", "w") as file:
                # print(welcome_message.center(80, '-'))
                    print("\n\n".center(terminal_width))
                    print("----------------------------------------------------------------".center(terminal_width))
                    print("|                             Invoice                          |".center(terminal_width))
                    print("----------------------------------------------------------------".center(terminal_width))
                    print(f"|{'':<16}Date:{time.strftime('%d-%m-%y')} Time:, {time.strftime('%H:%M:%S')} {'':<16}|".center(terminal_width))
                    print("----------------------------------------------------------------".center(terminal_width))
                    print(f"{'| #':<2} {'Name':<36}| {'Qty':<5}| {'Price':<5} | {'Total':<5} |".center(terminal_width))

                    file.write("\n\n\n")
                    file.write("----------------------------------------------------------------\n")
                    file.write("|                             Invoice                          |\n")
                    file.write("----------------------------------------------------------------\n")
                    file.write(f"|{'':<16}Date:{time.strftime('%d-%m-%y')} Time:, {time.strftime('%H:%M:%S')} {'':<16}|\n")
                    file.write("----------------------------------------------------------------\n")
                    file.write(f"{'| #':<2} {'Name':<36}| {'Qty':<5}| {'Price':<5} | {'Total':<5} |\n")
                    total = 0
                    # cart.append((weapon.name,quantity,weapon.price, f"Ammo for {weapon.name}", ammo_quantity,ammo.price))
                    # cart.append((weapon.name, quantity, weapon.price))
                    for i, item in enumerate(cart, start=1):
                        if len(item) == 3:
                            total = total + (item[1]*item[2])
                            print(f"|{i:2d}. {item[0]:<35}| {item[1]:<5}| ${item[2]:<5}|".center(terminal_width))
                            file.write(f"|{i:2d}. {item[0]:<35}| {item[1]:<5}| ${item[2]:<5}|\n")
                        elif len(item) == 6:
                            total = total + (item[1]*item[2]) +(item[4]*item[5])
                            print(f"|{i:2d}. {item[0]:<35}| {item[1]:<5}| ${item[2]:<5}| ${(item[2]*item[1]):<5}|".center(terminal_width))
                            file.write(f"|{i:2d}. {item[0]:<35}| {item[1]:<5}| ${item[2]:<5}| ${(item[2]*item[1]):<5}|\n")
                            # ammo_item = next((a for a in cart if a[0] == f"Ammo for {item[0]}".center(terminal_width)), None)
                            ammo_item = [item[4],item[5]]
                        
                            if ammo_item:
                                print(f"|{i:2d}. {item[3]:<35}| {ammo_item[0]:<5}| ${ammo_item[1]:<5}| ${(ammo_item[0]*ammo_item[1]):<5}|".center(terminal_width))
                                file.write(f"|{i:2d}. {item[3]:<35}| {ammo_item[0]:<5}| ${ammo_item[1]:<5}| ${(ammo_item[0]*ammo_item[1]):<5}|\n")

                    print("----------------------------------------------------------------".center(terminal_width))
                    print(f"| Total{' ':<48}| ${total:<5}|".center(terminal_width))
                    print("----------------------------------------------------------------".center(terminal_width))
                    print("Check invoice.txt to get the invoice in file".center(terminal_width))
                    file.write("----------------------------------------------------------------\n")
                    file.write(f"| Total{' ':<48}| ${total:<5}|\n")
                    file.write("----------------------------------------------------------------\n")
                    
        except:
            print("Something is wrong... Try again!".center(terminal_width))

def main():
    shop = Shop()


    # Adding weapons
    weapons_data = [
        {"name": "M16 Rifle", "price": 800, "ammo": 0},
        {"name": "Glock 17 Pistol", "price": 500, "ammo": 1},
        {"name": "AK-47 Assault Rifle", "price": 700, "ammo": 2},
        {"name": "Beretta M9 Pistol", "price": 450, "ammo": 3},
        {"name": "Remington 870 Shotgun", "price": 600, "ammo": 4},
        {"name": "MP5 Submachine Gun", "price": 650, "ammo": 5},
        {"name": "Barrett M82 Sniper Rifle", "price": 1500, "ammo": 6},
        {"name": "RPG-7 Rocket Launcher", "price": 1200, "ammo": 7},
        {"name": "M249 Light Machine Gun", "price": 900, "ammo": 8},
        {"name": "FN P90 Submachine Gun", "price": 750, "ammo": 9},
        {"name": "Plasma Blaster", "price": 800, "ammo": 10},
        {"name": "Nanoblade Pistol", "price": 500, "ammo": 11},
        {"name": "Quantum Disruptor Rifle", "price": 700, "ammo": 12},
        {"name": "Ionized Particle Cannon", "price": 450, "ammo": 13},
        {"name": "Void Infuser Shotgun", "price": 600, "ammo": 14},
        {"name": "Neuroshock SMG", "price": 650, "ammo": 15},
        {"name": "Photon Pulse Sniper", "price": 1500, "ammo": 16},
        {"name": "Fusion Warhammer", "price": 1200, "ammo": 17},
        {"name": "Neutron Phaser LMG", "price": 900, "ammo": 18},
        {"name": "Temporal Rift Launcher", "price": 750, "ammo": 19},
    ]

    # Adding ammo
    ammo_data = [
        Weapon(name="M16 Rifle Ammo", price=20),
        Weapon(name="Glock 17 Pistol Ammo", price=10),
        Weapon(name="AK-47 Assault Rifle Ammo", price=15),
        Weapon(name="Beretta M9 Pistol Ammo", price=8),
        Weapon(name="Remington 870 Shotgun Ammo", price=5),
        Weapon(name="MP5 Submachine Gun Ammo", price=12),
        Weapon(name="Barrett M82 Sniper Rifle Ammo", price=50),
        Weapon(name="RPG-7 Rocket Launcher Ammo", price=200),
        Weapon(name="M249 Light Machine Gun Ammo", price=25),
        Weapon(name="FN P90 Submachine Gun Ammo", price=10),
        Weapon(name="Plasma Blaster Ammo", price=30),
        Weapon(name="Nanoblade Pistol Ammo", price=15),
        Weapon(name="Quantum Disruptor Rifle Ammo", price=25),
        Weapon(name="Ionized Particle Cannon Ammo", price=15),
        Weapon(name="Void Infuser Shotgun Ammo", price=10),
        Weapon(name="Neuroshock SMG Ammo", price=20),
        Weapon(name="Photon Pulse Sniper Ammo", price=75),
        Weapon(name="Fusion Warhammer Ammo", price=0),
        Weapon(name="Neutron Phaser LMG Ammo", price=35),
        Weapon(name="Temporal Rift Launcher Ammo", price=20),
    ]




    for weapon_data in weapons_data:
        shop.add_weapon(Weapon(**weapon_data))

    for ammo in ammo_data:
        shop.add_ammo(ammo)

    cart = []
    clear_cmd = ""
    
    if platform.system() == 'Windows':
        clear_cmd = "cls"
    elif platform.system() == 'Linux':
        clear_cmd="clear"
    
    count =0
    while True:
        os.system(clear_cmd)
        if count>0:
            print("You can generate invoice by entering Q/q".center(terminal_width))
        print(f"executing {clear_cmd} command in 1 secound.".center(terminal_width))
        time.sleep(1)
        os.system(clear_cmd)

        print("----------------------------------------------------------------".center(terminal_width))
        print("|                                                              |".center(terminal_width))
        print("|   Greetings, Warrior! Arm Yourself and Unleash Your Power!   |".center(terminal_width))
        print("|                                                              |".center(terminal_width))
        print("----------------------------------------------------------------".center(terminal_width))
        print(f"| Weapons:{'':<53}|".center(terminal_width))
        for i, weapon in enumerate(shop.weapons, start=1):
            print(f"| {i:2d}. {weapon.name:<47}: ${weapon.price:<7}|".center(terminal_width))
        print("----------------------------------------------------------------".center(terminal_width))
        
        print("NOTE: Type Q/q to generate invoice and exit".center(terminal_width))
        print("Enter weapon numbers and weapons quantity or".center(terminal_width))
        print("Only weapon_number i.e: 1,1 2,2 5,4 ...".center(terminal_width) )
        weapon_choices = center_input("").split(",")


        if 'q' in weapon_choices or 'Q' in weapon_choices:
            shop.generate_invoice(cart)
            exit()  # Exit the program after generating invoice
        else:
            for weapon_choice in weapon_choices:
                if weapon_choice == '0':
                    break  # Exit the loop without generating invoice
                try:
                    parts = weapon_choice.split()
                    index = int(parts[0]) - 1
                    if len(parts) > 1:
                        quantity = int(parts[1])
                    else:
                        quantity = 1
                    weapon = shop.weapons[index]
                    
                    if weapon.ammo is not None and int(weapon.ammo) >= 0:  # Change condition to >= 0
                        ammo_quantity = int(center_input(f"Enter ammo quantity for {weapon.name}: "))
                        ammo = shop.ammo[int(weapon.ammo)]  # Access ammo by index
                        cart.append([weapon.name,quantity,weapon.price, f"Ammo for {weapon.name}", ammo_quantity,ammo.price])
                    else:
                        # total = weapon.price * quantity
                        cart.append([weapon.name, quantity, weapon.price])
                except:
                    os.system(clear_cmd)
                    print("Take a look at the input format. You insert wrong... ".center(terminal_width))
                    time.sleep(2)
        count=count+1


if __name__ == "__main__":
    main()

