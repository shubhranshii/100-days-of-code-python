import random
import art
import game_data
from replit import clear

#print logo
print(art.logo)

#define a function called play_game. begin with generating two random entries from list

def play_game():
  A=random.choice(game_data.data)
  B=random.choice(game_data.data)

  game_not_over=True
  
  while game_not_over:
    score=0
    print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")
    print(art.vs)
    print(f"Compare B: {B['name']}, a {B['description']} from {B['country']}")
    user_choice=input("Who has more followers? Type 'A' or 'B':")
    if user_choice=='A':
      user=A
      other=B
    else:
      user=B
      other=A

    if user['follower_count']>other['follower_count']:
      score+=1
      clear()
      A=user
      B=random.choice(game_data.data)


    else:
      print(f"Your score is {score}. Game over.")
      game_not_over=False
  

play_game()