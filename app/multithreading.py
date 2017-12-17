from PyQt5.QtCore import *
import time


class Worker(QObject):

    def __init__(self):

        super().__init__()

        self.is_running = True
        print("Hi! I'm your friendly worker and I'm being initialized.")

    def task(self):

        while self.is_running:
            print("I'm your worker and I'm running your task")
            time.sleep(1)

    def stop(self):

        self.is_running = False


class MultiThreading(QThread):

    def __init__(self):
        super().__init__()
        #self.__id = None

    def create_thread(self):

        self.__thread = QThread()
        self.__worker = Worker()
        #self.__threads.append((self.__thread, self.__worker))
        self.__worker.moveToThread(self.__thread)
        self.__thread.started.connect(self.__worker.task)
        self.__thread.start()

    def stop_thread(self):

        print("Sending stop signal to thread")
        self.__worker.stop()
        self.__thread.quit()
        self.__thread.wait()
