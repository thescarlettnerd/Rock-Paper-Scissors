rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
print("Let's play Rock Paper Scissors!")
user_choice = input("Do you pick ROCK, PAPER, or SCISSORS?\n")
throw = user_choice.lower()
if throw == "rock":
  print(rock)
  pick = 0
if throw == "paper":
  print(paper)
  pick = 1
if throw == "scissors":
  print(scissors)
  pick = 2

print("\nThe computer chose: ")
cp_pick = random.randint(0, 2)
if cp_pick == 0:
  print(rock)
if cp_pick == 1:
  print(paper)
if cp_pick == 2:
  print(scissors)

if (cp_pick == 0 and pick == 0) or (cp_pick == 1 and pick == 1) or (cp_pick == 2 and pick == 2):
  print("Tie.")
if (pick == 0 and cp_pick == 1) or (pick == 1 and cp_pick == 2) or (pick == 2 and cp_pick == 0):
  print("You lose.")
if (cp_pick == 0 and pick == 1) or (cp_pick == 1 and pick == 2) or (cp_pick == 2 and pick == 0):
  print("You win.")
