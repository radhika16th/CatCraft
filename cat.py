"""
Name: Raadhikka Gupta
Student Number: 400557687
Purpose: This program implements the Cat class, which serves as the model in the CatCraft game.
The cat has attributes which includes its health, tameness, and interactions like feeding and 
hitting. It also handles exceptions for invalid operations.
"""

# Import Statements
import random

# Cat class Implementation
class Cat:
    """
    The Cat class represents a cat in the CatCraft world, where a cat can be tame or wild,
    alive or dead, and it has health and fish in its stomach. Users can interact
    with the cat by feeding, hitting, or making it night for the cats.
    """
    
    def __init__(self, name):
        """
        The __init__ method initializes a new Cat object.
        
        Parameters:
            name: A str that has the name of the cat.
        """

        self.__name = name
        self.__is_alive = True
        self.__is_tame = False
        self.__health = 2.0
        self.__fish_fed = 0
    
    def get_name(self):
        """
        The function get_name returns the name of the cat.
        
        Returns:
            name: A str that has the name of the cat.
        """
        return self.__name
    
    def get_health(self):
        """
        The function get_health returns the current health of the cat.
        
        Returns:
            health: A float that has the health of the cat.
        """
        
        return self.__health
    
    def get_fish(self):
        """
        The function get_fish returns the number of fish the cat has eaten.
        
        Returns:
            fish_fed: An int that has the number of fish the cat currently has in his stomach.
        """
        
        return self.__fish_fed
    
    def feed_cat(self):
        """
        The function feed_cat feeds the cat a fish; it also increases health, may tame the cat, 
        and tracks the number of fish fed. If the cat eats more than 3 fish, it dies.

        Returns:
            Exception: If the cat is dead or overeats and dies.
        """
        
        if not self.__is_alive:
            raise Exception("ERROR! You can't feed a dead cat!")
        
        self.__fish_fed += 1
        
        if self.__health < 4.0: # Does not increment health if the health is already at 4.
            self.__health += 1.0
        
        if random.random() >= 0.5: # Randomizer for taming the cat.
            self.__is_tame = True
            
        if self.__fish_fed > 3: # If cat ate more fishes than it can handle; DEAD and raised exception.
            self.__is_alive = False
            self.__health = 0.0
            raise Exception("OH NO! You fed the cat a lot! It's now DEAD.")
            
    def hit_cat(self):
        """
        The functions hit_cat hits the cat, reducing its health by 1.5 (min 0), makes
        it wild and may kill it if health drops to 0.
        """ 
        
        self.__health -= 1.5
        self.__is_tame = False
        
        if self.__health < 0.0: # If health is 0, changes negative health and DEAD cat.
            self.__health = 0.0
            self.__is_alive = False
            
    def night(self):
        """
        The function night simulates nighttime, where if the cat is alive, one fish is consumed, if fish
        drops to 0, the cat becomes wild, and a tame cat with fish may leave a gift.
        
        Returns:
            str: A message if the cat left a gift or None otherwise.
        """
        
        if self.__is_alive:
            self.__fish_fed -= 1
            
            if self.__fish_fed <= 0: # Turn cat wild if fish consumed is 0.
                self.__fish_fed = 0
                self.__is_tame = False
                
            if self.__is_tame and self.__fish_fed > 0: # Leaves a gift if cat is tame and more 0 fishes fed.
                return f"{self.__name} left you a gift!"

        return
    
    def __str__(self):
        """
        The function __str__ returns a string representation of the cat's current state.
        
        Returns:
            str: A summary of the cat's state, including whether it is alive, its
                 tameness, health, and number of fish fed.
        """
        
        state_of_cat = ""
        type_of_cat = ""
        
        if self.__is_alive: # Inputs the state of the cat (alive or dead) to a variable.
            state_of_cat = "ALIVE"
        else:
            state_of_cat = "DEAD"
        
        if self.__is_tame: # Inputs the state of the cat (wild or tame) to a variable.
            type_of_cat = "Tame Cat"
        else:
            type_of_cat = "Wild Cat"
            
        return f"{state_of_cat} {type_of_cat} {self.__name}: {self.__health} health, {self.__fish_fed} fish."
