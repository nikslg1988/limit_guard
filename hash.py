import hashlib
import os

salt = os.urandom(16)

password = input("Введите данные для хэширования: ")
hash_psw = hashlib.sha256(salt + password.encode("utf-8")).hexdigest()
print(hash_psw)