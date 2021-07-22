print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("welcome to bill payer selection randomly")



names_string = input("Give me everybody's names, separated by a comma and I will pick a name randomly")
names = names_string.split(",")


import random

a= random.randint(0, len(names)-1)
print(a)

b= names[a]

print(f"{b} is going to pay bill today")

print()

but1= print(input("press enter for bye..........."))

# c=random.choice(names)
# print(f"{c} is going to buy the meal today")

