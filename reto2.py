numerosecreto = int(input("Adivina el número"))
numero = 8
while numerosecreto != numero:
    if numerosecreto <numero:
        print("demasiado bajo")
    elif numerosecreto >numero:
        print("demasiado alto")
    numerosecreto = int(input("Adivina el número"))
print("ganaste")
#al parecer si quiero que ni yo sepa el numero puedo usar: import random. Y abajo poner: numero = random.randint(1,100)


