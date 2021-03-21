#!/usr/bin/env python3
def mul(x, y):
    output = x * y
    return output


def add(x, y):
    output = x + y
    return output

ask = input("Voulez vous additionner ou multiplier? (Add ou Mul): ")
if (ask.lower() == "add"):

    p = input("Voulez vous additionner deux entier? (oui ou non): ")

    if (p.lower()) =="oui":
        x = input(" Entrez un premier numero s'il vous plait: ")
        while isinstance(x, str):
            try:
                x = int(x)
            except:
                x = input("vous n'avez pas entrer un numero\nEntrez un numero: ")
        y = input(" Entrez un deuxieme numero s'il vous plait: ")
        while isinstance(y, str):
            try: 
                y = int(y)
            except:
                y = input("Vous n'avez pas entrer un numero\nEntrez un numero: ")
        print("Le resultat de", x , "+", y , "est de", add(x, y))
    else:
        print("Desole nous ne pourrons pas proceder a votre requete")


else:
     p = input("Voulez vous multiplier deux entier? (Oui ou Non): ")
     if (p.lower() == "oui"):
         x = input("Entrez un premier numero s'il vous plait: ")
         while isinstance(x, str):
             try:
                 x = int(x)
             except:
                 x = input("Vous n'avez pas entre un numero\nEntrez un numero: ")


         y = input("Entrez le premier numero s'il vous plait: ")
         while isinstance(y, str):
             try:
                 y = int(y)
             except:
                 y = input("Vous n'avez pas entrer de numero\nEntrez un numero: ")

         print("Le resultat de", x , "*", y , "est de ", mul(x, y))
     else:
         print("Desole nous ne pourrons pas proceder a votre requete")
