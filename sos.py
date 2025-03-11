import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def generate_key():
    return os.urandom(16)  
def encrypt_message(key, message):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt_message(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()
    
    return decrypted_data.decode()


key = generate_key()

message = "Давай встретимся завтра в 15:00 в кафе."

encrypted_message = encrypt_message(key, message)
print("Зашифрованное сообщение:", encrypted_message.hex())

decrypted_message = decrypt_message(key, encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def aes_encrypt(key, data):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    return encryptor.update(padded_data) + encryptor.finalize()

def aes_decrypt(key, data):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(data) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    return unpadder.update(decrypted_padded) + unpadder.finalize()

key = os.urandom(16)

# Первое сообщение
message1 = "Боб, встречаемся 10 марта в парке."
encrypted_message1 = aes_encrypt(key, message1)
print("Зашифрованное сообщение 1:", encrypted_message1.hex())

decrypted_message1 = aes_decrypt(key, encrypted_message1).decode()
print("Расшифрованное сообщение 1:", decrypted_message1)

# Второе сообщение
message2 = "Боб, встречаемся 15 марта в кафе."
encrypted_message2 = aes_encrypt(key, message2)
print("Зашифрованное сообщение 2:", encrypted_message2.hex())

# Замена последнего блока второго сообщения на последний блок первого
block_size = 16  # Размер блока AES
modified_message2 = encrypted_message2[:-block_size] + encrypted_message1[-block_size:]
print("Модифицированное зашифрованное сообщение 2:", modified_message2.hex())

# Попытка расшифровать измененное сообщение
decrypted_modified_message2 = aes_decrypt(key, modified_message2)
print("Расшифрованное модифицированное сообщение 2:", decrypted_modified_message2.decode(errors='ignore'))
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def generate_key():
    return os.urandom(16)  

def encrypt_message(key, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt_message(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    
 
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()
    
    return decrypted_data.decode()

aes_key = generate_key()
print(f"AES Key: {aes_key.hex()}")

message = input("Введите сообщение: ")

encrypted = encrypt_message(aes_key, message)
print(f"Зашифрованное сообщение: {encrypted.hex()}")

decrypted = decrypt_message(aes_key, encrypted)
print(f"Расшифрованное сообщение: {decrypted}")  (ред.)
09:18


import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
09:18


Матвей Акентьев
Матвей Акентьев
Сын космического злодея
def generate_key():
    return os.urandom(16)  

def encrypt_message(key, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt_message(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()
    
    return decrypted_data.decode()

aes_key = generate_key()

message1 = "Встреча Боба и Алисы 10 марта в кино"
encrypted1 = encrypt_message(aes_key, message1)
print(f"Зашифрованное сообщение 1: {encrypted1.hex()}")

message2 = "Встреча Боба и Алисы 15 марта в кафе"
encrypted2 = encrypt_message(aes_key, message2)
print(f"Зашифрованное сообщение 2: {encrypted2.hex()}")

block_size = 16
modified_encrypted2 = encrypted2[:-block_size] + encrypted1[-block_size:]

modified_message2 = decrypt_message(aes_key, modified_encrypted2)
print(f"Расшифрованное изменённое сообщение 2: {modified_message2}")