#!/usr/bin/env python3

def add(x, y):
     output = x + y
     return output
x = input("Entrez le premier nombre s'il vous plait: ")
while isinstance(x, str):
    try:
         x = int(x)
    except:
         x = input("vous n'avez pas entre de numero.\nEntrez le premier nombre")
print()
y =input("Entrez le deuxiem numero s'il vous plait: ")
while isinstance(y, str):
    try:
         y = int(y)
    except:
         y = input("Vous n'avez pas entrer de numero\n entrer le deuxieme nombre")
print(add(x, y))
