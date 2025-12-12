from app.models.user import User
from app.models.category import Category
from app.models.transaction import Transaction
from limit_guard.app.services.transaction_manager import TransactionManager

u = User('barmagloth1976@gmail.com', '12345aA!')
cat_auto = Category('автомобиль', str(u.id))
#print(cat.name)
u.add_category(cat_auto)

transaction = Transaction(str(u.id), str(cat_auto.name), 1000)
print(transaction.__dict__)