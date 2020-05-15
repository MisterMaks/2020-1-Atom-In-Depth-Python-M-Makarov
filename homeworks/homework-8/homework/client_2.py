"""client"""
import socket
import json
from http_request import HttpRequest
import time
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8081))

print("CLIENT IS RUNNING\n")

urls = ["https://mail.ru", "https://google.com", "https://yandex.ru"] * 10

http_request = HttpRequest(host='localhost', port=8080, method="GET", data=urls)
sock.sendall(http_request.request)

start_time = datetime.datetime.now()
while True:
    encode_data = sock.recv(2048 * 100)
    data = encode_data.decode("utf-8")
    # data = json.loads(encode_data.decode("utf-8"))
    print(f"{data}\n")

sock.close()
print("\nCLIENT SHUT DOWN")