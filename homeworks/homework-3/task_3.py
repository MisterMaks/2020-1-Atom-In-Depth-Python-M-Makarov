class MedianFinder:
    """Поиск медианы"""

    def __init__(self, nums_lst=None):
        """Инициализируем список"""
        self.nums_lst = []
        if nums_lst:
            self.nums_lst = nums_lst[:]

    def addNum(self, num: int) -> None:
        """Добавляем элемент в список"""
        self.nums_lst.append(num)

    def findMedian(self) -> float:
        """Ищем медиану"""
        median_pos = (len(self.nums_lst) / 2) - 1
        self.nums_lst.sort()
        if median_pos == int(median_pos):
            median_pos_1 = int(median_pos)
            median_pos_2 = median_pos_1 + 1
            median = (self.nums_lst[median_pos_1] + self.nums_lst[median_pos_2]) / 2
        else:
            median = self.nums_lst[int(median_pos) + 1]
        return median
