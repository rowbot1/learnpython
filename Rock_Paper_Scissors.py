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

"""
"""idea to make this a network game and randomise who goes first"""

r = "rock"
p = "paper"
s = "scissors"

valid = ["r", "p", "s"]



# player_1 = input("Player 1 type R, P or S to choose Rock, Paper or Scissors: ")
# player_2 = input("Player 2 type R, P or S to choose Rock, Paper or Scissors: ")

while True:
    p1 = input("Player 1 R P or C: ")
    p2 = input("Player 2 R P or C: ")

    if p1 == p2:
        print("Draw Game")
    elif p1 == r and p2 == s:
        print("Player 1 Wins!")
    elif p1 == r and p2 == p:
        print("Player 2 Wins")