from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Score_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.score_box = QtWidgets.QLineEdit(self.centralwidget)
        self.score_box.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.score_box.setObjectName("score_box")
        self.score_text = QtWidgets.QLabel(self.centralwidget)
        self.score_text.setGeometry(QtCore.QRect(120, 100, 150, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.score_text.setFont(font)
        self.score_text.setObjectName("score_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
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
        self.score_text.setText(_translate("MainWindow", "Your Team Score : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Score_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

