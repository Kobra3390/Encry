from cryptography.fernet import Fernet

def Generate_Key():
   # key generation
   key = Fernet.generate_key()
   # string the key in a file
   with open('filekey.key', 'wb') as filekey:
      filekey.write(key)

      
