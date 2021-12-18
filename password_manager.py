import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, kdf
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as k:
        k.write(key)'''

'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key'''

master_pwd = input("Login: ")
password = b"master_pwd"
salt = b'\x01\xbe\xb6\xc3\x8c\xb7\xbb\xa9\x15\x04E\xad\xb5\xdfhc'b'\x1c\xa6~\x9b\xab@v\xa6\x8b\xfd\x8f\x8f\xccx\r3'b'9\xd5\xed\x0b\xa6\x83\x18\xd6B\xed\x92\xdc7\x13\x1d\x1b'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)

key = base64.urlsafe_b64encode(kdf.derive(password))
fer = Fernet(key)
      
def view():
   with open('pass.txt', 'r') as f:
       for line in f.readlines():
           #data = line.rstrip()
           user, passw = line.split(" ")
           print("Username: ", user, "| password: ", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Username: ")
    pwd = input("Password: ")

    with open('pass.txt', 'a') as f:
        f.write(name + " " + fer.encrypt(pwd.encode()).decode() + "\n")
        f.close()


while True:
    
    mode = input("1.Add new passwords 2.View existing passwords 3.Quit ")

    if mode == "3":
        print("Goodbye")
        break
    if mode == "2":
        view()
    elif mode == "1":
        add()
    else:
        print("Invalid option")
        continue

