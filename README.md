# Introduzione a Encry (IT)
*Encry* è uno script python che permette di encryptare-decryptare singoli file e cartelle. Esso è composto da 2 file: `main_function.py` che contiene tutte le funzioni per la corretta esecuzione del programma, e `Encry.py`, ossia il file main del progetto, in esso vengono richiamate le funzioni che permettono la encryptare-decryptare i file e le cartelle. Il programma è scritto nella versione di *python3*, (più nello specifico python 3.9.2) Per effettuare le operazioni la cartella e il file dovrà trovarsi nella stessa cartella dello script, e soprattutto prima di qualsiasi operazione dovrà essere generata la chiave, con essa sarà possibile fare tutto.

---
# Introduction an Encry (EN)
*Encry* is a python script that allows the user to encrypt/decrypt single file and entire folders. It is made up of two files: `Encry.py` the main file of the project, `main_function.py` wich contains all the functions used in *Encry.py*. The program is written in python3 (more specifically, in python version 3.9.2). In order to work, the file or folder to encrypt/decrypt must be in the same folder as the script, aslo, before any operation the key must be generated. 

---

# REQUISITI (IT)

I requisiti per il programma sono 2 moduli principali, il *modulo rich* e il *modulo cryptography* installabili rispettivamente:

```python
pip install rich
```
```python
pip install cryptography
```

La documentazione per il modulo cryptography può essere reperibile dal seguente link: 
> https://cryptography.io/en/latest/

---

# REQUIREMENTS (EN)

The main requirments for the program are two modules, the *rich module* and the *cryptography module*, to install them, respectively:

```python
pip install rich
```
```python
pip install cryptography
```

The documentation for the cryptography module can be found at the following link:
> https://cryptography.io/en/latest/

---

# INSTALAZIONE (IT)

Per Windows e linux:

```
$ https://github.com/Kobra3390/Encry.git
$ cd Encry
$ python Encry.py
```
O in alternativa:
```
$ python3 Encry.py
```

---

# HOW TO INSTALL (EN)

For Windows and Linux:

```
$ https://github.com/Kobra3390/Encry.git
$ cd Encry
$ python Encry.py
```
Or in alternative:
```
$ python3 Encry.py
```

---
# CARATTERISTICHE (IT)

1. *Generate the Key*: Permette la generazione di una chiave per cryptare e decryptare il file o la cartella, questa operazione va fatta prima di tutto 
2. *Encrypt the File*: Una volta generata la chiave e dando in input il nome del file questa funzione lo cryptera (il file dovrà trovarsi nella stessa cartella dello script)
3.  *Decrypt the File*: Dando in input il nome del file questa funzione lo decryptera (il file dovrà trovarsi nella stessa cartella dello script)
4. *Encrypt the Folder*: Una volta generata la chiave e dando in input il nome della cartella questa funzione cryptera tutti i file della cartella con la chiave generata in precedenza (la cartella dovrà trovarsi nella stessa cartella dello script)
5. *Decrypt the Folder*:  Dando in input il nome della cartella questa funzione decryptera tutti i file in essa contenuti (la cartella dovrà trovarsi nella stessa cartella dello script)

---

# FEATURES (EN)

*Remember*: to crypt/decrypt a file/folder, the latter must be in the same folder as the script itself. 

1. *Generate the Key*: Generates the key to encrypt and decrypt the file/folder, this operation must be done before anything else
2. *Encrypt the File*: After generating the key adn giving in input the file's name, this operation will encrypt it
3. *Decrypt the File*: After generating the key and giving in input the file's name, this operation will decrypt it
4. *Encrypt the Folder*: After generating the key and giving in input the folder's name, this operation will encrypt all the files in the folder with the same key
5. *Decrypt the Folder*: After generating the key and giving in input the folder's name, this operation will decrypt all the files in the folder