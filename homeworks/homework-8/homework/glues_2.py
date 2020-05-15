"""По аналогии с Django как urls.py (склеиваем views и server)"""
from master_worker_2 import server as server_2
from views import get_web_page_data, get_web_page_words_statistics_most_common_10


server_2(func_server=get_web_page_data)
# server_2(func_server=get_web_page_words_statistics_most_common_10)
