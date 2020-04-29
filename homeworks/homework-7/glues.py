"""По аналогии с Django как urls.py (склеиваем views и server)"""
from server import server
from views import get_web_page_words_statistics_most_common_10


server(func_server=get_web_page_words_statistics_most_common_10)
