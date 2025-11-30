import uuid
import re
import hashlib
import os

class User:
    def __init__(self, email, password):
        self.__id = str(uuid.uuid4())
        self.email = email
        self.__salt = os.urandom(16)
        self.categories = []
        self.password = password # валидацию пароля
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            raise ValueError ("Неправильный Email")
        self.__email = value
        
    @property
    def id(self):
        return self.__id
    
    @property
    def password(self):
        raise AttributeError("Нельзя получить значение пароля")

    @password.setter
    def password(self, value):
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).+$', value) or len(value) < 8:
            raise ValueError("Пароль должен содержать как минимум одну заглавную букву, одну цифру и один символ и быть больше или равен 8 символам")
        self.__password = self._hash_password(value)
          
    @property
    def salt(self):
        return self.__salt
    
    
    def _hash_password(self, raw_password):
        byte_password = raw_password.encode("utf-8")
        hash_hex = hashlib.sha256(self.__salt + byte_password).hexdigest()
        return hash_hex
             
    def check_password(self, raw_password):  #TODO
        hash_check = self._hash_password(raw_password)
        return hash_check == self.__password
    
    def add_category(self, category):
        if category.user_id != self.__id:
            raise ValueError ("Категория принадлежит другому пользователю")
        self.categories.append(category)
    

