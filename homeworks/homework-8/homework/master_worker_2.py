import socket
import json
from config import SIZE
import logging
import os
import signal
from multiprocessing.dummy import Pool as ThreadPool
from http_response import HttpResponse, JsonResponse
import threading


global count_url


# Логирование
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    filename=u'logs/server.log')


def default_func_server(data):
    """Просто дефолтная функция"""
    return data


def finish(signal_num, frame):
    global count_url
    print("\n---------- \n")
    print(f"----- Count URL: {count_url} ----- \n")
    print("DAEMON STOP")
    raise SystemExit()


def server(size=SIZE, host='localhost', port=8081, count_listen=10, func_server=default_func_server):
    """Сервер"""

    signal.signal(signal.SIGUSR1, finish)

    global count_url
    count_url = 0

    lock = threading.Lock()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    sock.bind((host, port))
    sock.listen(count_listen)

    print(f"pid={os.getpid()}\n")

    print("SERVER IS RUNNING\n")

    while True:
        conn, addr = sock.accept()

        def send_response(url, func=func_server, conn=conn, lock=lock):
            try:
                response = func(url)
                data_response = response.data
                status_code = response.status_code
                if data_response:
                    lock.acquire()
                    global count_url
                    count_url += 1
                    conn.sendall(data_response)
                    # self.conn.sendall(JsonResponse(data={'message': self.message}).data)
                    lock.release()
                else:
                    status_code = 404
                    conn.sendall(
                        HttpResponse(status_code=404, data={'error': '404', 'message': 'not found'}).data)
                    logging.error(f"404 {url}")
            except Exception as e:
                status_code = 404
                conn.sendall(HttpResponse(status_code=404, data={'error': '404', 'message': 'not found'}).data)
                logging.error(f"404 {url} {e}")
            print(f"Get data from <{url}> status code {status_code}\n")

        print(f"New connection from {addr}\n")
        while True:
            encode_request = conn.recv(2048 * 10)
            if not encode_request:
                print()
                break
            request = json.loads(encode_request.decode("utf-8"))
            print(request)
            print()
            request_data = request['data']
            # print(request_data)

            pool = ThreadPool(size)
            pool.map(send_response, request_data)
            pool.close()
            pool.join()

        conn.close()



