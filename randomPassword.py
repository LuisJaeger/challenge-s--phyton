import random
digitsPassword = int(input("How many digits do you want in your password?"))
symbols = input("Do you want symbols?")
if symbols == "yes":
    manysymbols = int(input("How many symbols do you want?"))
selecteddigits = []
selectedsymbols = []
for i in range(digitsPassword):
    digits = random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    selecteddigits.append(digits)

if symbols == "yes":
    for i in range(manysymbols):
        randomsymbols = random.choice(["!", "@", "#", "€", "/", "(", ")", "=", "?"])
        selectedsymbols.append(randomsymbols)
finallist = selectedsymbols + selecteddigits
random.shuffle(finallist)
password = "".join(finallist)
print(password)