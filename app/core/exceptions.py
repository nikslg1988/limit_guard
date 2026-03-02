class DomainError(Exception):
    """
    Базовый класс для всех доменных исключений
    """
    pass

class UserNotFoundError(DomainError):
    def __init__(self, user_id: object) -> None:
        self.user_id = user_id
        super().__init__(f"User with id={self.user_id} not found")
        
class CategoryNotFoundError(DomainError):
    def __init__(self, category_id: object) -> None:
        self.category_id = category_id
        super().__init__(f"Category with id={self.category_id} not found")
        
class CategoryOwnershipError(DomainError):
    def __init__(self, user_id: object, category_id: object) -> None:
        self.user_id = user_id
        self.category_id = category_id
        super().__init__(f"Category id={self.category_id} does not belong to user id={self.user_id}")

class LimitNotFoundError(DomainError):
    def __init__(self, user_id: object, category_id: object) -> None:
        self.user_id = user_id
        self.category_id = category_id
        super().__init__(f"Limit for user id={self.user_id} and category id={self.category_id} not found")
        
class LimitExceededError(DomainError):
    def __init__(self, user_id: object, category_id: object, limit_amount: object, current_spent: object, attempted_amount: object) -> None:
        self.user_id = user_id
        self.category_id = category_id
        self.limit_amount = limit_amount
        self.current_spent = current_spent
        self.attempted_amount = attempted_amount
        super().__init__(f"Limit exceeded for user id={self.user_id}, category id={self.category_id}. Limit={self.limit_amount}, spent={self.current_spent}, attempted={self.attempted_amount}")