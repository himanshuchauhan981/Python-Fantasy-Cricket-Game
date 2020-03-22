from PyQt5 import QtCore, QtGui, QtWidgets


class New_Ui_MainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.teamLabel = QtWidgets.QLabel(self.centralwidget)
        self.teamLabel.setGeometry(QtCore.QRect(120, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.teamLabel.setFont(font)
        self.teamLabel.setObjectName("teamLabel")
        self.teamName = QtWidgets.QLineEdit(self.centralwidget)
        self.teamName.setGeometry(QtCore.QRect(100, 130, 191, 31))
        self.teamName.setObjectName("teamName")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(130, 190, 111, 41))
        self.submitButton.setObjectName("submitButton")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.teamLabel.setText(_translate("MainWindow", "Enter team Name"))
        self.submitButton.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = New_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

