"""
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

R	P
R	S
P	R
P	S
S	R
S	P
"""
rock = "r"
paper = "p"
scissors = "s"
# ensures the game contines to play after win event has completed
while True:
    p1 = input("Player 1 r p or s: ").lower()
    p2 = input("Player 2 r p or s: ").lower()
    if p1 == p2:
        print("Draw")
    elif p1 == rock and p2 == paper:
        print("Paper wins")
    elif p1 == rock and p2 == scissors:
        print("rock wins")
    elif p1 == paper and p2 == rock:
        print("scissors wins")
    elif p1 == paper and p2 == scissors:
        print("scissors win")
    elif p1 == scissors and p2 == rock:
        print("rock wins")
    elif p1 == scissors and p2 == paper:
        print("scissors wins")


"""idea to make this a network game and randomise who goes first"""
