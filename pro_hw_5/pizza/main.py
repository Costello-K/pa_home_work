from pizza import PizzaDay
from order import OrderForPizzeria, OrderForDelivery
from waiter import Waiter
from customer import CustomerInPizzeria, CustomerWithHomeDelivery
from deliveryman import Deliveryman


if __name__ == '__main__':
    p_d_1 = PizzaDay()
    p_d_2 = PizzaDay()
    p_d_3 = PizzaDay()
    p_d_4 = PizzaDay()

    print(p_d_1.__dict__)
    p_d_1.del_ingredients('ing1')
    p_d_1.del_ingredients('ing2')
    p_d_1.add_ingredients('ing1')
    p_d_1.add_ingredients('ing10')
    p_d_1.add_ingredients('ing10')
    p_d_1.add_ingredients('ing10')
    p_d_1.add_ingredients('ing12')
    p_d_1.add_ingredients('ing13')
    p_d_1.add_ingredients('ing14')
    p_d_1.add_ingredients('ing15')
    p_d_1.add_ingredients('ing15')
    print(p_d_1.__dict__)
    p_d_1.del_ingredients('ing12')
    p_d_1.del_ingredients('ing10')
    p_d_1.del_ingredients('ing10')
    p_d_1.del_ingredients('ing10')
    p_d_1.del_ingredients('ing10')
    print(p_d_1.__dict__)
    print(p_d_1.total_price())

    p_d_2.add_ingredients('ing12')
    p_d_2.add_ingredients('ing16')

    p_d_3.add_ingredients('ing16')
    p_d_3.add_ingredients('ing12')

    print(p_d_1)
    print(p_d_2)

    customer_1 = CustomerInPizzeria('Anton', 'Petrov', 23)
    customer_2 = CustomerWithHomeDelivery('Anton', 'Petrov', '+0635457878')
    print(customer_1)

    waiter_1 = Waiter('Тетяна', 'Гушко')
    print(waiter_1)

    order_1 = OrderForPizzeria(customer_1, waiter_1)
    order_1.add_pizza(p_d_1)
    order_1.add_pizza(p_d_2)
    order_1.add_pizza(p_d_2)
    order_1.add_pizza(p_d_3)
    order_1.add_pizza(p_d_4)
    order_1.del_pizza(p_d_1)
    print('*' * 50)
    print(order_1)

    deliveryman_1 = Deliveryman('Gog', 'Gogovich', '+380635895568')
    order_2 = OrderForDelivery(customer_2, deliveryman_1)
    order_2.add_pizza(p_d_1)
    order_2.add_pizza(p_d_2)
    order_2.add_pizza(p_d_2)
    order_2.add_pizza(p_d_3)
    order_2.add_pizza(p_d_4)
    order_2.add_pizza(p_d_4)
    order_2.add_pizza(p_d_4)
    order_2.del_pizza(p_d_4)
    order_2.del_pizza(p_d_1)
    order_2.add_pizza(p_d_1)
    print('*' * 50)
    print(order_2)
