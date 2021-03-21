#!/usr/bin/env python3
def mul(x, y):
    output = x * y
    return output 
x = input("Entrez un numero s'il vous plait: ")
while isinstance(x, str):
    try:
        x = int(x)
    except:
        x = input("vous avez manque un numero\nENtrez un numero: ")

y = input("Entrez un deuxieme numero s'il vous plait: ")
while isinstance(y, str):
    try:
        y = int(y)
    except:
        y = input("vous n'avez pas entrer de numero\nEntrez un numero: ")
     
print("Le resultat de", x , "x", y , "est de", mul(x, y)) 
