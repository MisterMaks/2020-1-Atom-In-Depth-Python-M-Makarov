"""Объект http request"""
import json


class MethodError(Exception):
    """Ошибка метода"""
    pass


class HttpRequest:
    def __init__(self, host, port, method, data=None):
        self.host = host
        self.port = port
        if method not in ["GET", "POST"]:
            raise MethodError(f"method {method} does not exist")
        self.method = method
        self.data = data
        self.request_dict = {'host': host, "port": port, "method": method, "data": data}
        self.request = json.dumps(self.request_dict, ensure_ascii=False).encode("utf-8")
