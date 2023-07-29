from sheets import Sheet
from natural_language import Exercises

user_input = input("Enter exercise details.")
exercises = Exercises()
result=exercises.estimate_calories(user_input)
sheet = Sheet()
sheet.add_data(result)
