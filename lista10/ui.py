# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(324, 244)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check_dodaj = QtWidgets.QRadioButton(self.centralwidget)
        self.check_dodaj.setGeometry(QtCore.QRect(10, 140, 82, 17))
        self.check_dodaj.setObjectName("check_dodaj")
        self.check_odejmij = QtWidgets.QRadioButton(self.centralwidget)
        self.check_odejmij.setGeometry(QtCore.QRect(90, 140, 82, 17))
        self.check_odejmij.setObjectName("check_odejmij")
        self.check_mnoz = QtWidgets.QRadioButton(self.centralwidget)
        self.check_mnoz.setGeometry(QtCore.QRect(180, 140, 82, 17))
        self.check_mnoz.setObjectName("check_mnoz")
        self.check_dziel = QtWidgets.QRadioButton(self.centralwidget)
        self.check_dziel.setEnabled(True)
        self.check_dziel.setGeometry(QtCore.QRect(250, 140, 82, 17))
        self.check_dziel.setObjectName("check_dziel")
        self.doCalc = QtWidgets.QPushButton(self.centralwidget)
        self.doCalc.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.doCalc.setObjectName("doCalc")
        self.doClean = QtWidgets.QPushButton(self.centralwidget)
        self.doClean.setGeometry(QtCore.QRect(90, 170, 75, 23))
        self.doClean.setObjectName("doClean")
        self.input_a = QtWidgets.QLineEdit(self.centralwidget)
        self.input_a.setGeometry(QtCore.QRect(10, 30, 91, 20))
        self.input_a.setObjectName("input_a")
        self.input_b = QtWidgets.QLineEdit(self.centralwidget)
        self.input_b.setGeometry(QtCore.QRect(10, 70, 91, 20))
        self.input_b.setObjectName("input_b")
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(10, 110, 91, 20))
        self.output.setText("")
        self.output.setObjectName("output")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 324, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kalkulator"))
        self.check_dodaj.setText(_translate("MainWindow", "Dodawanie"))
        self.check_odejmij.setText(_translate("MainWindow", "Odejmowanie"))
        self.check_mnoz.setText(_translate("MainWindow", "Mnożenie"))
        self.check_dziel.setText(_translate("MainWindow", "Dzielenie"))
        self.doCalc.setText(_translate("MainWindow", "Wykonaj!"))
        self.doClean.setText(_translate("MainWindow", "Wyczyść"))
        self.label.setText(_translate("MainWindow", "Liczba a"))
        self.label_2.setText(_translate("MainWindow", "Liczba b"))
        self.label_3.setText(_translate("MainWindow", "Wynik"))
