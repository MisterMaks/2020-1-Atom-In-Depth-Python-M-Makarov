class CoolListNotValidType(Exception):
    """Ошибка если на вход CoolList был подан не список"""
    pass


class CoolListNotValidTypeItems(Exception):
    """Ошибка, если в списке в CoolList есть не int() элемент"""
    pass


class CCoolList(list):
    def __init__(self, lst):
        self.lst = lst
        self.check_list()
        self.check_list_items()

    def check_list(self):
        """Проверяем, чтобы на вход классу был подан список"""
        if type(self.lst) is not list:
            raise CoolListNotValidType("CoolList want list for __init__()")

    def check_list_items(self):
        """Проверяем, чтобы тип всех элементов списка был int()"""
        for i in self.lst:
            if type(i) is not int:
                raise CoolListNotValidTypeItems("All elements should be int()")

    def length_equalization(self):
        """Увеличиваем длину меньшего списка, добавляя в него нули"""
        difference = len(self.lst) - len(self.other.lst)  # Разница длин
        if difference > 0:
            self.other.lst += [0] * difference
        else:
            self.lst += [0] * (-difference)

    def __sub__(self, other):
        """-"""
        self.get_other_list(other)
        self.length_equalization()
        return [self.lst[i] - self.other.lst[i] for i in range(len(self.lst))]

    def __add__(self, other):
        """+"""
        self.get_other_list(other)
        self.length_equalization()
        return [self.lst[i] + self.other.lst[i] for i in range(len(self.lst))]

    def __lt__(self, other):
        """<"""
        self.get_other_list(other)
        return sum(self.lst) < sum(self.other.lst)

    def __le__(self, other):
        """<="""
        self.get_other_list(other)
        return sum(self.lst) <= sum(self.other.lst)

    def __eq__(self, other):
        """=="""
        self.get_other_list(other)
        return sum(self.lst) == sum(self.other.lst)

    def __ne__(self, other):
        """!="""
        self.get_other_list(other)
        return sum(self.lst) != sum(self.other.lst)

    def __gt__(self, other):
        """>"""
        self.get_other_list(other)
        return sum(self.lst) > sum(self.other.lst)

    def __ge__(self, other):
        """>="""
        self.get_other_list(other)
        return sum(self.lst) >= sum(self.other.lst)

    def get_other_list(self, other):
        if type(other) is list:
            self.other = CCoolList(other)
        elif type(other) is CCoolList:
            self.other = other
        else:
            raise CoolListNotValidType("Some operand has an invalid type")


"""Проверки кода"""
# print(CCoolList([1, 2, 3]) - CCoolList([4, 5]))
# print()
#
# print(CCoolList([1, 2, 3]) + CCoolList([4, 5]))
# print()
#
# print(CCoolList([1, 2, 3]) > CCoolList([4, 5]))
# print()
#
# print(CCoolList([1, 2, 3]) >= CCoolList([4, 5]))
# print()
#
# print(CCoolList([1, 2, 3]) < CCoolList([4, 5]))
# print()
#
# print(CCoolList([1, 2, 3]) <= CCoolList([4, 5]))
# print()
#
# print(CCoolList([1, 2, 3]) == CCoolList([4, 5]))
# print()
#
# print(CCoolList([1, 2, 3]) != CCoolList([4, 5]))
# print()
#
# print(CCoolList([1, 2, 3]) - [4, 5])
# print()
#
# print(CCoolList([1, 2, 3]) > [4, 5])
# print()
#
# print(CCoolList([1, 2, 3]) > "ABC")
# print()
#
# print(CCoolList([1, 2, 3]) - "ABC")
# print()
#
# print(CCoolList("afsa"))
# print()
#
# print(CCoolList(123))
# print()
