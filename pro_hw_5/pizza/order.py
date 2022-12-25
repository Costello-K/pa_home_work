from waiter import Waiter
from customer import CustomerInPizzeria, CustomerWithHomeDelivery
from pizza import CustomPizza
from deliveryman import Deliveryman


class Order:
    order = 1

    def __init__(self):
        self.pizzas = {}
        self._order = Order.order

        Order.order += 1

    def __str__(self):
        order = f'Order: {self._order}\n'
        list_of_pizzas = '\n'.join(f'{key}: {val["quantity"]} x {val["price"]} = '
                                   f'{val["quantity"] * val["price"]}' for key, val in self.pizzas.items())
        total_price = f'\nTotal price: {self.total_price()}'
        return f'{order}{list_of_pizzas}{total_price}'

    def add_pizza(self, pizza: CustomPizza):
        if not isinstance(pizza, CustomPizza):
            raise ValueError

        for key, val in self.pizzas.items():
            if not set(val['base_ingredients']) ^ set(pizza.ingredients) and \
                    val['added_ingredients'] == pizza.added_ingredients:
                self.pizzas[key]['quantity'] += 1
                break
        else:
            new_name = f'{pizza.name}_type_{"".join(self.pizzas.keys()).count(pizza.name) + 1}' \
                if pizza.name in self.pizzas else pizza.name
            self.pizzas[new_name] = {'quantity': 1,
                                     'price': pizza.total_price(),
                                     'base_ingredients': pizza.ingredients,
                                     'added_ingredients': pizza.added_ingredients
                                     }

    def del_pizza(self, pizza: CustomPizza):
        if not isinstance(pizza, CustomPizza):
            raise ValueError
        if self.pizzas.get(pizza.name) or f'{pizza.name}_type_' in "".join(self.pizzas.keys()):
            for key, val in self.pizzas.items():
                if not set(val['base_ingredients']) ^ set(pizza.ingredients) and \
                        val['added_ingredients'] == pizza.added_ingredients:
                    if self.pizzas[key]['quantity'] > 1:
                        self.pizzas[key]['quantity'] -= 1
                        break
                    del self.pizzas[key]
                    break

    def total_price(self):
        return sum(val["quantity"] * val["price"] for val in self.pizzas.values())


class OrderForDelivery(Order):
    def __init__(self, customer: CustomerWithHomeDelivery, deliveryman: Deliveryman):
        super().__init__()
        self.__customer = customer
        self.__deliveryman = deliveryman

    def __str__(self):
        return f'{super().__str__()}\nClient: {self.__customer}\nDeliveryman: {self.__deliveryman}'

    def __setattr__(self, key, value):
        if key == 'customer' and not isinstance(value, CustomerWithHomeDelivery):
            raise TypeError
        if key == 'deliveryman' and not isinstance(value, Deliveryman):
            raise TypeError
        self.__dict__[key] = value


class OrderForPizzeria(Order):
    def __init__(self, customer: CustomerInPizzeria, waiter: Waiter):
        super().__init__()
        self.__customer = customer
        self.__waiter = waiter

    def __str__(self):
        return f'{super().__str__()}\nClient: {self.__customer}\nWaiter: {self.__waiter}'

    def __setattr__(self, key, value):
        if key == 'customer' and not isinstance(value, CustomerInPizzeria):
            raise TypeError
        if key == 'waiter' and not isinstance(value, Waiter):
            raise TypeError
        self.__dict__[key] = value
