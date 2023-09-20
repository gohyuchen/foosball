import random
import sys


class Player:
    """
    docstring1
    docstring2
    """
    def __init__(self, name, position, atk_attr, def_attr, shots):
        self.name = name
        self.position = position
        self.atk_attr = atk_attr
        self.def_attr = def_attr
        self.shots = shots
        
    def __str__(self):
        return f"{self.name} plays the {self.position} position, with base stats of {self.atk_attr}+{self.def_attr}"

    def attack(self):
        print(f"{self.name} attacks using the {str(skills_dict[self][random.randint(0,2)])} skill!")


Tom     = Player(
            name = "Tom",
            position = "Back", 
            atk_attr = 8, 
            def_attr = 6,
            shots = 2
            )
Billy   = Player(
            name = "Billy",
            position = "Forward", 
            atk_attr = 9, 
            def_attr = 8,
            shots = 2
            )
Jon     = Player(
            name = "Jon",
            position = "Back", 
            atk_attr = 9, 
            def_attr = 9,
            shots = 2
            )
Alicia  = Player(
            name = "Alicia",
            position = "Forward", 
            atk_attr = 9, 
            def_attr = 9,
            shots = 3
            )

skills_dict = {
    Tom:    ["confusing dribble between 3 bar",
                "bank shot",
                "Tom Special",
            ],
    Billy:  ["slow shot from 3 bar side man",
                "straight down the center",
                "THE RIGHT HAND",
            ],
    Jon:    ["2 bar see no ball",
                "front pin",
                "lucky shot",
            ],
    Alicia: ["Hiyah!",
                "Hoosah!",
                "Aieeeieieieieieiee",
            ],              
}


def str_to_class(classname):
    """
    convert input string to Class Object if match
    """
    return getattr(sys.modules[__name__], classname)

print('Enter your first player:')
p1 = input()
print('Enter your second player:')
p2 = input()
print(f"Your 2 players are {p1} and {p2}")

Player1 = str_to_class(p1)
Player2 = str_to_class(p2)

print(Player1)
print(Player2)
print('\n #### BEGIN ####')
print('\n')


# Game
while Player1.shots > 0:
    Player1.attack()
    score_chance = random.randint(1,5)+ Player1.atk_attr - Player2.def_attr
    if score_chance >= 4:
        print('SCOREEEEEEEE')
        break
    print(f"OH NO! {Player1.name} MISSES")
    
    Player1.shots -= 1
