from colorama import init
init()
from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text', end=" ")

import random

masque=""

fichierSource = open("liste.txt","r")
tableau = fichierSource.readlines()

motMystere = tableau[random.randint (0,len(tableau))]

def masque() :
    masque=""
    for i in range (len(motMystere)):
        masque=masque+"*"
    return masque

#jeu

masque=masque()
print (masque)
print(motMystere)