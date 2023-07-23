
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas

df= pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict={row.letter:row.code for (index,row) in df.iterrows()}
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = (input("Enter a word.")).upper()
    try:
        phonetic_codes=[new_dict[letter] for letter in word]
    except KeyError as error_message:
        print("Please enter letters only.")
        generate_phonetic()
    else:
        print(phonetic_codes)

generate_phonetic()