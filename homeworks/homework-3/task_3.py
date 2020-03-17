import collections


class MedianFinder:
    """Поиск медианы"""

    def __init__(self):
        """Инициализируем упорядоченный словарь и кол-во элементов в словаре"""
        self.data = collections.OrderedDict()
        self.length = 0

    def addNum(self, num: int) -> None:
        """Добавляем элемент в словарь и увеличиваем кол-во эл-ов"""
        self.length += 1
        self.data[self.length] = num

    def findMedian(self) -> float:
        """Ищем медиану"""
        median_pos = self.length / 2
        if median_pos == int(median_pos):
            median_pos_1 = int(median_pos)
            median_pos_2 = median_pos_1 + 1
            median = (self.data[median_pos_1] + self.data[median_pos_2]) / 2
        else:
            median = self.data[int(median_pos) + 1]
        return median
