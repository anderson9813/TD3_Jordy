#!/usr/bin/env python3
try:
     x = int(input("Entrez le premier nombre s'il vous plait: "))
     y = int(input("Entrez le deuxieme nombre s'il vous plait: "))

     z = x + y 
     print("Le resultat de", x , "+", y , "est de", z)
except:
       print("Il y a une erreur")
