import unittest
from orm_v_2 import Models
import psycopg2
import yaml


""" Конфиг БД """
with open('db_config.yaml') as f:
    db_data = yaml.safe_load(f)


class BlaBlaTable(Models.Model):
    """ Таблица для тестов """
    def __init__(self):
        self.bla_int = Models.IntegerField()
        self.bla_char = Models.CharField(max_len=128)
        self.bla_text = Models.TextField()
        self.bla_bool = Models.BooleanField(null=True)


def db_request(command):
    """ Функция для запросов к БД """
    con = psycopg2.connect(database=db_data['db_name'], user=db_data['user'], password=db_data['password'], host=db_data['host'])
    cursor = con.cursor()
    cursor.execute(command)
    result = cursor.fetchall()
    con.close()
    return result


class MyTestCase(unittest.TestCase):
    """ Тесты """

    bla_bla_table = BlaBlaTable()

    def test_orm(self):
        """ Тесты """

        # Проверяем, что таблица еще не создана
        command = "SELECT table_name FROM information_schema.tables"
        tables = [table[0] for table in db_request(command)]

        self.assertFalse(self.bla_bla_table.__class__.__name__.lower() in tables)

        # Создаем таблицу
        self.bla_bla_table.create_table()

        # Проверяем, что таблица существует
        command = "SELECT table_name FROM information_schema.tables"
        tables = [table[0] for table in db_request(command)]

        self.assertTrue(self.bla_bla_table.__class__.__name__.lower() in tables)

        # Проверяем, что создались соответствующие столбцы
        command = f"SELECT column_name FROM information_schema.columns WHERE information_schema.columns.table_name='{self.bla_bla_table.__class__.__name__.lower()}';"
        columns = [column[0] for column in db_request(command)]

        self.assertEqual(columns, ['id', 'bla_int', 'bla_char', 'bla_text', 'bla_bool'])

        # Добавляем данные в БД и проверяем, что они там есть
        self.bla_bla_table.add({"bla_int": 7, "bla_char": "Bla", 'bla_text': 'BlaBla'})  # Добавляем данные через именованные аргументы
        self.bla_bla_table.add_list((2020, "Bla_1", 'BlaBla_1', True))  # Добавляем данные списком

        command = "SELECT * FROM blablatable"
        data = db_request(command)

        self.assertEqual(data, [(1, 7, "Bla", 'BlaBla', None), (2, 2020, "Bla_1", 'BlaBla_1', True)])

        # Проверяем get() и all()
        self.assertEqual(self.bla_bla_table.get(bla_int=7),
                         [{'id': 1, 'bla_int': 7, 'bla_char': 'Bla', 'bla_text': 'BlaBla', 'bla_bool': None}])

        self.assertEqual(self.bla_bla_table.all(),
                         [{'id': 1, 'bla_int': 7, 'bla_char': 'Bla', 'bla_text': 'BlaBla', 'bla_bool': None}, {'id': 2, 'bla_int': 2020, 'bla_char': 'Bla_1', 'bla_text': 'BlaBla_1', 'bla_bool': True}])

        # Проверяем delete
        self.bla_bla_table.delete(bla_int=7)

        self.assertIsNone(self.bla_bla_table.get(bla_int=7))

        # Проверяем update
        self.bla_bla_table.update({'bla_int': 2021, 'bla_char': "Bla_1", 'bla_text': 'BlaBla_1', 'bla_bool': True}, id=2)  # update для именовынных аргументов

        self.assertIsNotNone(self.bla_bla_table.get(bla_int=2021))

        self.bla_bla_table.update_id_with_list(2, [2020, "Bla_2020", 'BlaBla_2020', True])  # update для id без названий столбцов

        self.assertIsNotNone(self.bla_bla_table.get(bla_int=2020))

        # Проверяем drop
        self.bla_bla_table.drop()
        command = "SELECT table_name FROM information_schema.tables"
        tables = [table[0] for table in db_request(command)]

        self.assertFalse(self.bla_bla_table.__class__.__name__.lower() in tables)


if __name__ == '__main__':
    unittest.main()
