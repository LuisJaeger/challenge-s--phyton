nombre = input("¿Cómo te llamas?")
print("Hola," + nombre)
estado = input("¿Cómo estás?")
comoesta = ["bien", "genial", "alegre", "feliz"]
if estado in comoesta:
    print("Me alegro")
else:
    print("Lo siento")
juegofavorito = input("¿Y cual es tu videojuego favorito?")
print("Buen juego la verdad")
comida = input("De acuerdo, ahora dime ¿Cuál es tu comida favorita?")
print("La mía también")
resumen = input("¿Quieres ver un resumen de tus gustos?")
aceptar = ["sí", "si", "vale", "de acuerdo"]
if resumen in aceptar:
    print(f"Te llamas {nombre}, tu juego favorito es {juegofavorito}, tu comida favorita es {comida} y hoy te encuentras {estado}.")
else:
    print("Pues vete a tomar por culo payaso")




