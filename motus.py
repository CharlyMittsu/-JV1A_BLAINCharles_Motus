from colorama import init
init()
from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text', end=" ")

import random
end = False
essais=0

fichierSource = open("liste.txt","r")
tableau = fichierSource.readlines()

motMystere = tableau[random.randint (0,len(tableau))-1]

def red(mot,lettre):
    if lettre==mot:
        return True
    else:
        return False

def yellow(mot,lettre,rang):
    compte=0
    for i in range(rang):
        if mot[i]==lettre:
            compte+=1
    return compte


        
#jeu

print(motMystere)
while end == False and essais < 8:
    guess=""
    while len(guess)!=6:
        guess = input()
        if len(guess)!=6:
            print(Fore.WHITE + "Le mot doit faire 6 lettre.")
    good = 0
    for i in range (6):
        same=yellow(motMystere,guess[i],6)
        oversame=yellow(guess,guess[i],i)
        if red(motMystere[i],guess[i])==True:
            print(Fore.RED + guess[i], end="")
            good= good+1
        elif same>0 and oversame<same:
            print(Fore.YELLOW + guess[i], end="")
        else:
            print(Fore.BLUE + guess[i], end="")
    print(Fore.WHITE + "(",essais,")")
    essais+=1
    if good ==6:
        end=True
if end == True:
    print(Fore.GREEN + "gg vous avez trouvé en",essais,"éssais")
else:
    print(Fore.GREEN + "Perdu... vous avez utilisé vos",essais,"éssais")