# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n= len(names)
#print(n)
chosen= random.randint(0,n)
#print (chosen)
print(f"{names[chosen-1]} is going to buy the meal today!")