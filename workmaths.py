# Connor ter Stege
# november 12 
# something to do with math or numbers i think i kinda forgot

import random
import time

def main():
    pass
    if __name__ == "__main__":
        main() 
    
# asks for how far you need to go and how fast you will be going roughly
# responds with the estimated time to get there
# estimate traffic based on time of day asking the user what time and day it is,
# if its a friday is going to be longer than a 2am on a tuesday because of traffic
# prints the response in days, hours, minutes format

def color_judges():

    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "white", "gray"]
    judges = 5
    scores = {}

    user_colors = []
    while len(user_colors) < 5:
        color = input("gib color: ").strip().lower()
        if color in user_colors:
            print("be original smh.")
        elif color not in colors:
            print("we dont know ;p.")
            user_colors.append(color)
        else:
            user_colors.append(color)

    for color in user_colors:
        scores[color] = []
        for judge in range(judges):

            time.sleep(1)
            if color not in colors:
                score = random.randint(0, 4)  # Lower score for unknown colors
            else:
                if color in ["red", "orange", "yellow"]:
                    score = random.randint(7, 10)  # Warmer colors get higher scores
                else:
                    score = random.randint(0, 6)  # Cooler colors get lower scores
            scores[color].append(score)
            print(f"judge {judge + 1} is thinkying {color}...")
            time.sleep(0.5)
            print(f"judge {judge + 1} rated {color} a {score}.")
            time.sleep(1)

    print("\nFinal Scores:")
    for color, color_scores in scores.items():
        average_score = sum(color_scores) / len(color_scores)
        print(f"{color.capitalize()}: avg score = {average_score:.2f} (scores: {color_scores})")

color_judges()


# make a program called mcdoland that asks if u want a burger = 5$  and fries = 3$ and outputs the total cost with 14% tax

def mcdoland():
    print("burger is money and the other one is also money.")
    burger_price = 5.00
    fries_price = 3.00
    tax_rate = 0.14

    want_burger = input("Do you want a burger? (yes/no): ").strip().lower()
    want_fries = input("Do you want fries? (yes/no): ").strip().lower()

    total_cost = 0.0

    if want_burger == "yes":
        total_cost += burger_price
    if want_fries == "yes":
        total_cost += fries_price
    else:
        print("ok no food for u")
        time.sleep(1)
        
    tax_amount = total_cost * tax_rate
    total_cost += tax_amount

    print(f"Your total cost including tax is: ${total_cost:.2f}")