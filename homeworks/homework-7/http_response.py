"""Объект http response"""
import json


class TypeDataResponseError(Exception):
    """Ошибка типа"""
    pass


class HttpResponse:
    def __init__(self, status_code=200, type_data='str', data=None):
        self.status_code = status_code
        self.type_data = type_data
        self.data = data
        if status_code == 404:
            self.data = json.dumps(self.data, ensure_ascii=False).encode("utf-8")


class JsonResponse:
    def __init__(self, status_code=200, type_data='json', data=None):
        self.status_code = status_code
        self.type_data = type_data
        self.data = data
        if type(self.data) != dict:
            raise TypeDataResponseError(f"type data responce is not valid")
        self.data = json.dumps(self.data, ensure_ascii=False).encode("utf-8")
