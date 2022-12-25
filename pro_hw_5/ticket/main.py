from regular import RegularSingleTicket, AdvanceDiscountRegularSingleTicket, StudentDiscountRegularSingleTicket, \
    LateMarginRegularSingleTicket


if __name__ == '__main__':
    print(RegularSingleTicket('IT', 7, '2023/12/6 14:00'))
    print('*' * 5)
    print(RegularSingleTicket.get_property_ticket('2--IT--7.00--2023/12/06 14:00--NSC «OLYMPIYSKIY»--Single--Regular'))
    print('*' * 60)
    print(AdvanceDiscountRegularSingleTicket('IT', 7, '2023/5/12 8:00'))
    print('*' * 5)
    print(AdvanceDiscountRegularSingleTicket.get_property_ticket(
        '3--IT--4.20--2023/05/12 08:00--NSC «OLYMPIYSKIY»--Single--Discount--40--Advance'))
    print('*' * 60)
    print(StudentDiscountRegularSingleTicket('IT', 7, '2023/12/12 14:00'))
    print('*' * 5)
    print(StudentDiscountRegularSingleTicket.get_property_ticket(
        '4--IT--3.50--2023/12/12 14:00--NSC «OLYMPIYSKIY»--Single--Discount--50--Student'))
    print('*' * 60)
    print(LateMarginRegularSingleTicket('IT', 7, '2023/1/3 23:00'))
    print('*' * 5)
    print(LateMarginRegularSingleTicket.get_property_ticket(
        '5--IT--7.70--2023/01/03 23:00--NSC «OLYMPIYSKIY»--Single--Margin--10--Late'))
