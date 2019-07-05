"""
rock beats: scissors
paper beats: rock
scissors beat: paper

rock looses to: paper
paper looses to: rock
scissors loose to: rock

rock draws with rock
paper draws with paper
scissors draws with scissors

# """

r = "rock"
p = "paper"
s = "scissors"

# # ensures the game contines to play after win sequence has completed
while True:
    p1 = input("Player 1 R P or C: ").lower()
    p2 = input("Player 2 R P or C: ").lower()
    
    if p1 == p2:
        print("Draw")
        
    elif p1 == r and p2 == p:
        print("paper wins")
    elif p1 == r and p2 == s:
        print("rock wins")
    elif p1 == p and p2 == r:
        print("paper wins")
    elif p1 == p and p2 == s:
        print("scissors win")
    elif p1 == s and p2 == r:
        print("rock wins")
    elif p1 == s and p2 == p:
        print("scissors win")













"""idea to make this a network game and randomise who goes first"""
