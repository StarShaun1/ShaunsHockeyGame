from colorama import Fore, Back, Style, init
from time import sleep
import os
import random


init(convert=True)

play = input(Fore.GREEN + "SHAUN'S HOCKEY GAME --- Press e to enter : ")

def chances():
    maxl = 2
    minl = 1
    
    win = random.randint(minl, maxl)
    if win == 1:
        os.system("cls")
        print(Fore.GREEN + "Your puck went in the net. YOU GOT A GOAL!")
        retry = input("Play again? (y/n) : ")
            
        if retry == "y":
            game()
    else:
        os.system("cls")
        print(Fore.GREEN + "Your puck missed the net. You didn't get a goal.")
        retry = input("Play again? (y/n) : ")
            
        if retry == "y":
            game()

def shoot():
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "   ███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "      ███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "         ███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "             ███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "                 ███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "                     ███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "                         ███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "                             ███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "                                 ███")
    sleep(0.1)
    os.system("cls")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "                                     ███")
    sleep(0.1)
    chances()
    
def game():
    os.system("cls")
    print(Fore.RED + "                              ░░░░██████████░░░░░░")
    print(Fore.RED + "                              ░░░██░░░░░░░░░█████░")
    print(Fore.RED + "                              ░███████████░░░░░░██")
    print(Fore.RED + "                              █░░░░░░░░░░░█░░░░░░█")
    print(Fore.RED + "                              █░░░░░░░░░░░█░░░░░██")
    print(Fore.RED + "                              █░░░░░░░░░░░█░░░███░")
    print(Fore.RED + "                              █░░░░░░░░░░░█░██░░░░")
    print(Fore.RED + "                              █░░░░░░░░░░░██░░░░░░   The hockey net")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    puck = input(Fore.GREEN + "Enter s to shoot the puck : ")
    
    if puck == "s":
        shoot()
    else:
        game();


    


if play == "e":
    os.system("cls")
    game()