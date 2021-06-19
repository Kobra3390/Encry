from cryptography.fernet import Fernet


# Function to Generate the key
def Generate_Key():
   # key generation
   key = Fernet.generate_key()
   # string the key in a file
   with open('filekey.key', 'wb') as filekey:
      filekey.write(key)

# Function to Encrypt the file using the key generated
def Encrypt_File():
   # openning the key
   with open('filekey.key', 'rb') as filekey:
      key = filekey.read()
   # using the generated key
   fernet = Fernet(key)
   # opening the original file to encrypt
   file_name = str(input("Enter a file name to encrypt: "))
   with open(file_name, 'rb') as file:
      original = file.read()
   # emcrypting the file
   encrypted = fernet.encrypt(original)
   # openint the file in write mode and 
   # writing the encryèted data
   with open(file_name, 'wb') as encrypted_file:
      encrypted_file.write(encrypted)

      
