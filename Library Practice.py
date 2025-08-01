#Importing Libraries
import random

#List
teams = ("alpha", "beta", "charlie", "delta")
numb = random.randint(4,15)

#randomly list a team
print(f"you are in the {numb}th {random.choice(teams)} squad")
