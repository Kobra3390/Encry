from cryptography.fernet import Fernet
import os

def Generated_key():
   # key generation
   key = Fernet.generate_key()
   # string the key in a file
   with open('filekey.key', 'wb') as filekey:
      filekey.write(key)

# Function to Encrypt the file using the key generated
def Encrypt_File():
   # opening the key
   with open('filekey.key', 'rb') as filekey:
      key = filekey.read()
   # using the generated key
   fernet = Fernet(key)
   # opening the original file to encrypt
   file_name = str(input("Enter a file name to encrypt: "))
   with open(file_name, 'rb') as file:
      original = file.read()
   # encrypting the file
   encrypted = fernet.encrypt(original)
   # opening the file in write mode and 
   # writing the encrypted data
   with open(file_name, 'wb') as encrypted_file:
      encrypted_file.write(encrypted)

# Decrypt the encrypted file

def Decrypt_file():
   # opening the key
   with open('filekey.key', 'rb') as filekey:
      key = filekey.read()
   # using the key
   fernet = Fernet(key)
   # opening the encrypted file
   file_name = str(input("Enter a file name to decrypt: "))
   with open(file_name, 'rb') as enc_file:
      encrypted = enc_file.read()
   # decrypting the file
   decrypted = fernet.decrypt(encrypted)
   # opening the file in write mode and
   # writing the decrypted data
   with open(file_name,'wb') as dec_file:
      dec_file.write(decrypted)

# encrypt the folder
def Encrypt_Folder():
   # opening the key
   with open('filekey.key', 'rb') as filekey:
      key = filekey.read()
   # using the generated key
   fernet = Fernet(key)
   # opening the original folder to encrypt
   folder_name = str(input("Enter the folder name to encrypt: "))
   for files in os.scandir(folder_name):
      if files.is_file():
         with open(files, 'rb') as file:
            original = file.read()
   # encrypting the file
   encrypted = fernet.encrypt(original)
   # opening the file in write mode and 
   # writing the encrypted data
   for files in os.scandir(folder_name):
      if files.is_file():
         with open(files, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

def Decrypt_Folder():
   # opening the key
   with open('filekey.key', 'rb') as filekey:
      key = filekey.read()
   # using the generated key
   fernet = Fernet(key)
   # opening the encrypt folder
   folder_name = str(input("Enter the folder name to decrypt: "))
   for files in os.scandir(folder_name):
      if files.is_file():
         with open(files, 'rb') as enc_file:
            encrypted = enc_file.read()
         # decrypting the file
         decrypted = fernet.decrypt(encrypted)
         with open(files,'wb') as dec_file:
            dec_file.write(decrypted) 

   

