import uuid
import datetime

class Limit:
    def __init__(self, limit, user_id, category_id, start_date, end_date):
        self.__id = str(uuid.uuid4())
        self.limit = limit
        self.category_id = category_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
    
    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, value):
        if value < 0:
            raise ValueError("Число должно быть больше или равно нулю")
        self.__limit = value
        
    
