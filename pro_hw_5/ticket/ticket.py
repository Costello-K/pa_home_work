from datetime import datetime
from decimal import Decimal


# 2. Write a program for selling tickets to IT-events. Each ticket has a unique number and a price.
# There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days before
# the event), late ticket (purchased fewer than 10 days before the event) and student ticket.
# Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# -the ability to construct a ticket by number;
# -the ability to ask for a ticket’s price;
# -the ability to print a ticket as a String.
class Ticket:
    next_number = 1

    def __init__(self, title: str, price: int | float):
        self.title = title
        self.price = Decimal(price).quantize(Decimal("1.00"))

        Ticket.next_number += 1

    def __str__(self):
        raise NotImplementedError


class SingleTicket(Ticket):
    def __init__(self, title, price, event_date: str, place: str, type_use: str):
        super().__init__(title, price)
        self.event_date = datetime.strptime(event_date, '%Y/%m/%d %H:%M').strftime('%Y/%m/%d %H:%M')
        self.place = place
        self.type_use = type_use

    def __str__(self):
        raise NotImplementedError
