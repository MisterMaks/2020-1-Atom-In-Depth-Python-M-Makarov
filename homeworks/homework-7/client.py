import socket
import json
from http_request import HttpRequest

while True:
    print("Input url:")
    url = input()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_request = HttpRequest(host='localhost', port=8080, method="GET", data=url)
    sock.connect((http_request.host, http_request.port))
    sock.sendall(http_request.request)
    encode_data = sock.recv(2048)
    data = json.loads(encode_data.decode("utf-8"))
    sock.close()
    print(data)
