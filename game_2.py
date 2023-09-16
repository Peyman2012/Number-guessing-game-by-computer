import random
rand = random.randint(1,100)
print(rand)
ent = " "
a = True
while a:
    if ent == "b":
        rand = random.randint(rand, 100)
        print(rand)
    elif ent == "k":
        rand = random.randint(1, rand)
        print(rand)
    elif ent == "ok":
        print("pc is good!!!!")
        break
    ent = input("Enter b or k : ")

