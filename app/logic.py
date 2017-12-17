from app.multithreading import *


class Logic:
    def __init__(self):
        super().__init__()
        print("Logic has been initialized")
        self.threads = []

    def start_thread(self):

        self.thread = MultiThreading()
        self.thread.create_thread()
        self.threads.append(self.thread)

    def stop_thread(self):

        for thread in self.threads:
            thread.stop_thread()
            