"""views.py по аналогии с Django"""
import requests
from bs4 import BeautifulSoup
from http_response import HttpResponse, JsonResponse
from operator import itemgetter
import re


def get_web_page_data(request):
    try:
        web_page = requests.get(request).text
    except Exception:
        try:
            web_page = requests.get("https://"+request).text
        except Exception:
            web_page = requests.get("http://" + request).text
    web_page_soup = BeautifulSoup(web_page, features='html.parser')
    web_page_text = " ".join(filter(lambda word: len(word) > 0, [word for word in re.split(r"\W", web_page_soup.get_text())]))
    response = web_page_text
    return HttpResponse(data=response)


def get_web_page_words_statistics_most_common_10(request):
    try:
        web_page = requests.get(request).text
    except Exception:
        try:
            web_page = requests.get("https://"+request).text
        except Exception:
            web_page = requests.get("http://" + request).text
    web_page_soup = BeautifulSoup(web_page, features='html.parser')
    web_page_text = web_page_soup.get_text()
    web_page_words = [word.lower() for word in re.split(r'\W', web_page_text)]
    words_statistics_dict = {}
    for word in web_page_words:
        if len(word) != 0:
            if word not in words_statistics_dict:
                words_statistics_dict[word] = 1
            else:
                words_statistics_dict[word] += 1
    words_statistics_dict_most_common_10 = dict(sorted(words_statistics_dict.items(), key=itemgetter(1), reverse=True)[:10])
    return JsonResponse(data=words_statistics_dict_most_common_10)