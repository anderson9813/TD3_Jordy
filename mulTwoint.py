#!/usr/bin/env python3
try:
     x = int(input("Entrez un numero s'il vous plait: "))
     y = int(input("Entrez un deuxieme numero s'il vous plait: "))

     z = x * y
     print("Le resultat de", x , "x", y , "est de", z) 
except:
     print("Vous avez fait une erreur")
