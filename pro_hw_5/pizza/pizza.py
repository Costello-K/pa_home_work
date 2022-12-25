import copy
from decimal import Decimal
from datetime import datetime
from store import data_name_pizza_day, data_ingredients_pizza, data_price_pizza, data_ingredients


# 3. Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day
# depends on the day of week. Having a pizza-of-the-day simplifies ordering for customers.
# They don't have to be experts on specific types of pizza. Also, customers can add extra
# ingredients to the pizza-of-the-day. Write a program that will form orders from customers.
class Pizza:
    def __init__(self, name: str):
        self.name = name
        self.price = Decimal(data_price_pizza[self.name]).quantize(Decimal("1.00"))
        self.ingredients = [*data_ingredients_pizza[self.name]]

    def __setattr__(self, key, value):
        if key == 'name':
            if value not in data_ingredients_pizza:
                raise ValueError('Pizza not found')
            self.__dict__[key] = value
        if key in ('price', 'ingredients'):
            self.__dict__[key] = value

    def __str__(self):
        return f'{self.name}. Price: {self.price}'

    def total_price(self):
        raise NotImplementedError


class CustomPizza(Pizza):
    def __init__(self, name):
        super().__init__(name)
        # after removing the original ingredients the price does not change
        self.original_ingredients = tuple(copy.deepcopy(self.ingredients))
        self.added_ingredients = None

    def __setattr__(self, key, value):
        if key in ('name', 'price', 'ingredients'):
            super().__setattr__(key, value)
        if key == 'original_ingredients':
            self.__dict__[key] = value
        if key == 'added_ingredients':
            self.__dict__[key] = value if data_ingredients.get(key) else {}

    def total_price(self):
        raise NotImplementedError


class PizzaDay(CustomPizza):
    def __init__(self):
        super().__init__(name=data_name_pizza_day[datetime.now().weekday()])

    def __str__(self):
        pizza = f'Pizza:\n{self.name}: {self.price}'
        additional_ingredients = '\nAdditional ingredients:\n' + \
            '\n'.join(f'{i}: {self.added_ingredients[i][0]} x {self.added_ingredients[i][1]} = '
                      f'{self.added_ingredients[i][0] * self.added_ingredients[i][1]}' for i in self.added_ingredients)
        total_price = f'\nTotal price: {self.total_price()}'
        return f'{pizza}{additional_ingredients if self.added_ingredients else ""}{total_price}'

    def add_ingredients(self, ingredient):
        if not data_ingredients.get(ingredient):
            raise ValueError('Ingredient not found')
        if ingredient in self.original_ingredients and ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
        elif self.added_ingredients.get(ingredient):
            self.added_ingredients[ingredient][0] += 1
        else:
            self.added_ingredients[ingredient] = [1, Decimal(data_ingredients[ingredient]).quantize(Decimal("1.00"))]

    def del_ingredients(self, ingredient):
        if len(self.ingredients) < 2:
            raise ValueError('You can not remove all the basic ingredients')
        if self.added_ingredients.get(ingredient) and self.added_ingredients[ingredient][0] > 1:
            self.added_ingredients[ingredient][0] -= 1
        elif self.added_ingredients.get(ingredient):
            del self.added_ingredients[ingredient]
        elif ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def total_price(self):
        return self.price + sum(quantity * price for quantity, price in self.added_ingredients.values())
