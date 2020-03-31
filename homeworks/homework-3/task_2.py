import collections


class ICache:
    """LRU Cache"""

    def __init__(self, capacity: int = 10) -> None:
        """Инициализируем размер кэша и упорядоченный словарь"""
        self.capacity = capacity
        self.cache_dict = collections.OrderedDict()

    def get(self, key: str) -> str:
        """Получаем значение по ключу и перемещаем в конец"""
        self.cache_dict.move_to_end(key)
        return self.cache_dict[key]

    def set(self, key: str, value: str) -> None:
        """Если не превышаем размер кэша, то добавляем в конец
        Если превышаем, то удаляем первый элемент, и добавляем в конец"""
        if self.capacity > 0:
            self.cache_dict[key] = value
            self.capacity -= 1
        else:
            self.cache_dict.popitem(last=False)
            self.cache_dict[key] = value

    def del_item(self, key: str) -> None:
        """Удаляем элемент по ключу"""
        self.cache_dict.pop(key)
        self.capacity += 1
