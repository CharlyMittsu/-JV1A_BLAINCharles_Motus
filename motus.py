from colorama import init
init()
from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text', end=" ")

import random

fichierSource = open("liste.txt","r")
tableau = fichierSource.readlines()
