from PyQt5.QtCore import *
import time


class Worker(QObject):

    def __init__(self):

        super().__init__()

        self.is_running = True
        print("Hi! I'm your friendly worker and I'm being initialized")

    def task(self):

        while self.is_running:
            print("I'm your worker and I'm running your task")
            time.sleep(1)

    def stop(self):

        self.is_running = False

class MultiThreading(QThread):
    def __init__(self):
        super().__init__()

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
