import rich
from rich.console import Console 
from main_function import *

console = Console()

console.print("""[yellow]
▓█████  ███▄    █  ▄████▄   ██▀███ ▓██   ██▓
▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒
▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░
▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░
░▒████▒▒██░   ▓██░▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░
░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ 
 ░ ░  ░░ ░░   ░ ▒░  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ 
   ░      ░   ░ ░ ░          ░░   ░ ▒ ▒ ░░  
   ░  ░         ░ ░ ░         ░     ░ ░     
                  ░                 ░ ░     
""")

console.print("[blue]1 - Generate a Key")
print("\n")

options = int(input("Enter an options --> "))

if(options == 1):
   Generate_Key()