"""
Name: Raadhikka Gupta  
Student Number: 400557687  
Purpose: This program implements the CatCraft game, where players interact with cats, since the program 
has multiple Cat objects and a menu-based gameplay, brought together by importing the Cat class from 
cat.py. Players can feed or hit the cats, make nighttime for cats and receive gifts from tamed cats. 
"""

# Import statements
import cat

print("Welcome to the game, CatCraft. Here you have three pet cats that you can feed and hit, or make it nighttime for the cats that might result you in getting a gift, and quit when you're happy. Good Luck playing!")

# Initialize Cat Objects from Cat class.
name_one = str(input("Enter the name of the first cat: "))
cat_one = cat.Cat(name_one)

name_two = str(input("Enter the name of the second cat: "))
cat_two = cat.Cat(name_two)

name_three = str(input("Enter the name of the third cat: "))
cat_three = cat.Cat(name_three)

cat_list = [cat_one, cat_two, cat_three] # Make a list of all the cats.

# Main Loop
while True:
    print("\n-------------------------------------------------------")
    print("\n1. Feed\t2. Hit\t3. Night\t  4. Quit\n")
    print(f"1. {cat_one}\n2. {cat_two}\n3. {cat_three}")
    
    try:
        # User Input for selecting the what option to do.
        try:
            choice = int(input("Choice: "))
            
            if choice < 1 or choice > 4: # User entered number out of bounds (not 1 to 4).
                raise ValueError("Invalid entry! You didn't enter with the options provided.")
        except ValueError as e: # User entered value that's not a number.
            print("Error: ", e)
            continue
        
        if choice == 4: # Quit
            print("Thank you for playing CatCraft!")
            break
        
        elif choice == 1 or choice == 2: # Feed or Hit.
            # User Input for selecting the cat.
            try:
                cat_choice = int(input("For which cat? "))
                if (cat_choice < 1 or cat_choice > 3): # User entered number out of bounds (not 1 to 3).
                    raise ValueError("Invalid entry! You didn't enter with the options provided.")
            except ValueError as e:  # User entered value that's not a number.
                print("Error: ", e)
                continue
            
            if choice == 1: # Feed.
                cat_list[cat_choice-1].feed_cat() # Chooses the cat that the user enters from the cat list to feed.
                print(f"\n{cat_list[cat_choice-1].get_name()} has been fed.")
            else: # Hit.
                cat_list[cat_choice-1].hit_cat() # Chooses the cat that the user enters from the cat list to hit.
                print(f"\n{cat_list[cat_choice-1].get_name()} has been hit.")
        else: # Night.
            for current_cat in cat_list:
                gift = current_cat.night() # Make night for the current cat.
                if gift != None:
                    print(gift) # Print gift if they gave a gift.
    except Exception as e: # Catches all other excceptions.
        print(e)
