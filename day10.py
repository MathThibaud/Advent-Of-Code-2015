input = '1321131112'

def look_and_say(nb):
    new = ""
    i = 0
    while i < len(nb):
        current = nb[i]
        j = 1
        while i+j < len(nb) and nb[i+j] == current:
            j += 1
        new += str(j) + str(current) # new = new + str(j) + str(i) foire temporellment pour 50
        i = i + j
    return new

def question1(nb):
    for i in range(40):
        nb = look_and_say(nb)
    return len(nb)

def question2(nb):
    for i in range(50):
        nb = look_and_say(nb)
    return len(nb)



print("Advent Of The Code 2015")
print("Jour 10")
print(f"Réponse partie 1 : {question1(input)} ")
print(f"Réponse partie 2 : {question2(input)} ")   