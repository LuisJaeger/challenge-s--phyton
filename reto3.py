productos = ["manzana", "yogur", "leche", "galletas"]
comprar = input("¿Qué desea comprar?")
cesta = []
while comprar != "pagar":
    if comprar in productos:
        cesta.append(comprar)
        comprar = input("¿Desea comprar algo más?")
    else:
        comprar = input("No tenemos eso, ¿Desea comprar algo más?")
print(f"Los productos finales son: {cesta}")







