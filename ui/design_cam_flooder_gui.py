# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_cam_flooder_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(205, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 4, 0, 1, 1)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 4, 1, 1, 1)
        self.rate_label = QtWidgets.QLabel(self.centralwidget)
        self.rate_label.setObjectName("rate_label")
        self.gridLayout.addWidget(self.rate_label, 2, 0, 1, 1)
        self.rate_slider = QtWidgets.QSlider(self.centralwidget)
        self.rate_slider.setMinimum(1)
        self.rate_slider.setMaximum(999)
        self.rate_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rate_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.rate_slider.setObjectName("rate_slider")
        self.gridLayout.addWidget(self.rate_slider, 3, 0, 1, 2)
        self.lcd_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_number.setObjectName("lcd_number")
        self.gridLayout.addWidget(self.lcd_number, 1, 1, 1, 1)
        self.interface_box = QtWidgets.QComboBox(self.centralwidget)
        self.interface_box.setObjectName("interface_box")
        self.gridLayout.addWidget(self.interface_box, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 205, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.rate_label.setBuddy(self.rate_slider)

        self.retranslateUi(MainWindow)
        self.rate_slider.sliderMoved['int'].connect(self.lcd_number.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cam Flooder"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.rate_label.setText(_translate("MainWindow", "Rate"))

