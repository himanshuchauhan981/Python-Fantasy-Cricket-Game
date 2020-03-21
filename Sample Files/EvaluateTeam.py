from PyQt5 import QtCore, QtGui, QtWidgets
from ScoreTeam import Ui_Score_MainWindow as ScoresTeam
import sqlite3
conn = sqlite3.connect("match.db")
cur = conn.cursor()


class Ui_Evaluate_MainWindow(object):
    def __init__(self):
        self.score_team = QtWidgets.QMainWindow()
        self.score_screen = ScoresTeam()
        self.score_screen.setupUi(self.score_team)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 402)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 300, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.team_box = QtWidgets.QComboBox(self.centralwidget)
        self.team_box.setGeometry(QtCore.QRect(40, 50, 111, 31))
        self.team_box.setObjectName("team_box")
        self.match_box = QtWidgets.QComboBox(self.centralwidget)
        self.match_box.setGeometry(QtCore.QRect(240, 50, 111, 31))
        self.match_box.setObjectName("match_box")
        self.team_box.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 80, 361, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 140, 361, 191))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PlayerList = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.PlayerList.setObjectName("Player_List")
        self.horizontalLayout_2.addWidget(self.PlayerList)
        self.PointList = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.PointList.setObjectName("Point_List")
        self.horizontalLayout_2.addWidget(self.PointList)
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(150, 340, 75, 23))
        self.Calculate.setObjectName("Calculate")
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

        self.team_box.activated.connect(self.matchesShow)
        self.match_box.activated.connect(self.dataShow)
        self.Calculate.clicked.connect(self.calculateWindow)

        cur.execute("SELECT Name FROM Team")
        team_data = cur.fetchall()
        team_data = list(set(team_data))
        for data in team_data:
            self.team_box.addItem(data[0])

    def matchesShow(self):
        value = self.team_box.currentText()
        cur.execute("SELECT Matches FROM Team WHERE Name = '" + value + "'")
        play_match = cur.fetchall()
        play_match = list(set(play_match))
        play_match.sort()
        self.match_box.clear()
        for match in play_match:
            self.match_box.addItem(match[0])

    def dataShow(self):
        value = self.match_box.currentText()
        cur.execute("SELECT Players , Scores FROM Team WHERE Matches = '"+ value +"'")
        play_data = cur.fetchall()
        self.PlayerList.clear()
        self.PointList.clear()
        for data in play_data:
            self.PlayerList.addItem(data[0])
            self.PointList.addItem(str(data[1]))

    def calculateWindow(self):
        items = []
        for index in range(self.PointList.count()):
            item = self.PointList.item(index)
            items.append(int(item.text()))
        print(sum(items))
        self.score_screen.score_box.setText(str(sum(items)))
        self.score_team.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Evaluate the Performance of your Fantasy Team"))
        self.label_3.setText(_translate("MainWindow", "                       Players"))
        self.label_2.setText(_translate("MainWindow", "                        Points"))
        self.Calculate.setText(_translate("MainWindow", "Calculate"))
        self.team_box.setItemText(0, _translate('MainWindow', "Select Teams"))
        self.match_box.setItemText(0, _translate('MainWindow', "Select Matches"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Evaluate_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

