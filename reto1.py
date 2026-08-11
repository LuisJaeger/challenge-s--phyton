edad = int(input("¿Cuántos años tienes?"))
if edad < 18:
    print("no puedes pasar por ser menor")
elif edad >17 and edad <65:
    nombre = input("¿Cuál es tu nombre?")
    nombrevip = ["Daniel", "Luis", "PitilínSupremo"]
    if nombre in nombrevip:
        print("puedes pasar a la sala vip")
    else:
        print("puedes pasar a la sala estandar")
elif edad >=65:
    print("Puedes entrar por veterano")

