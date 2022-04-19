from listener import listener
from player import player

# import os
# from colorama import Fore, Style

# # Thanks to https://stackoverflow.com/a/684344
# def clear():
#     os.system('cls' if os.name=='nt' else 'clear')

# clear()
# option = input(f"""
#   __  __                        _____ _     _             
# |  \/  | __ _  ___ _ __ ___   |_   _| |__ (_)_ __   __ _ 
# | |\/| |/ _` |/ __| '__/ _ \    | | | '_ \| | '_ \ / _` |
# | |  | | (_| | (__| | | (_) |   | | | | | | | | | | (_| |
# |_|  |_|\__,_|\___|_|  \___/    |_| |_| |_|_|_| |_|\__, |
#                                                     |___/                 
#   {Fore.GREEN}What would you like to do?{Style.RESET_ALL}

#     {Fore.GREEN}1{Style.RESET_ALL}.  Make a new macro
#     {Fore.GREEN}2{Style.RESET_ALL}.  Run an existing macro
#     {Fore.GREEN}3{Style.RESET_ALL}.  Edit a macro
#     {Fore.GREEN}4{Style.RESET_ALL}.  Delete a macro
    
# {Style.DIM}[enter a number]{Style.RESET_ALL} """)

option = input("? ")

if option == "2":
  asdf = player("foo.txt")
  asdf.play()
elif option == "1":
  with open("foo.txt", "w") as f:
    f.write("")
  hello = listener("foo.txt")
  hello.start()