#SmartPass a simple program written in Python to generate secure passwords
#License: GPL3 https://www.gnu.org/licenses/gpl.html
import random
import sys
import tkinter as tk
import os

print("""
Welcome to SmartPass
  _________                      __ __________                       
 /   _____/ _____ _____ ________/  |\______   \_____    ______ ______
 \_____  \ /     \\__  \\_  __ \   __\     ___/\__  \  /  ___//  ___/
 /        \  Y Y  \/ __ \|  | \/|  | |    |     / __ \_\___ \ \___ \ 
/_______  /__|_|  (____  /__|   |__| |____|    (____  /____  >____  >
        \/      \/     \/                           \/     \/     \/

         .-:///:-.   
       `:/.     .//` 
       :/`       `/: 
       //         // 
      .//.........//.
      ///////////////
      ///////////////
      ///////////////
      ///////////////
      ///////////////
        """)
print("By Alessio Rigoli")
print("Website:agrtech.com.au")
print ("Password generator utility")
print("")
print("+++++++++++++++++++++++++++++")
while True:
    print("")
    print("Here is your random password:")
###############################################################################################
    characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#!$&(@3187%=+}{<->?"
    length = 27 #max password length which can be increased or decreased based on your needs
    RandPass = ""

    for i in range(length):
        GenPass = random.randrange(len(characters))
        RandPass = RandPass + characters[GenPass]

    print(RandPass)

    choice = input("Would you like to create a new password y/n: ")

    if choice == "y":
        print(RandPass)

    if choice == "n":
        sys.exit()
