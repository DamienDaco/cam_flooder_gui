try:
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except:
    print("[-] Import failed. PyQt5 library not found. \nTry installing it with: apt install python3-qt5")
    exit()
from ui.design_cam_flooder_gui import Ui_MainWindow
from app.logic import *
import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.slider_value = self.rate_slider.value()
        print("Slider value is %d" % self.slider_value)
        self.logic = Logic(self.slider_value)
        self.__id = int(QThread.currentThreadId())
        print("Main thread id is %s" % self.__id)

        self.start_button.clicked.connect(self.logic.start_thread)
        self.stop_button.clicked.connect(self.logic.stop_thread)


        self.rate_slider.valueChanged.connect(self.slider_value_changed)

    def slider_value_changed(self):
        self.slider_value = self.rate_slider.value()
        print("New slider value is %d" % self.slider_value)
        self.logic.slider_value_changed(self.slider_value)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())