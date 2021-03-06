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
        self.interface_box.addItems(get_interfaces())
        self.selected_interface = str(self.interface_box.currentText())
        print("Selected interface is %s " % self.selected_interface)
        self.logic = Logic(1.0 / float(self.slider_value), self.selected_interface)

        self.start_button.clicked.connect(self.logic.start_thread)
        self.stop_button.clicked.connect(self.logic.stop_thread)

        self.rate_slider.valueChanged.connect(self.logic.slider_value_changed)
        self.interface_box.currentIndexChanged.connect(self.get_current_interface)

    def get_current_interface(self):
        interface = str(self.interface_box.currentText())
        print("Selected interface: %s " % interface)
        self.logic.selected_interface = interface
        return interface


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())