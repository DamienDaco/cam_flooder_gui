from app.multithreading import *


class Logic:
    def __init__(self, slider_value):
        super().__init__()
        print("Logic has been initialized")
        self.threads = []                   # List for storing multiple threads
        self.worker_id = 0
        self.slider_value = slider_value

    def start_thread(self):

        self.thread = MultiThreading(self.worker_id, self.slider_value)
        self.thread.create_thread()
        self.threads.append(self.thread)    # Store the thread in a list for later usage
        self.worker_id += 1

    def stop_thread(self):

        if len(self.threads) > 0:               # Check if there's something in the list
            for thread in self.threads:         # Let's go through the list of threads
                thread.stop_thread()            # And send the stop signal to each thread

        self.threads = []                       # When done, reset list

    def slider_value_changed(self, slider_value):
        self.slider_value = slider_value
        if len(self.threads) > 0:
            print(self.threads)
            for thread, worker in self.threads:
                worker.change_worker_rate(self.slider_value)
