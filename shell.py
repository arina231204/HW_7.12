from restaurant.models import *

user1 = Client(user = User.objects.create(email='nikname21@gmail.com', password='defender4'),
               name='Азат Соколов', card_name=4147565798789009 )
user1.save()

user2 = Worker(user = User.objects.create(email='altywa1998@gmail.com', password='nono34'),name='Алтынай Алиева', position='Оператор кассы')
user2.save()

dish1 = Food(name='Шаурма', start_price=50)
dish1.save()

dish2 = Food(name='Гамбургер', start_price=25)
dish2.save()

ingredient1 = Ingredient(name='сыр', extra_price=10)
ingredient1.save()

ingredient2 = Ingredient(name='курица', extra_price=70)
ingredient2.save()

ingredient3 = Ingredient(name='говядина', extra_price=80)
ingredient3.save()

ingredient4 = Ingredient(name='салат', extra_price=15)
ingredient4.save()

ingredient5 = Ingredient(name='фри', extra_price=15)
ingredient5.save()

dish1.orders.set([ingredient3,ingredient1,ingredient4,ingredient5],through_defaults={'client': user1,
                                                                                         'worker':user2})
dish2.orders.set([ingredient2,ingredient4],through_defaults={'client': user1,
                                                             'worker':user2})

price_dish1 =(ingredient3.extra_price + ingredient1.extra_price + ingredient4.extra_price + ingredient5.extra_price +dish1.start_price)
print(price_dish1)

price_dish2 =(ingredient2.extra_price + ingredient4.extra_price + dish2.start_price)
print(price_dish2)



