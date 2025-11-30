from user import User
from category import Category

u = User('barmagloth1976@gmail.com', '12345aA!')
cat_auto = Category('автомобиль', str(u.id))
#print(cat.name)
u.add_category(cat_auto)
print(u.__dict__)