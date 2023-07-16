# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
lname= name.lower()
t=lname.count("t")
r=lname.count("r")
u=lname.count("u")
e=lname.count("e")
d1= t + r + u + e

l=lname.count("l")
o=lname.count("o")
v=lname.count("v")
e=lname.count("e")
d2= l + o + v + e

score= d1*10 + d2

if score < 10 or score >90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score <50:
    print(f"Your score is {score}, you are alright together.")    
else:
    print(f"Your score is {score}.")    