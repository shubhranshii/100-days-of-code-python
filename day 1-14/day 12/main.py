#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

print(art.logo)

number_list=[]
for i in range (0,101):
  number_list.append(i)

number=random.choice(number_list)

difficulty = input(f"Welcome to the Number Guessing Game!\n,I'm thinking of a number between 1 and 100.\nThe number is {number}.\nChoose a difficulty. Type 'easy' or 'hard':")

if difficulty=="easy":
  guesses=10
else:
  guesses=5

game_not_ended=True
while game_not_ended:
  if guesses==0:
    print("You have run out of guesses. You lose")
    game_not_ended= False
  else:
    
    print(f"You have {guesses} attempts remaining to guess the number.")
    player_guess=int(input("Make a guess:"))
    if player_guess==number:
      print(f"You win. The number was {number}")
      game_not_ended=False
    elif player_guess<number:
      print("Too low")
    elif player_guess>number:
      print("Too high")
    guesses-=1
