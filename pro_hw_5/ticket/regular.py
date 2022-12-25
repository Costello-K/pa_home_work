from datetime import datetime
from ticket import SingleTicket


class RegularSingleTicket(SingleTicket):
    def __init__(self, title, price, event_date, place='NSC «OLYMPIYSKIY»', type_use='Single',
                 type_ticket: str = 'Regular'):
        super().__init__(title, price, event_date, place, type_use)
        self.type_ticket = type_ticket

    def __str__(self):
        event = f'Event: {self.title}\n'
        type_ticket = f'{self.type_use} ticket. Type: {self.type_ticket}\n'
        price = f'Price: {self.price}\n'
        event_date = f'Event date: {self.event_date}\n'
        place = f'Place: {self.place}\n'
        return f'{"".join(i for k, i in enumerate(locals().values()) if k)}{self.number_ticket()}'

    def get_price(self):
        return self.price

    def number_ticket(self):
        return f'{RegularSingleTicket.next_number}--' + '--'.join(map(str, self.__dict__.values()))

    @staticmethod
    def get_property_ticket(number_of_ticket):
        # if need to encode and decode data in the ticket number
        # str_to_num = dict(zip(range(100, 300), "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМН"
        #      "ОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяёЁіІїЇ'`«»:;/ !#$%&()*+,-./:;<=>?@[\]^_`{|}~\""))
        # num_to_str = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮ"
        #       "ЯабвгдежзийклмнопрстуфхцчшщъыьэюяёЁіІїЇ'`«»:;/ !#$%&()*+,-./:;<=>?@[\]^_`{|}~\"", range(100, 300)))
        next_number, title, price, event_date, place, type_use, type_ticket = number_of_ticket.split('--')
        event = f'Event: {title}\n'
        type_ticket = f'{type_use} ticket. Type: {type_ticket}\n'
        price = f'Price: {price}\n'
        event_date = f'Event date: {event_date}\n'
        place = f'Place: {place}\n'
        return f'{event}{type_ticket}{price}{event_date}{place}{number_of_ticket}'


class DiscountRegularSingleTicket(RegularSingleTicket):
    def __init__(self, title, price, event_date, place, type_use, type_ticket, discount: int, tariff: str):
        super().__init__(title, price * (1 - discount/100), event_date, place, type_use, type_ticket)
        self.discount = abs(discount)
        self.tariff = tariff

    def __str__(self):
        event = f'Event: {self.title}\n'
        type_ticket = f'{self.type_use} ticket. Type: {self.type_ticket} {self.discount}%. Tariff: {self.tariff}\n'
        price = f'Price: {self.price}\n'
        event_date = f'Event date: {self.event_date}\n'
        place = f'Place: {self.place}\n'
        return f'{"".join(i for k, i in enumerate(locals().values()) if k)}{self.number_ticket()}'

    @staticmethod
    def get_property_ticket(number_of_ticket):
        next_number, title, price, event_date, place, type_use, type_ticket, discount, tariff = number_of_ticket.split('--')
        event = f'Event: {title}\n'
        type_ticket = f'{type_use} ticket. Type: {type_ticket} {discount}%. Tariff: {tariff}\n'
        price = f'Price: {price}\n'
        event_date = f'Event date: {event_date}\n'
        place = f'Place: {place}\n'
        return f'{event}{type_ticket}{price}{event_date}{place}{number_of_ticket}'


class LateMarginRegularSingleTicket(DiscountRegularSingleTicket):
    def __init__(self, title, price, event_date, place='NSC «OLYMPIYSKIY»', type_use='Single', type_ticket='Margin',
                 margin=-10, tariff='Late'):
        super().__init__(title, price, event_date, place, type_use, type_ticket, margin, tariff)

    def __setattr__(self, key, value):
        if key == 'event_date' and (datetime.strptime(value, '%Y/%m/%d %H:%M') - datetime.now()).days > 10:
            raise ValueError('This rate is not available for this date')
        self.__dict__[key] = value


class AdvanceDiscountRegularSingleTicket(DiscountRegularSingleTicket):
    def __init__(self, title, price, event_date, place='NSC «OLYMPIYSKIY»', type_use='Single', type_ticket='Discount',
                 discount=40, tariff='Advance'):
        super().__init__(title, price, event_date, place, type_use, type_ticket, discount, tariff)

    def __setattr__(self, key, value):
        if key == 'event_date' and (datetime.strptime(value, '%Y/%m/%d %H:%M') - datetime.now()).days < 60:
            raise ValueError('This rate is not available for this date')
        self.__dict__[key] = value


class StudentDiscountRegularSingleTicket(DiscountRegularSingleTicket):
    def __init__(self, title, price, event_date, place='NSC «OLYMPIYSKIY»', type_use='Single', type_ticket='Discount',
                 discount=50, tariff='Student'):
        super().__init__(title, price, event_date, place, type_use, type_ticket, discount, tariff)
        self.tariff = tariff
