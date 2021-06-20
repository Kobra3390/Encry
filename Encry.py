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

console.print("[blue]1 - Generate the Key")
console.print("[blue]2 - Ecrypt the File")
console.print("[blue]3 - Decrypt the File")
print("\n")

options = int(input("Enter an options --> "))

if(options == 1):
  Generated_key()
if(options == 2):
  Encrypt_File()
if(options == 3):
  Decrypt_file()