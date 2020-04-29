import psycopg2
import yaml
from descriptors_v_2 import Int, Text, Char, Bool


""" Конфиг БД """
with open('db_config.yaml') as f:
    db_data = yaml.safe_load(f)


class IntegerField:
    """ Целые числа """
    default = Int()
    null = Bool()

    def __init__(self, default=0, null=False):
        self.type = int
        self.int = default
        self.name = 'INTEGER'
        if not null:
            self.name = 'INTEGER NOT NULL'


class CharField:
    """ Строка """
    default = Char()
    max_len = Int()
    null = Bool()

    def __init__(self, default='', max_len=128, null=False):
        self.char = default
        self.max_len = max_len
        self.type = str
        self.name = f'VARCHAR({max_len})'
        if not null:
            self.name = f'VARCHAR({max_len}) NOT NULL'


class TextField:
    """ Текст """
    default = Text()
    null = Bool()

    def __init__(self, default='', null=False):
        self.text = default
        self.type = str
        self.name = 'TEXT'
        if not null:
            self.name = 'TEXT NOT NULL'


class BooleanField:
    """ Булевы значения """
    default = Bool()
    null = Bool()

    def __init__(self, default=False, null=False):
        self.bool = default
        self.type = bool
        self.name = 'BOOLEAN'
        if not null:
            self.name = 'BOOLEAN NOT NULL'


class Model:
    """ Методы ORM """
    def sql_request(self, command, fetch=None, lst=None):
        """
        Запрос к БД
        Если установлен fetch ('all' или 'one'), то возвращает данные в виде словаря
        Если установлен lst=True, то возвращает данные в виде списка
        """
        con = psycopg2.connect(database=db_data['db_name'], user=db_data['user'], password=db_data['password'], host=db_data['host'])
        cursor = con.cursor()
        cursor.execute(command)
        con.commit()
        data = None
        if fetch == "all":
            data = cursor.fetchall()
        if fetch == "one":
            data = [cursor.fetchone()]
        if data in [[None], None]:
            con.close()
            return None
        if lst is False:
            if fetch:
                command = f"SELECT column_name FROM information_schema.columns WHERE information_schema.columns.table_name='{self.__class__.__name__.lower()}'"
                cursor.execute(command)
                columns = [column[0] for column in cursor.fetchall()]
            data_list = []
            for values in data:
                data_dict = {}
                for column, value in zip(columns, values):
                    data_dict[column] = value
                data_list.append(data_dict)
            con.close()
            return data_list
        con.close()
        return data

    def create_table(self):
        """ Создание таблицы """
        command = f"""CREATE TABLE {self.__class__.__name__} (id INT GENERATED BY DEFAULT AS IDENTITY, {", ".join([f"{key} {value.name}" for key, value in self.__dict__.items()])})"""
        self.types_data = [value for value in self.__dict__.values()]
        self.sql_request(command)

    def check_type(self, value, type_value):
        """ Проверка типов """
        if type(value) == type_value.type:
            if 'max_len' in type_value.__dict__ and len(value) > type_value.max_len:
                raise Exception(f'len({value}) should be <= {type_value.max_len}')
        else:
            raise Exception(f'type({value}) should be {type_value.type}')

    def add(self, values):
        """ Добавление данных в таблицу """
        table_id = self.sql_request(f"SELECT max(id) FROM {self.__class__.__name__.lower()}", "one")[0][0]
        if table_id is None:
            table_id = 0
        table_id += 1
        for value, type_value in zip(values, self.types_data):
            self.check_type(value, type_value)
        command = f"""INSERT INTO {self.__class__.__name__} VALUES ({table_id}, {', '.join([f"'{str(value)}'" for value in values])})"""
        self.sql_request(command)

    def get(self, lst=False, all=False, **conditions):
        """ Получение первого совпадающего с условием значения """
        command = f'''SELECT * FROM {self.__class__.__name__} WHERE ( {", ".join([f"{key}='{value}'" for key, value in conditions.items()])} )'''
        if all is True:
            return self.sql_request(command, "all", lst)
        return self.sql_request(command, "one", lst)

    def all(self, lst=False):
        """ Вывод всех данных """
        command = f'SELECT * FROM {self.__class__.__name__}'
        return self.sql_request(command, "all", lst)

    def delete(self, **conditions):
        """ Удаление данных """
        command = f'''DELETE FROM {self.__class__.__name__} WHERE ( {", ".join([f"{key}='{value}'" for key, value in conditions.items()])} )'''
        self.sql_request(command)

    def drop(self):
        """ Удаление таблицы """
        command = f'DROP TABLE {self.__class__.__name__.lower()};'
        self.sql_request(command)

    def update(self, id, update_data):
        """ Обновление таблицы """
        command = f"""UPDATE {self.__class__.__name__} SET {", ".join([f"{column} = '{value}'" for column, value in zip(self.__dict__.keys(), update_data)])} WHERE id = {id}"""
        self.sql_request(command)


class Models:
    """ ORM """
    IntegerField = IntegerField
    CharField = CharField
    TextField = TextField
    BooleanField = BooleanField
    Model = Model
