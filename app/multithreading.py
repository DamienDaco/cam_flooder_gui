from PyQt5.QtCore import *


class Worker(QObject):

    def __init__(self):

        super(Worker, self).__init__()

        print("Hi! I'm your friendly worker and I'm being initialized")

    def task(self):

        print("I'm your worker and I'm running your task")


class MultiThreading():
    def __init__(self):
        super(MultiThreading, self).__init__()

    def create_thread(self):

        print("Creating a thread")

        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.task)
        self.thread.start()

    def stop_thread(self):

        print("Sending stop signal to thread")
        self.worker.stop()
        self.thread.quit()
        self.thread.wait()
