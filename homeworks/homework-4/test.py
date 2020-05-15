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


bla_bla_table = BlaBlaTable()
# bla_bla_table.create_table()

# bla_bla_table.add({"bla_int": 7, "bla_char": "Bla", 'bla_text': 'BlaBla'})
# bla_bla_table.add_list((2020, "Bla_1", 'BlaBla_1', True))
#
# print(bla_bla_table.get(bla_int=7))
# print(bla_bla_table.all())
#
# bla_bla_table.delete(bla_int=7)
#
# bla_bla_table.update({'bla_int': 2021, 'bla_char': "Bla_1", 'bla_text': 'BlaBla_1', 'bla_bool': True}, id=2)
# bla_bla_table.update_id_with_list(2, [2020, "Bla_2020", 'BlaBla_2020', True])
bla_bla_table.drop()

