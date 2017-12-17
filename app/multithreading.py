from PyQt5.QtCore import *
from work import *



class Worker(QObject):

    def __init__(self):

        super().__init__()

        self.is_running = True
        print("Hi! I'm your friendly worker and I'm being initialized.")

    def task(self):
        index = 0
        while self.is_running:
            work(index)
            index += 1

    def stop(self):

        self.is_running = False


class MultiThreading(QThread):

    def __init__(self):
        super().__init__()

    def create_thread(self):

        self.__thread = QThread()
        self.__worker = Worker()
        self.__worker.moveToThread(self.__thread)
        self.__thread.started.connect(self.__worker.task)
        self.__thread.start()

    def stop_thread(self):

        print("Sending stop signal to thread")
        self.__worker.stop()
        self.__thread.quit()
        self.__thread.wait()
