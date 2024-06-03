# Form implementation generated from reading ui file 'battle_qt.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fondo = QtWidgets.QLabel(parent=self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.fondo.setText("")
        self.fondo.setPixmap(QtGui.QPixmap("img/wallpaperflare.com_wallpaper.jpg"))
        self.fondo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fondo.setObjectName("fondo")
        self.rondas = QtWidgets.QLabel(parent=self.centralwidget)
        self.rondas.setGeometry(QtCore.QRect(500, 0, 200, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(36)
        self.rondas.setFont(font)
        self.rondas.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n")
        self.rondas.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.rondas.setObjectName("rondas")
        self.n_rondas = QtWidgets.QLabel(parent=self.centralwidget)
        self.n_rondas.setGeometry(QtCore.QRect(550, 55, 100, 70))
        font = QtGui.QFont()
        font.setFamily("Frozen Crystal Bold")
        font.setPointSize(36)
        self.n_rondas.setFont(font)
        self.n_rondas.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_rondas.setObjectName("n_rondas")
        self.turno = QtWidgets.QLabel(parent=self.centralwidget)
        self.turno.setGeometry(QtCore.QRect(790, 30, 361, 61))
        font = QtGui.QFont()
        font.setFamily("VCR OSD Mono")
        font.setPointSize(24)
        self.turno.setFont(font)
        self.turno.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.turno.setObjectName("turno")
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(400, 650, 400, 190))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.orden = QtWidgets.QPushButton(parent=self.splitter)
        self.orden.setObjectName("orden")
        self.jugar = QtWidgets.QPushButton(parent=self.splitter)
        self.jugar.setObjectName("jugar")
        self.explosion = QtWidgets.QPushButton(parent=self.splitter)
        self.explosion.setObjectName("explosion")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(630, 130, 571, 451))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.C1_b = QtWidgets.QPushButton(parent=self.widget)
        self.C1_b.setObjectName("C1_b")
        self.gridLayout_3.addWidget(self.C1_b, 0, 2, 1, 1)
        self.E3_b = QtWidgets.QPushButton(parent=self.widget)
        self.E3_b.setObjectName("E3_b")
        self.gridLayout_3.addWidget(self.E3_b, 2, 4, 1, 1)
        self.A3_b = QtWidgets.QPushButton(parent=self.widget)
        self.A3_b.setObjectName("A3_b")
        self.gridLayout_3.addWidget(self.A3_b, 2, 0, 1, 1)
        self.D2_b = QtWidgets.QPushButton(parent=self.widget)
        self.D2_b.setObjectName("D2_b")
        self.gridLayout_3.addWidget(self.D2_b, 1, 3, 1, 1)
        self.B3_b = QtWidgets.QPushButton(parent=self.widget)
        self.B3_b.setObjectName("B3_b")
        self.gridLayout_3.addWidget(self.B3_b, 2, 1, 1, 1)
        self.D5_b = QtWidgets.QPushButton(parent=self.widget)
        self.D5_b.setObjectName("D5_b")
        self.gridLayout_3.addWidget(self.D5_b, 4, 3, 1, 1)
        self.E1_b = QtWidgets.QPushButton(parent=self.widget)
        self.E1_b.setObjectName("E1_b")
        self.gridLayout_3.addWidget(self.E1_b, 0, 4, 1, 1)
        self.A1_b = QtWidgets.QPushButton(parent=self.widget)
        self.A1_b.setObjectName("A1_b")
        self.gridLayout_3.addWidget(self.A1_b, 0, 0, 1, 1)
        self.D3_b = QtWidgets.QPushButton(parent=self.widget)
        self.D3_b.setObjectName("D3_b")
        self.gridLayout_3.addWidget(self.D3_b, 2, 3, 1, 1)
        self.E2_b = QtWidgets.QPushButton(parent=self.widget)
        self.E2_b.setObjectName("E2_b")
        self.gridLayout_3.addWidget(self.E2_b, 1, 4, 1, 1)
        self.B5_b = QtWidgets.QPushButton(parent=self.widget)
        self.B5_b.setObjectName("B5_b")
        self.gridLayout_3.addWidget(self.B5_b, 4, 1, 1, 1)
        self.B4_b = QtWidgets.QPushButton(parent=self.widget)
        self.B4_b.setObjectName("B4_b")
        self.gridLayout_3.addWidget(self.B4_b, 3, 1, 1, 1)
        self.E4_b = QtWidgets.QPushButton(parent=self.widget)
        self.E4_b.setObjectName("E4_b")
        self.gridLayout_3.addWidget(self.E4_b, 3, 4, 1, 1)
        self.C3_b = QtWidgets.QPushButton(parent=self.widget)
        self.C3_b.setObjectName("C3_b")
        self.gridLayout_3.addWidget(self.C3_b, 2, 2, 1, 1)
        self.A2_b = QtWidgets.QPushButton(parent=self.widget)
        self.A2_b.setIconSize(QtCore.QSize(20, 20))
        self.A2_b.setObjectName("A2_b")
        self.gridLayout_3.addWidget(self.A2_b, 1, 0, 1, 1)
        self.B1_b = QtWidgets.QPushButton(parent=self.widget)
        self.B1_b.setObjectName("B1_b")
        self.gridLayout_3.addWidget(self.B1_b, 0, 1, 1, 1)
        self.C5_b = QtWidgets.QPushButton(parent=self.widget)
        self.C5_b.setObjectName("C5_b")
        self.gridLayout_3.addWidget(self.C5_b, 4, 2, 1, 1)
        self.D1_b = QtWidgets.QPushButton(parent=self.widget)
        self.D1_b.setObjectName("D1_b")
        self.gridLayout_3.addWidget(self.D1_b, 0, 3, 1, 1)
        self.C4_b = QtWidgets.QPushButton(parent=self.widget)
        self.C4_b.setObjectName("C4_b")
        self.gridLayout_3.addWidget(self.C4_b, 3, 2, 1, 1)
        self.B2_b = QtWidgets.QPushButton(parent=self.widget)
        self.B2_b.setObjectName("B2_b")
        self.gridLayout_3.addWidget(self.B2_b, 1, 1, 1, 1)
        self.D4_b = QtWidgets.QPushButton(parent=self.widget)
        self.D4_b.setObjectName("D4_b")
        self.gridLayout_3.addWidget(self.D4_b, 3, 3, 1, 1)
        self.C2_b = QtWidgets.QPushButton(parent=self.widget)
        self.C2_b.setObjectName("C2_b")
        self.gridLayout_3.addWidget(self.C2_b, 1, 2, 1, 1)
        self.A5_b = QtWidgets.QPushButton(parent=self.widget)
        self.A5_b.setObjectName("A5_b")
        self.gridLayout_3.addWidget(self.A5_b, 4, 0, 1, 1)
        self.E5_b = QtWidgets.QPushButton(parent=self.widget)
        self.E5_b.setObjectName("E5_b")
        self.gridLayout_3.addWidget(self.E5_b, 4, 4, 1, 1)
        self.A4_b = QtWidgets.QPushButton(parent=self.widget)
        self.A4_b.setObjectName("A4_b")
        self.gridLayout_3.addWidget(self.A4_b, 3, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 130, 571, 451))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.E1 = QtWidgets.QLabel(parent=self.widget1)
        self.E1.setObjectName("E1")
        self.gridLayout_2.addWidget(self.E1, 0, 4, 1, 1)
        self.B3 = QtWidgets.QLabel(parent=self.widget1)
        self.B3.setObjectName("B3")
        self.gridLayout_2.addWidget(self.B3, 2, 1, 1, 1)
        self.E3 = QtWidgets.QLabel(parent=self.widget1)
        self.E3.setObjectName("E3")
        self.gridLayout_2.addWidget(self.E3, 2, 4, 1, 1)
        self.D4 = QtWidgets.QLabel(parent=self.widget1)
        self.D4.setObjectName("D4")
        self.gridLayout_2.addWidget(self.D4, 3, 3, 1, 1)
        self.B5 = QtWidgets.QLabel(parent=self.widget1)
        self.B5.setObjectName("B5")
        self.gridLayout_2.addWidget(self.B5, 4, 1, 1, 1)
        self.E5 = QtWidgets.QLabel(parent=self.widget1)
        self.E5.setObjectName("E5")
        self.gridLayout_2.addWidget(self.E5, 4, 4, 1, 1)
        self.A5 = QtWidgets.QLabel(parent=self.widget1)
        self.A5.setObjectName("A5")
        self.gridLayout_2.addWidget(self.A5, 4, 0, 1, 1)
        self.C2 = QtWidgets.QLabel(parent=self.widget1)
        self.C2.setObjectName("C2")
        self.gridLayout_2.addWidget(self.C2, 1, 2, 1, 1)
        self.A1 = QtWidgets.QLabel(parent=self.widget1)
        self.A1.setObjectName("A1")
        self.gridLayout_2.addWidget(self.A1, 0, 0, 1, 1)
        self.E4 = QtWidgets.QLabel(parent=self.widget1)
        self.E4.setObjectName("E4")
        self.gridLayout_2.addWidget(self.E4, 3, 4, 1, 1)
        self.A2 = QtWidgets.QLabel(parent=self.widget1)
        self.A2.setObjectName("A2")
        self.gridLayout_2.addWidget(self.A2, 1, 0, 1, 1)
        self.C5 = QtWidgets.QLabel(parent=self.widget1)
        self.C5.setObjectName("C5")
        self.gridLayout_2.addWidget(self.C5, 4, 2, 1, 1)
        self.D3 = QtWidgets.QLabel(parent=self.widget1)
        self.D3.setObjectName("D3")
        self.gridLayout_2.addWidget(self.D3, 2, 3, 1, 1)
        self.A3 = QtWidgets.QLabel(parent=self.widget1)
        self.A3.setObjectName("A3")
        self.gridLayout_2.addWidget(self.A3, 2, 0, 1, 1)
        self.A4 = QtWidgets.QLabel(parent=self.widget1)
        self.A4.setObjectName("A4")
        self.gridLayout_2.addWidget(self.A4, 3, 0, 1, 1)
        self.B1 = QtWidgets.QLabel(parent=self.widget1)
        self.B1.setObjectName("B1")
        self.gridLayout_2.addWidget(self.B1, 0, 1, 1, 1)
        self.E2 = QtWidgets.QLabel(parent=self.widget1)
        self.E2.setObjectName("E2")
        self.gridLayout_2.addWidget(self.E2, 1, 4, 1, 1)
        self.B4 = QtWidgets.QLabel(parent=self.widget1)
        self.B4.setObjectName("B4")
        self.gridLayout_2.addWidget(self.B4, 3, 1, 1, 1)
        self.D1 = QtWidgets.QLabel(parent=self.widget1)
        self.D1.setObjectName("D1")
        self.gridLayout_2.addWidget(self.D1, 0, 3, 1, 1)
        self.D5 = QtWidgets.QLabel(parent=self.widget1)
        self.D5.setObjectName("D5")
        self.gridLayout_2.addWidget(self.D5, 4, 3, 1, 1)
        self.B2 = QtWidgets.QLabel(parent=self.widget1)
        self.B2.setObjectName("B2")
        self.gridLayout_2.addWidget(self.B2, 1, 1, 1, 1)
        self.C4 = QtWidgets.QLabel(parent=self.widget1)
        self.C4.setObjectName("C4")
        self.gridLayout_2.addWidget(self.C4, 3, 2, 1, 1)
        self.C1 = QtWidgets.QLabel(parent=self.widget1)
        self.C1.setObjectName("C1")
        self.gridLayout_2.addWidget(self.C1, 0, 2, 1, 1)
        self.D2 = QtWidgets.QLabel(parent=self.widget1)
        self.D2.setObjectName("D2")
        self.gridLayout_2.addWidget(self.D2, 1, 3, 1, 1)
        self.C3 = QtWidgets.QLabel(parent=self.widget1)
        self.C3.setObjectName("C3")
        self.gridLayout_2.addWidget(self.C3, 2, 2, 1, 1)
        #self.fondo.raise_()
        self.A1.raise_()
        self.B1.raise_()
        self.D1.raise_()
        self.E1.raise_()
        self.E2.raise_()
        self.A2.raise_()
        self.C2.raise_()
        self.B2.raise_()
        self.D2.raise_()
        self.A3.raise_()
        self.B3.raise_()
        self.E3.raise_()
        self.C3.raise_()
        self.D3.raise_()
        self.A4.raise_()
        self.B4.raise_()
        self.E4.raise_()
        self.D5.raise_()
        self.A5.raise_()
        self.E5.raise_()
        self.C4.raise_()
        self.B5.raise_()
        self.C5.raise_()
        self.D4.raise_()
        self.A1_b.raise_()
        self.B1_b.raise_()
        self.C1_b.raise_()
        self.D1_b.raise_()
        self.E1_b.raise_()
        self.E2_b.raise_()
        self.A2_b.raise_()
        self.B2_b.raise_()
        self.C2_b.raise_()
        self.D2_b.raise_()
        self.E3_b.raise_()
        self.A4_b.raise_()
        self.A3_b.raise_()
        self.D4_b.raise_()
        self.B3_b.raise_()
        self.B4_b.raise_()
        self.C4_b.raise_()
        self.E4_b.raise_()
        self.C3_b.raise_()
        self.D3_b.raise_()
        self.A5_b.raise_()
        self.E5_b.raise_()
        self.C5_b.raise_()
        self.B5_b.raise_()
        self.D5_b.raise_()
        self.orden.raise_()
        self.jugar.raise_()
        self.explosion.raise_()
        self.rondas.raise_()
        self.n_rondas.raise_()
        self.turno.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1241, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rondas.setText(_translate("MainWindow", "Ronda"))
        self.n_rondas.setText(_translate("MainWindow", "0"))
        self.turno.setText(_translate("MainWindow", "Tu turno"))
        self.orden.setText(_translate("MainWindow", "Orden Aleatorio"))
        self.jugar.setText(_translate("MainWindow", "Jugar"))
        self.explosion.setText(_translate("MainWindow", "Explosión de Material"))
        self.C1_b.setText(_translate("MainWindow", "C1"))
        self.E3_b.setText(_translate("MainWindow", "E3"))
        self.A3_b.setText(_translate("MainWindow", "A3"))
        self.D2_b.setText(_translate("MainWindow", "D2"))
        self.B3_b.setText(_translate("MainWindow", "B3"))
        self.D5_b.setText(_translate("MainWindow", "D5"))
        self.E1_b.setText(_translate("MainWindow", "E1"))
        self.A1_b.setText(_translate("MainWindow", "A1"))
        self.D3_b.setText(_translate("MainWindow", "D3"))
        self.E2_b.setText(_translate("MainWindow", "E2"))
        self.B5_b.setText(_translate("MainWindow", "B5"))
        self.B4_b.setText(_translate("MainWindow", "B4"))
        self.E4_b.setText(_translate("MainWindow", "E4"))
        self.C3_b.setText(_translate("MainWindow", "C3"))
        self.A2_b.setText(_translate("MainWindow", "A2"))
        self.B1_b.setText(_translate("MainWindow", "B1"))
        self.C5_b.setText(_translate("MainWindow", "C5"))
        self.D1_b.setText(_translate("MainWindow", "D1"))
        self.C4_b.setText(_translate("MainWindow", "C4"))
        self.B2_b.setText(_translate("MainWindow", "B2"))
        self.D4_b.setText(_translate("MainWindow", "D4"))
        self.C2_b.setText(_translate("MainWindow", "C2"))
        self.A5_b.setText(_translate("MainWindow", "A5"))
        self.E5_b.setText(_translate("MainWindow", "E5"))
        self.A4_b.setText(_translate("MainWindow", "A4"))
        self.E1.setText(_translate("MainWindow", "TextLabel"))
        self.B3.setText(_translate("MainWindow", "TextLabel"))
        self.E3.setText(_translate("MainWindow", "TextLabel"))
        self.D4.setText(_translate("MainWindow", "TextLabel"))
        self.B5.setText(_translate("MainWindow", "TextLabel"))
        self.E5.setText(_translate("MainWindow", "TextLabel"))
        self.A5.setText(_translate("MainWindow", "TextLabel"))
        self.C2.setText(_translate("MainWindow", "TextLabel"))
        self.A1.setText(_translate("MainWindow", "TextLabel"))
        self.E4.setText(_translate("MainWindow", "TextLabel"))
        self.A2.setText(_translate("MainWindow", "TextLabel"))
        self.C5.setText(_translate("MainWindow", "TextLabel"))
        self.D3.setText(_translate("MainWindow", "TextLabel"))
        self.A3.setText(_translate("MainWindow", "TextLabel"))
        self.A4.setText(_translate("MainWindow", "TextLabel"))
        self.B1.setText(_translate("MainWindow", "TextLabel"))
        self.E2.setText(_translate("MainWindow", "TextLabel"))
        self.B4.setText(_translate("MainWindow", "TextLabel"))
        self.D1.setText(_translate("MainWindow", "TextLabel"))
        self.D5.setText(_translate("MainWindow", "TextLabel"))
        self.B2.setText(_translate("MainWindow", "TextLabel"))
        self.C4.setText(_translate("MainWindow", "TextLabel"))
        self.C1.setText(_translate("MainWindow", "TextLabel"))
        self.D2.setText(_translate("MainWindow", "TextLabel"))
        self.C3.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
