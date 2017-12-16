from design_cam_flooder_gui import Ui_MainWindow


try:
    from PyQt5.QtCore import *
    # from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
except:
    print("[-] Import failed. PyQt5 library not found. \nTry installing it with: apt install python3-qt5")
    exit()

import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())