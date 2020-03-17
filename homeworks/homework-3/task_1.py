#!/usr/bin/env python
# coding: utf-8


class MaxHeap:
    """Очередь с максимальным приоритетом (max heap)"""
    def __init__(self, array):
        """Передается список и строится max heap"""
        self.array = array[:]
        self.heapify()

    def push(self, val: int) -> None:
        """Вставляется новый элемент """
        self.array.append(val)
        self.sift_up()

    def pop(self) -> int:
        """Извлечение максимального элемента"""
        maximum = self.array.pop(0)
        if len(self.array) > 0:
            self.array.insert(0, self.array.pop())
            self.sift_down(0)
        return maximum

    def heapify(self) -> None:
        """Восстановление кучи"""
        for i in range(len(self.array) // 2 - 1, -1, -1):
            self.sift_down(i)

    def sift_up(self):
        """Просеивание вверх"""
        index = len(self.array) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.array[parent] >= self.array[index]:
                return True
            self.array[index], self.array[parent] = self.array[parent], self.array[index]
            index = parent

    def sift_down(self, i):
        """Просеивание вниз"""
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.array) and self.array[left] >= self.array[i]:
            largest = left
        if right < len(self.array) and self.array[right] >= self.array[largest]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.sift_down(largest)
