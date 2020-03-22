from PyQt5 import QtCore, QtGui, QtWidgets


class Open_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openLabel = QtWidgets.QLabel(self.centralwidget)
        self.openLabel.setGeometry(QtCore.QRect(80, 100, 260, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.openLabel.setFont(font)
        self.openLabel.setObjectName("openLabel")
        self.openInput = QtWidgets.QLineEdit(self.centralwidget)
        self.openInput.setGeometry(QtCore.QRect(120, 150, 171, 20))
        self.openInput.setObjectName("openInput")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(160, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openLabel.setText(_translate("MainWindow", "Enter Team Name to Open"))
        self.openButton.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Open_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

