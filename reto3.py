productos = {
    "manzana": 1,
    "yogur": 1,
    "leche": 2,
    "galletas": 3,
}
comprar = input("¿Qué desea comprar?")
cesta = []
total = 0
while comprar != "pagar":
    if comprar in productos:
        cesta.append(productos[comprar])
        total = total + productos[comprar]
        comprar = input("¿Desea comprar algo más?")
    else:
        comprar = input("No tenemos eso, ¿Desea comprar algo más?")
respuesta = "no tengo dinero"
respuesta2 = "toma el dinero"
paga = input(f"El precio final es {total}€.")
if paga in respuesta:
    print("No puedes llevarte los productos")
elif paga in respuesta2:
    print("Tenga un buen día")
        









