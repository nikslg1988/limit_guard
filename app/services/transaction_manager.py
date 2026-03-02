from app.models.transaction import Transaction
from app.core.exceptions import UserNotFoundError, CategoryNotFoundError, CategoryOwnershipError, LimitExceededError, LimitNotFoundError

class TransactionManager:
    def __init__(self, users, categories, limits, transactions):
        #юзеры, категории и лимиты пока что создаются вручную и добавляются в списки в ручную потом это все подключим к БД
        self.users_dict = {user.id: user for user in users}
        self.categories_dict = {category.id: category for category in categories}
        self.limits_dict = {(limit.user_id, limit.category_id): limit for limit in limits}
        self.transactions = transactions

    def _validate_user(self, user_id):
        if user_id not in self.users_dict: 
            raise UserNotFoundError(user_id)
        return self.users_dict[user_id]
    
    def _validate_category(self, category_id, user_id):
        if category_id not in self.categories_dict:
            raise CategoryNotFoundError(category_id)
        category = self.categories_dict[category_id]
        if category.user_id != user_id:
            
            raise CategoryOwnershipError(user_id, category_id)
        return category

        
    
    def _validate_limit(self, category_id, user_id):
        key = (user_id, category_id)
        if key not in self.limits_dict:
            raise LimitNotFoundError(user_id, category_id)
        return self.limits_dict[key]

    
    def create_transaction(self, user_id, category_id, amount):
        #Проверяем что юзер существует и что категория 
        user = self._validate_user(user_id)
        category = self._validate_category(category_id, user_id)
        
        #Проверяем Лимит
        limit = self.limits_dict.get((user_id, category_id))
        
        #Вычисляем сколько потрачено на данный момент
        current_spent = 0 
        for existing_transaction in self.transactions:
            if existing_transaction.user_id == user_id and existing_transaction.category_id == category_id:
                current_spent += existing_transaction.amount
        #Если лимит существует и сумма трат превышает лимит 
        if limit:
            if current_spent + amount > limit.amount:
                raise LimitExceededError(user_id, category_id, limit.amount, current_spent, amount)
              
        #Создаем объект transaction
        transaction = Transaction(user_id = user.id,
                                  category_id = category.id,
                                  amount = amount)
        self.transactions.append(transaction)
        
        return transaction
