from ui.design_cam_flooder_gui import Ui_MainWindow


try:
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except:
    print("[-] Import failed. PyQt5 library not found. \nTry installing it with: apt install python3-qt5")
    exit()

import sys
from app.logic import *


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.logic = Logic()
        self.__id = int(QThread.currentThreadId())
        print("Main thread id is %s" % self.__id)

        self.start_button.clicked.connect(self.logic.start_thread)
        self.stop_button.clicked.connect(self.logic.stop_thread)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())