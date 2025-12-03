import uuid
import datetime
import calendar

class Limit:
    def __init__(self,  user_id, category_id, amount):
        self.__id = str(uuid.uuid4())
        self.__category_id = category_id
        self.__user_id = user_id
        self.amount = amount
        
        today = datetime.date.today()
        _, last_day = calendar.monthrange(today.year, today.month)
        
        self.__start_date = datetime.date(today.year, today.month, 1)
        self.__end_date = datetime.date(today.year, today.month, last_day)
    
    def __str__(self):
        return f"Лимит на период с {self.start_date} по {self.end_date}: {self.amount}"
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Число должно быть больше или равно нулю")
        self.__amount = value
    
    def update_amount(self, value):
        if not isinstance(value, (int,float)) or value < 0:
            raise ValueError("Число должно быть больше или равно нулю")
        self.__amount = value
        
    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def category_id(self):
        return self.__category_id
    
    @property
    def start_date(self):
        return self.__start_date
    
    @property
    def end_date(self):
        return self.__end_date
    
