import random

#make a list of all the terms
with open("terms.txt", "r") as file:
    terms = file.read().splitlines()
#get a random term
print("\n")
while len(terms) > 0:
    number = random.randrange(len(terms))
#ask the user for their response
    user = input(f"The term is: {terms[number]}: ")
#write the response in, delete it from temp list
    with open("terms.txt", "a") as file:
        file.write(f"{terms[number]} - {user}\n")
    terms.pop(number)

print("live to fight another day")