from PyQt5.QtCore import *
from app.work import *


class Worker(QObject):

    def __init__(self, rate, identity, selected_interface):

        super().__init__()

        self.is_running = True
        self.rate = rate
        self.identity = identity
        thread = QThread.currentThread()
        thread_id = int(QThread.currentThreadId())
        self.cam_flood_attack = CamFloodAttack(selected_interface)
        print("Hi! I'm your friendly worker %d and I'm being initialized." % self.identity)
        print("My current thread is %s and my thread ID is %s" % (thread, thread_id))

    def task(self):
        index = 0
        while self.is_running:
            self.cam_flood_attack.cam_flooder_random(self.identity, index, self.rate)
            index += 1

    def change_worker_rate(self, rate):
        self.rate = rate

    def stop(self):

        self.is_running = False


class MultiThreading(QThread):

    def __init__(self, rate, identity, selected_interface):
        super().__init__()
        self.rate = rate
        self.identity = identity
        self.threads = []
        self.selected_interface = selected_interface

    def start_thread(self):

        self.__worker = Worker(self.rate, self.identity, self.selected_interface)
        self.__thread = QThread()
        self.threads.append((self.__worker, self.__thread))
        self.__worker.moveToThread(self.__thread)
        self.__thread.started.connect(self.__worker.task)
        self.__thread.start()

    def stop_thread(self):

        if len(self.threads) > 0:                       # Check if there's something in the list
            print("Sending stop signal to thread")
            for worker, thread in self.threads:         # Let's go through the list of threads
                worker.stop()                           # And send the stop signal to each worker/thread
                thread.quit()
                thread.wait()

        self.threads = []                               # When done, reset list

    def slider_value_changed(self, slider_value):
        if len(self.threads) > 0:
            print("Sending new slider value to threads")
            for worker, thread in self.threads:
                worker.rate = slider_value

    def change_worker_rate(self, rate):
        if len(self.threads) > 0:
            for worker in self.threads:
                worker.change_worker_rate(rate)