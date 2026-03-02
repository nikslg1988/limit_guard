from app.models.user import User
from app.models.category import Category
from app.models.limit import Limit
from app.services.transaction_manager import TransactionManager


u = User('barmagloth1976@gmail.com', '12345aA!')
cat_auto = Category('Авто', u.id)
u.add_category(cat_auto)

limit_auto = Limit(u.id, cat_auto.id, 2000)
manager = TransactionManager([u], [cat_auto], [limit_auto], [])

transaction = manager.create_transaction(u.id, cat_auto.id, 1000)
print(transaction.to_dict())
