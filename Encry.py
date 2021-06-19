import rich
from rich.console import Console 
from main_function import *

console = Console()

# ascii art
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
console.print("[blue]2 - Encrypt the File")
print("\n")

options = int(input("Enter an options --> "))

if(options == 1):
  Generate_Key()
if(options == 2):
  Encrypt_File()