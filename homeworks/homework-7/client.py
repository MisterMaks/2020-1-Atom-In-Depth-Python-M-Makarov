"""client"""
import socket
import json
from http_request import HttpRequest

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

print("CLIENT IS RUNNING\n")

while True:
    print("Input url:")
    url = input()
    if url in ["exit", "exit()", "close", "close()"]:
        sock.close()
        print("\nCLIENT SHUT DOWN")
        break
    http_request = HttpRequest(host='localhost', port=8080, method="GET", data=url)
    sock.sendall(http_request.request)
    encode_data = sock.recv(2048)
    data = json.loads(encode_data.decode("utf-8"))
    print(f"{data}\n")
