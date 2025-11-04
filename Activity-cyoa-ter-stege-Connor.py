# connor ter stege
# cyoa i think i didnt really check the name ;p
# sept 26/25

# if u start the game and like run it again its gonna freak out i think and overlap so yeah idk <-- js kill the terminal
import random
import time
import os


altitude = -100
exit_altitude = 20
alive = True
steps = 0
health = 100
weapon_uses = 0
water = 100

print("You wake up in a dark cave...")
time.sleep(2)
print("Its cold, and you hear water dripping from the walls...")
time.sleep(2)
print("You must find your way out, You are currently at -100m below sea level, the exit is at +20m")
time.sleep(2)
name = input("You sketch your name into the wall with a stone --> ")
time.sleep(0.3)
print(f"Good luck {name}... You'll need it!!")

while alive:
    print(f"Altitude: {altitude}, Health: {health}")
    time.sleep(2)
    choice = input("You are met with two options... do you go left or right? ").strip().lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    roll = random.randint[0, 100]

    if roll <= 33:
        print("You carefully climb upwards, dodging sharp rocks...")
        altitude += 10
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif roll <= 66:
        print("You slip no wet stone and fall back down...")
        time.sleep(1)
        print("You graze your arm on a sharp stone...")
        altitude -= 5
        health -= 10
        print(f"Health: {health}")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif roll == 100:
            print("CAVE IN!")
            print("You hear rumbling all around you...")
            time.sleep(0.5)
            health = 1
            print(f"Health: {health}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

    else:
        event = random.choice(["bear", "weapon", "bandage", "cave_in", "armor"])

        if event == "bear":
            print("EVENT: BEAR!")
            if weapon_uses > 0:
                print("A bear charges! You swing your weapon and block part of the attack.")
                health -= 10
                weapon_uses -= 1
                print(f"{weapon_uses}")
                print(f"Health: {health}  (Weapon uses left: {weapon_uses})")
                time.sleep(2)
            else:
                print("A bear growls and charges! You have no weapon left and get hurt badly.")
                health -= 30
                print(f"Health: {health}")
                time.sleep(2)

        elif event == "weapon":
            print("EVENT: WEAPON!")
            print("You stumble upon a rusty weapon... you feel a little safer carrying it.")
            weapon_uses += 1
            time.sleep(1)
            print("The sword will protect you for a couple battles, but no more than two...")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif event == "bandage":
            print("EVENT: HEALING!")
            print("You find some old medical supplies...")
            time.sleep(1)
            health += 20
            if health > 100:
                health = 100
                print(f"Health: {health}")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')

        elif event == "armor":
             print("idk what to put here yet")
             health =+ 50
             print(f"Health: {health}")
             time.sleep(2)
             os.system('cls' if os.name == 'nt' else 'clear')

    if altitude >= exit_altitude:
        print("Light appears ahead! You made it!!")
        time.sleep(3)
        alive = False
        break

    if health <= 0:
        time.sleep(1)
        print("You collapse in the darkness...")
        time.sleep(3)
        alive = False
        break