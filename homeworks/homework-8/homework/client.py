"""client"""
import time
import socket
import json
from http_request import HttpRequest

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

print("CLIENT IS RUNNING\n")

urls = ["https://mail.ru", "https://google.com", "https://yandex.ru"] * 10

for url in urls:
    http_request = HttpRequest(host='localhost', port=8080, method="GET", data=url)
    sock.sendall(http_request.request)
    encode_data = sock.recv(2048 * 10)
    data = encode_data.decode("utf-8")
    # data = json.loads(encode_data.decode("utf-8"))
    print(f"{data}\n")

sock.close()
print("\nCLIENT SHUT DOWN")