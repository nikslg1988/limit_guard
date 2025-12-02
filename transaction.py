import uuid
import datetime

class Transaction:
    def __init__(self, user_id, category_id, amount, id=None, date=None):
        self.__id = id or str(uuid.uuid4())
        self.__user_id = user_id
        self.__category_id = category_id
        self.amount = amount
        self.__date = date or datetime.datetime.now()
        
    def __str__(self):
        return f"Транзакция: {self.amount} | категория: {self.__category_id} | дата: {self.__date}"
    
    @property
    def id(self):
        return self.__id
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Число должно быть больше или равно нулю")
        self.__amount = amount
    
    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def category_id(self):
        return self.__category_id
    
    @property
    def date(self):
        return self.__date
    
    def to_dict(self):
        return {
            "id": self.__id,
            "user_id": self.__user_id,
            "category_id": self.__category_id,
            "amount": self.__amount,
            "date": self.__date.isoformat()
            
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data["user_id"],
            category_id=data["category_id"],
            amount=data["amount"],
            id=data["id"],
            date=datetime.datetime.fromisoformat(data["date"])            
        )
        
