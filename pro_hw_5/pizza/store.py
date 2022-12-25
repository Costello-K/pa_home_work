from random import randint

pizza_names = ('Pizza Napoletana', 'Pizza Calzone', 'Pizza Romana', 'Pizza Siciliana', 'Pizza fritta', 'Pizza Gourmet',
               'Pizza al metro', 'Pizza al metro2', 'Pizza al metro3', 'Pizza al metro4')

data_name_pizza_day = dict(zip(range(7), pizza_names[:7]))

data_ingredients_pizza = dict.fromkeys(pizza_names, tuple([f'ing{randint(1, 20)}' for _ in range(5)]))

data_price_pizza = dict(zip(pizza_names, (randint(200, 400) for _ in range(20))))

data_ingredients = dict(zip((f'ing{i}' for i in range(1, 21)), (randint(20, 50) for _ in range(20))))
