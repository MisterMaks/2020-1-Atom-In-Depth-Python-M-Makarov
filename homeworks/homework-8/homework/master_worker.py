import threading
from queue import Queue
import socket
import json
from http_response import HttpResponse, JsonResponse
from config import SIZE
import logging
import os
import signal


global count_url


# Логирование
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    filename=u'logs/server.log')


def default_func_server(data):
    """Просто дефолтная функция"""
    return data


class ServerThread(threading.Thread):
    def __init__(self, q, lock, func, conn, thread_id=0):
        threading.Thread.__init__(self)
        self.q = q
        self.lock = lock
        self.func = func
        self.conn = conn
        self.message = f"Thread #{thread_id}"

    def run(self):
        while True:
            content = self.q.get()

            try:
                response = self.func(content['data'])
                data_response = response.data
                status_code = response.status_code
                if data_response:
                    self.lock.acquire()
                    global count_url
                    count_url += 1
                    self.conn.sendall(data_response)
                    # self.conn.sendall(JsonResponse(data={'message': self.message}).data)
                    self.lock.release()
                else:
                    status_code = 404
                    self.conn.sendall(HttpResponse(status_code=404, data={'error': '404', 'message': 'not found'}).data)
                    logging.error(f"404 {content['data']}")
            except Exception as e:
                status_code = 404
                self.conn.sendall(HttpResponse(status_code=404, data={'error': '404', 'message': 'not found'}).data)
                logging.error(f"404 {content['data']} {e}")
            print(f"{status_code}\n")


def build_worker_pool(q, lock, size, func, conn):
    workers = []
    for i in range(size):
        worker = ServerThread(q, lock, func, conn, i)
        worker.setDaemon(True)
        worker.start()
        workers.append(worker)
    return workers


def finish(signal_num, frame):
    global count_url
    print("\n---------- \n")
    print(f"----- Count URL: {count_url} ----- \n")
    print("DAEMON STOP")
    raise SystemExit()


def server(size=SIZE, host='localhost', port=8080, count_listen=10, func_server=default_func_server):
    """Сервер"""

    signal.signal(signal.SIGUSR1, finish)

    global count_url
    count_url = 0

    lock = threading.Lock()
    q = Queue()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    sock.bind((host, port))
    sock.listen(count_listen)

    print(f"pid={os.getpid()}\n")

    print("SERVER IS RUNNING\n")

    while True:
        conn, addr = sock.accept()

        worker_threads = build_worker_pool(q, lock, size, func_server, conn)

        print(f"New connection from {addr}\n")
        while True:
            encode_request = conn.recv(2048 * 10)
            if not encode_request:
                print()
                break
            request = json.loads(encode_request.decode("utf-8"))
            print(request)

            q.put(request)

        for worker in worker_threads:
            worker.join()

        conn.close()



