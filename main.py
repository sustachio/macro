from listener import listener
from player import player
from shutil import get_terminal_size

import os
from colorama import Fore, Style

# Thanks to https://stackoverflow.com/a/684344
def reset():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"""{Fore.GREEN} __  __                        _____ _     _             
|  \/  | __ _  ___ _ __ ___   |_   _| |__ (_)_ __   __ _ 
| |\/| |/ _` |/ __| '__/ _ \    | | | '_ \| | '_ \ / _` |
| |  | | (_| | (__| | | (_) |   | | | | | | | | | | (_| |
|_|  |_|\__,_|\___|_|  \___/    |_| |_| |_|_|_| |_|\__, |
                                                    |___/{Style.RESET_ALL}""")

size = get_terminal_size((80, 20))

def Run():
  reset()
  # list out all of the macros in the macros folder
  files = os.listdir("macros")
  print(f"  {Fore.CYAN}Here are your current macros:{Style.RESET_ALL}\n")
  
  if files:
    # pring all of the file with their size
    for i, file in enumerate(files):
      # file size in KB
      file_size = str(round(os.path.getsize(f"macros/{file}")/1000, 1))
      # spacing between file and filesize
      spacing = " "*(35-len(file)-len(str(i+1)))
      
      print(f"      {Fore.GREEN}{i+1}{Style.RESET_ALL} {file}{spacing}{file_size}KB")
      
  else:
    print(f"      {Fore.RED}You have no macros right now.{Fore.GREEN}")
      
  # spacing to the bottom
  print("\n"*(size.lines-10-len(files)))
  asdf = input("?")
  # asdf = player("macros/foo.txt")
  # asdf.play()

def Make():
  with open("foo.txt", "w") as f:
    f.write("")
  hello = listener("macros/foo.txt")
  hello.start()

def Home():
  reset()
  print(f"""  {Fore.CYAN}What would you like to do?{Style.RESET_ALL}

      {Fore.GREEN}1{Style.RESET_ALL}.  Make a new macro
      {Fore.GREEN}2{Style.RESET_ALL}.  Run an existing macro
      {Fore.GREEN}3{Style.RESET_ALL}.  Edit a macro
      {Fore.GREEN}4{Style.RESET_ALL}.  Delete a macro""")
  print("\n"*(size.lines-14)) # space it to the top of the terminal
  option = input(f"{Style.DIM}[enter a number]{Style.RESET_ALL} ")

  if option == "1":
    Make()
  elif option == "2":
    Run()
  
  
    
  

Home()