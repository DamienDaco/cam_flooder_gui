from app.multithreading import *


class Logic:
    def __init__(self):
        super().__init__()
        print("Logic has been initialized")
        self.threads = []                   # List for storing multiple threads

    def start_thread(self):

        self.thread = MultiThreading()
        self.thread.create_thread()
        self.threads.append(self.thread)    # Store the thread in a list for further use later

    def stop_thread(self):

        for thread in self.threads:         # Let's go through the list of threads
            thread.stop_thread()            # And send the stop signal to each thread
