import uuid

class Category:
    def __init__(self, name, user_id):
        self.__id = str(uuid.uuid4())
        self.name = name
        self.__user_id = user_id
    
    @property
    def id(self):
        return self.__id
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError ("Категория должна быть строкой и не должна быть пустой")
        self.__name = name
        
    @property
    def user_id(self):
        return self.__user_id