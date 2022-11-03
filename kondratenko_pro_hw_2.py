from logger import logger
from group import Group
from dict import students


if __name__ == '__main__':
    logger.info('Started logging')
    logger.warning('Started logging to log file')

    group_1 = Group('ПЦБ1')

    for i in students:
        try:
            group_1.add_student(i)
        except Exception as ex:
            print(f'For {i}: {ex}')

    logger.warning('Finished logging')
