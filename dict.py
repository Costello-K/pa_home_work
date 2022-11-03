from pro_hw_2.student import Student


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
    'degree': dict(zip(range(5), ['', 'thousand', 'million', 'billion', 'trillion']))
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

students = [Student('Ли', 'Чу', '1999.01.07', 'КВ208347'),
            Student('Ли2', 'Чун', '1999.02.21', 'КВ907341'),
            Student('Ли3', 'Чао', '1999.03.16', 'КВ218542'),
            Student('Ли4', 'Гао', '1999.04.06', 'КВ958349'),
            Student('Ли5', 'Чад', '1999.05.25', 'КВ908346'),
            Student('Ли6', 'Чан', '1999.06.30', 'КВ108342'),
            Student('Ли7', 'Чад', '1999.07.12', 'КВ708746'),
            Student('Ли8', 'Хун', '1999.08.03', 'КВ508346'),
            Student('Ли9', 'Хо', '1999.09.30', 'КВ108346'),
            Student('Ли10', 'Чук', '1999.10.08', 'КВ958379'),
            Student('Ли11', 'Ч', '1999.10.08', 'КВ96789')
            ]
