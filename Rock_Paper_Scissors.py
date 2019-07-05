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

p1 = input("Player 1 R P or C: ")
p2 = input("Player 2 R P or C: ")

#not sure when to use elif or else or while
if p1 == p2:
    print("DRAW")
elif:
    p1 == r
    p2 == s
    print("1 Wins")
elif:
    p1 == p
    p2 == r
    print("1 Wins")
elif:
    



# valid = ["r", "p", "s"]



# # p1 = input("Player 1 type R, P or S to choose Rock, Paper or Scissors: ")
# # p2 = input("Player 2 type R, P or S to choose Rock, Paper or Scissors: ")
# p1 = input("Player 1 R P or C: ")
# p2 = input("Player 2 R P or C: ")

# while True:
#     p1 == valid
#     p2 == valid
# else:
#     print("Not Valid")

#     if p1 == p2:
#         print("Draw Game")
#     elif p1 == r and p2 == s:
#         print("Player 1 Wins!")
#     elif p1 == r and p2 == p:
#         print("Player 2 Wins")