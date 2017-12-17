from PyQt5.QtCore import *
from work import *


class Worker(QObject):

    def __init__(self, worker_id: int):

        super().__init__()

        self.is_running = True
        self.worker_id = worker_id
        print("Hi! I'm your friendly worker number %d and I'm being initialized." % self.worker_id)

    def task(self):
        index = 0
        while self.is_running:
            work(index)
            index += 1

    def stop(self):

        self.is_running = False


class MultiThreading(QThread):

    def __init__(self, worker_id: int):
        super().__init__()
        self.worker_id = worker_id

    def create_thread(self):

        self.__thread = QThread()
        self.__worker = Worker(self.worker_id)
        self.__worker.moveToThread(self.__thread)
        self.__thread.started.connect(self.__worker.task)
        self.__thread.start()

    def stop_thread(self):

        print("Sending stop signal to thread")
        self.__worker.stop()
        self.__thread.quit()
        self.__thread.wait()
