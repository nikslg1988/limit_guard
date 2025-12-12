from models.transaction import Transaction

class TransactionManager:
    def __init__(self, users, categories, limits, transactions):
        #юзеры, категории и лимиты пока что создаются вручную и добавляются в списки в ручную потом это все подключим к БД
        self.users_dict = {user.id: user for user in users}
        self.categories_dict = {category.id: category for category in categories}
        self.limits_dict = {(limit.user_id, limit.category_id): limit for limit in limits}
        self.transactions = transactions

    def _validate_user(self, user_id):
        if user_id not in self.users_dict:
            raise ValueError("Пользователь не найден")
        return self.users_dict[user_id]
    
    def _validate_category(self, category_id, user_id):
        if category_id not in self.categories_dict:
            raise ValueError("Категория не найдена")
        category = self.categories_dict[category_id]
        if category.user_id != user_id:
            raise ValueError("Категория принадлежит другому пользователю")
        return category

        
    
    def _validate_limit(self, category_id, user_id):
        key = (user_id, category_id)
        if key not in self.limits_dict:
            raise ValueError("Лимит не найден")
        return self.limits_dict[key]

    
    def create_transaction(self, user_id, category_id, amount):
        #Проверяем что юзер существует и что категория 
        user = self._validate_user(user_id)
        category = self._validate_category(category_id, user_id)
        
        #Проверяем Лимит
        try:
            limit = self._validate_limit(category_id, user_id)
        except ValueError:
            limit = None
        
        if limit:
            if amount > limit.amount:
                raise ValueError(f"Транзакция на {amount} превышает лимит "
                                 f"{limit.amount} по категории '{category.name}'")
        
        #Создаем объект transaction
        transaction = Transaction(user_id = user.id,
                                  category_id = category.id,
                                  amount = amount)
        
        self.transactions.append(transaction)
        
        return transaction
    