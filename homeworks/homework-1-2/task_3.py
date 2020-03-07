# Функция для получения курса валюты относительно другой валюты
from task_3_package.get_currency import get_currency_value as gcv
# Функция для вывода валютных сокращений
from task_3_package.get_currency import show_currency_reductions as scr
# Функция для получения списка валютных сокращений
from task_3_package.get_currency import get_currency_reductions as gcr
# Функция для цветного текста
from django.utils.termcolors import colorize


def print_color(text, color='red'):
    """Функция печати в цвете. По умолчанию: красный"""
    print(colorize(text, fg=color))


class CSumCurrencies:
    """Класс для суммирования валют"""
    def __init__(self, val, currency=None):
        """Инициализируем значения по умолчанию. Если что-то не валидно, то ставим 0 для кол-ва и None для валюты"""
        if type(val) in [int, float] and val >= 0:
            self.val = val
        else:
            print_color("Не валидное кол-во валюты \nБудет установлено значение 0")
            self.val = 0
        if currency and currency not in gcr():
            print_color("Такого валютного сокращения нет \nБудет установаленно значение None")
            self.currency = None
        else:
            self.currency = currency

    def __add__(self, other):
        """Сложение валют. Здесь используются функции для получения курса валют через API"""
        self.other = other
        # Если валюты равны, то просто складываем значения
        if self.currency == self.other.currency:
            return CSumCurrencies(self.val + self.other.val, self.currency)
        # Если есть валюта первого операнда, то смотрим на валюту второго операнда
        if self.currency:
            # Если нет валюты 2-ого операнда, то приравниваем ее к первому операнду и складываем значения
            if not self.other.currency:
                self.other.currency = self.currency
                return CSumCurrencies(self.val + self.other.val, self.currency)
            # Если есть валюта у 2-ого операнда, то производим конвертацию валюты в валюту первого операнда
            # И складываем значения
            else:
                return CSumCurrencies(self.val + self.other.val * gcv(self.other.currency, self.currency),
                                      self.currency)
        # Если нет валюты у 1-ого операнда, но есть у второго, то складываем значения, а валюта будет None
        # (потому что у 1-ого операнда нет валюты)
        elif self.other.currency:
            return CSumCurrencies(self.val + self.other.val, self.currency)

    def __str__(self):
        """Приводим к читаемому виду"""
        return f"{round(self.val, 2)} {self.currency}"

    def __repr__(self):
        """Возвращает строку, скопировав которую можно получить экземпляр класса"""
        return f"СSumСurrencies({self.val}, '{self.currency}')"


"""Проверки кода"""
# print(scr())  # Печатает возможные значения валютных сокращений
# print()
#
# print(CSumCurrencies(10, 'RUB'))
# print()
#
# print([CSumCurrencies(10, 'RUB'), CSumCurrencies(20, 'USD')])
# print()
#
# print(CSumCurrencies(10, 'RUB') + CSumCurrencies(10, 'USD'))
# print()
#
# print(CSumCurrencies(10, 'USD') + CSumCurrencies(10, 'RUB'))
# print()
#
# print(CSumCurrencies(10, 'USD') + CSumCurrencies(10))
# print()
#
# print(CSumCurrencies(10) + CSumCurrencies(10, 'RUB'))
# print()
#
# print(CSumCurrencies(10) + CSumCurrencies(10))
# print()
#
# print(CSumCurrencies("ABC"))
# print()
#
# print(CSumCurrencies(123, "ABC"))
# print()
