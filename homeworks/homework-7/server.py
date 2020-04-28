import socket
from http_response import HttpResponse
import json
import logging


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    filename=u'logs/server.log')


def default_func_server(data):
    return data


def server(host='localhost', port=8080, count_listen=1, func_server=default_func_server):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    sock.bind((host, port))
    sock.listen(count_listen)

    while True:
        conn, addr = sock.accept()
        print(f"New connection from {addr}")
        while True:
            encode_request = conn.recv(2048)
            if not encode_request:
                break
            request = json.loads(encode_request.decode("utf-8"))
            print(request)
            try:
                response = func_server(request['data'])
                data_response = response.data
                status_code = response.status_code
                if data_response:
                    conn.sendall(data_response)
                else:
                    status_code = 404
                    conn.sendall(HttpResponse(status_code=404, data={'error': '404', 'message': 'not found'}).data)
                    logging.error(f"404 {request['data']}")
            except Exception as e:
                status_code = 404
                conn.sendall(HttpResponse(status_code=404, data={'error': '404', 'message': 'not found'}).data)
                logging.error(f"404 {request['data']} {e}")
            print(status_code)
        conn.close()




