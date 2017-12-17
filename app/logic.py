from app.multithreading import *
#from ui.design_cam_flooder_gui import Ui_MainWindow


class Logic():
    def __init__(self):
        super().__init__()
        print("Logic has been initialized")

    def start_thread(self):

        self.thread = MultiThreading()
        self.thread.create_thread()

    def stop_thread(self):

        self.thread.stop_thread()