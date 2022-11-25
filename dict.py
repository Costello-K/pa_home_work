import operator

operation = {
    '+': operator.add,
    '*': operator.mul,
    '**': operator.pow
}

days_week = dict(zip(range(1, 8), ['Monday', 'Tuesday', 'Wednesday',
                                   'Thursday', 'Friday', 'Saturday', 'Sunday']))

roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

dict_numbers = {
    'number': dict(zip(range(20), ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                                   'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
                                   'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                                   'nineteen'])),
    'tens': dict(zip(range(1, 10), ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
                                    'seventy', 'eighty', 'ninety'])),
    'degree': dict(zip(range(1, 6), ['', 'thousand', 'million', 'billion', 'trillion']))
}

dict_cats = [
    {
        'name': 'Puma',
        'age': 9,
        'passport': {
            'seria': 'ST',
            'number': 78954575184
        }
    },
    {
        'name': 'Koks',
        'age': 6,
        'passport': {
            'seria': 'RT',
            'number': 53654575578
        }
    },
    {
        'name': 'Pufic',
        'age': 12,
        'passport': {
            'seria': 'HT',
            'number': 3455457098
        }
    }
]

ticket_type = {'regular': 100,  'advance': 60, 'student': 50, 'late': 110}

pizza_day = dict(zip(('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'),
                     ('Pizza Napoletana', 'Pizza Calzone', 'Pizza Romana', 'Pizza Siciliana', 'Pizza fritta', 'Pizza Gourmet', 'Pizza al metro')
                     ))
