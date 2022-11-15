from logger import logger
from group import Group
from student import Student


if __name__ == '__main__':
    logger.info('Started logging')
    logger.warning('Started logging to log file')

    group_1 = Group('ПЦБ1')
    data_students = [Student('Ли', 'Чу', '1999.01.07', 'КВ208347'),
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

    for i in data_students:
        try:
            group_1.add_student(i)
        except Exception as ex:
            print(f'For {i}: {ex}')

    logger.warning('Finished logging')

    print(len(group_1))
    for i in group_1[:5:]:
        print(i)
