""" Здесь описаны дескрипторы для типов данных """


class Int:
    """ Дескриптор для типа INTEGER """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise Exception('type(value) != int')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Text:
    """ Дескриптор для типа TEXT """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise Exception('type(value) != str')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Char:
    """ Дескриптор для типа CHAR """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise Exception('type(value) != str')
        if len(value) > instance.max_len:
            raise Exception('len(value) > max_len')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Bool:
    """ Дескриптор для типа BOOL """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, bool):
            raise Exception('type(value) != bool')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
