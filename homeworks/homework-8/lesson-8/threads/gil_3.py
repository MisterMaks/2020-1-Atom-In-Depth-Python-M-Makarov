import threading

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self, name="threddy" + num)
        self.num = num

    def run(self):
        print("Thread", self.num)

thread2 = MyThread("2")
thread2.run()