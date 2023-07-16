from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print (art.logo)
print("Welcome to the secret auction program")

bidding_continues= True
bidders_info=[]
while bidding_continues:
  bidder={}
  bidder["name"]=input("What is your name?:")
  bidder["amount"]=int(input("Whats your bid: $"))
  bidders_info.append(bidder)
  if input("Are there any more bidders?yes/no")!="yes":
    bidding_continues=False
  clear()  

max=0
highest_bidder =""
for n in bidders_info:
  if n["amount"]>max:
    max=n["amount"]
    highest_bidder=n["name"]
    
print(f"The winner is {highest_bidder} with a bid of${max}")


