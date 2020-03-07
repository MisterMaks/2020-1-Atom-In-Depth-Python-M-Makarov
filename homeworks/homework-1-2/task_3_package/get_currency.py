import requests
from .exchange_rate_api_config import ExchangeRateApi as ERA  # конфиг для API курса валют
import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_currency_data_json(currency_from):
    """Получение курса валюты относительно других валют"""
    return requests.get(ERA.api_url+currency_from).json()


def get_currency_value(currency_from, currency_to):
    """Получение значения 1 единицы валюты в другой валюте"""
    return get_currency_data_json(currency_from)['conversion_rates'][currency_to]


def get_currency_reductions():
    """Получение валютных сокращений, и сохранение их в файл, чтобы постоянно не обращаться к API"""
    try:
        with open(f"{BASE_DIR}/task_3_package/currency_reductions.json", "r") as f:
            currency_reductions = json.load(f)
    except Exception:
        currency_reductions = list(get_currency_data_json('USD')['conversion_rates'].keys())
        with open(f"{BASE_DIR}/task_3_package/currency_reductions.json", "w") as f:
            json.dump(currency_reductions, f)
    return currency_reductions


def get_currency_reductions_dict():
    """Получение нумерованного словаря валютных сокращений"""
    currency_reductions = get_currency_reductions()
    currency_reductions_dict = {}
    for i in range(1, len(currency_reductions)+1):
        currency_reductions_dict[i] = currency_reductions[i-1]
    return currency_reductions_dict


def show_currency_reductions():
    """Печать валютных сокращений"""
    currency_reductions_dict = get_currency_reductions_dict()
    result = ""
    for key, value in currency_reductions_dict.items():
        result += f"{key}: {value}\n"
    return result[:-1]
