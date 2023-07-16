import random

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
user=int(input("What do you choose? Type 1 for Rock, 2 for Paper and 3 for Scissors."))
computer=random.randint(1,3)
if user==1:
  print (rock)
elif user==2:
  print(paper)
elif user==3:
  print(scissors)

print("computer chose:\n")
if computer==1:
  print (rock)
elif computer==2:
  print(paper)
elif computer==3:
  print(scissors)

if ((user==1 and computer==3) or (user==2 and computer==1) or (user==3 and computer==2)):
  print ("You win");
elif ((computer==1 and user==3) or (computer==2 and user==1) or (computer==3 and user==2)):
  print("You lost")
else:
  print("Draw")

  


