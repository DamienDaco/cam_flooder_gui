from app.multithreading import *
from app.network_functions import *


class Logic:

    def __init__(self, slider_value):
        super().__init__()
        print("Logic has been initialized")
        self.threads = []                   # List for storing multiple threads
        self.identities = 0                # List of workers identities (numbers)
        self.slider_value = slider_value
        self.interfaces = get_interfaces()

    def start_thread(self):

        thread = MultiThreading(self.slider_value, self.identities)
        thread.start_thread()
        self.threads.append(thread)
        self.identities += 1

    def stop_thread(self):

        if len(self.threads) > 0:               # Check if there's something in the list
            for thread in self.threads:         # Let's go through the list of threads
                thread.stop_thread()            # And send the stop signal to each thread

        self.threads = []                       # When done, reset list
        self.identities = 0

    def slider_value_changed(self, slider_value):

        self.slider_value = 1.0 / float(slider_value)
        print("New slider value is %f" % self.slider_value)
        if len(self.threads) > 0:
            for thread in self.threads:
                thread.slider_value_changed(self.slider_value)