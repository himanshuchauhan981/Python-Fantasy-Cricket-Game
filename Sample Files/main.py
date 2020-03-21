from CreateTeam import Ui_New_MainWindow as createTeam
from OpenTeam import Ui_Open_MainWindow as openTeam
from EvaluateTeam import Ui_Evaluate_MainWindow as evaluateTeam
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
conn = sqlite3.connect('match.db')
cur = conn.cursor()


class Ui_MainWindow(object):
    def __init__(self):
        self.max_WK = 1
        self.create_team = QtWidgets.QMainWindow()
        self.create_screen = createTeam()
        self.create_screen.setupUi(self.create_team)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 190, 581, 261))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.list1.setObjectName("list1")
        self.horizontalLayout_2.addWidget(self.list1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.list2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.list2.setObjectName("list2")
        self.horizontalLayout_2.addWidget(self.list2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 571, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Bat = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Bat.setObjectName("Bat")
        self.Bat.setEnabled(False)
        self.horizontalLayout.addWidget(self.Bat)
        self.Bowl = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Bowl.setObjectName("Bowl")
        self.Bowl.setEnabled(False)
        self.horizontalLayout.addWidget(self.Bowl)
        self.All = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.All.setObjectName("All")
        self.All.setEnabled(False)
        self.horizontalLayout.addWidget(self.All)
        self.WK = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.WK.setObjectName("WK")
        self.WK.setEnabled(False)
        self.horizontalLayout.addWidget(self.WK)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 571, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Batsman_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Batsman_1.setObjectName("Batsman_1")
        self.horizontalLayout_3.addWidget(self.Batsman_1)
        self.Batsman_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Batsman_2.setObjectName("Batsman_2")
        self.horizontalLayout_3.addWidget(self.Batsman_2)
        self.Bowlers_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Bowlers_1.setObjectName("Bowlers_1")
        self.horizontalLayout_3.addWidget(self.Bowlers_1)
        self.Bowlers_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Bowlers_2.setObjectName("Bowlers_2")
        self.horizontalLayout_3.addWidget(self.Bowlers_2)
        self.Allrounders_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Allrounders_1.setObjectName("Allrounders_1")
        self.horizontalLayout_3.addWidget(self.Allrounders_1)
        self.Allrounders_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Allrounders_2.setObjectName("Allrounders_2")
        self.horizontalLayout_3.addWidget(self.Allrounders_2)
        self.Wicketkeeper_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Wicketkeeper_1.setObjectName("Wicketkeeper_1")
        self.horizontalLayout_3.addWidget(self.Wicketkeeper_1)
        self.Wicketkeeper_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Wicketkeeper_2.setObjectName("Wicketkeeper_2")
        self.horizontalLayout_3.addWidget(self.Wicketkeeper_2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 150, 571, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pointAvailableText = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.pointAvailableText.setObjectName("pointAvailableText")
        self.horizontalLayout_4.addWidget(self.pointAvailableText)
        self.pointAvailableBox = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.pointAvailableBox.setObjectName("pointAvailableBox")
        self.horizontalLayout_4.addWidget(self.pointAvailableBox)
        self.teamNameText = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.teamNameText.setObjectName("teamNameText")
        self.horizontalLayout_4.addWidget(self.teamNameText)
        self.teamNameBox = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.teamNameBox.setObjectName("teamNameBox")
        self.horizontalLayout_4.addWidget(self.teamNameBox)
        self.pointUsedText = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.pointUsedText.setObjectName("pointUsedText")
        self.horizontalLayout_4.addWidget(self.pointUsedText)
        self.pointUsedBox = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.pointUsedBox.setObjectName("pointUsedBox")
        self.horizontalLayout_4.addWidget(self.pointUsedBox)
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.Allrounders_1.raise_()
        self.horizontalLayoutWidget_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.CREATE = QtWidgets.QAction(MainWindow)
        self.CREATE.setObjectName("CREATE")
        self.OPEN = QtWidgets.QAction(MainWindow)
        self.OPEN.setObjectName("OPEN")
        self.SAVE = QtWidgets.QAction(MainWindow)
        self.SAVE.setObjectName("SAVE")
        self.EVALUATE = QtWidgets.QAction(MainWindow)
        self.EVALUATE.setObjectName("EVALUATE")
        self.menuManage_Teams.addAction(self.CREATE)
        self.menuManage_Teams.addAction(self.OPEN)
        self.menuManage_Teams.addAction(self.SAVE)
        self.menuManage_Teams.addAction(self.EVALUATE)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.create_screen.pushButton.clicked.connect(self.show_teamName)
        self.Bat.clicked.connect(self.show_names)
        self.Bowl.clicked.connect(self.show_names)
        self.WK.clicked.connect(self.show_names)
        self.All.clicked.connect(self.show_names)
        self.list1.doubleClicked.connect(self.take_names)
        self.list2.doubleClicked.connect(self.remove_names)
        self.CREATE.triggered.connect(self.create_teams)
        self.SAVE.triggered.connect(self.save_teams)
        self.OPEN.triggered.connect(self.open_teams)
        self.EVALUATE.triggered.connect(self.evaluate_teams)

    def show_names(self):
        if self.Bat.isChecked():
            self.list1.clear()
            cur.execute('SELECT Player FROM player_data WHERE type = "Batsman"')
            bats_data = cur.fetchall()

            for data in bats_data:
                self.list1.addItem(data[0])
        if self.Bowl.isChecked():
            self.list1.clear()
            cur.execute('SELECT Player fROM player_data WHERE type = "Bowler"')
            bowl_data = cur.fetchall()
            for data in bowl_data:
                self.list1.addItem(data[0])
        if self.WK.isChecked():
            self.list1.clear()
            cur.execute('SELECT Player FROM player_data WHERE type = "WicketKeeper"')
            WK_data = cur.fetchall()
            for data in WK_data:
                self.list1.addItem(data[0])
        if self.All.isChecked():
            self.list1.clear()
            cur.execute('SELECT Player FROM player_data WHERE type ="Allrounder"')
            all_data = cur.fetchall()
            for data in all_data:
                self.list1.addItem(data[0])

    def show_points(self):
        cur.execute('SELECT SUM(Points) from player_data')
        points = cur.fetchall()
        self.pointAvailableBox.setText(str(points[0][0]))

    def take_names(self):
        if self.WK.isChecked() and self.max_WK is not 0 or self.Bat.isChecked() or self.Bowl.isChecked() or self.All.isChecked():
            item = self.list1.takeItem(self.list1.currentRow())
            self.list2.addItem(item)
            item = item.text()
            cur.execute("SELECT Points FROM player_data WHERE Player = '" + item + "';")
            play_pt = cur.fetchall()
            actual_pt = self.pointAvailableBox.text()
            actual_pt = int(actual_pt) - int(play_pt[0][0])
            self.pointAvailableBox.setText(str(actual_pt))
            added_pt = self.pointUsedBox.text()
            add_pt = int(added_pt) + int(play_pt[0][0])
            self.pointUsedBox.setText(str(add_pt))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("You cannot select more than one wicketkeeper")
            msg.exec_()

        if self.Bat.isChecked():
            bat_count = self.Batsman_2.text()
            bat_count = int(bat_count)-1
            self.Batsman_2.setText(str(bat_count))
        elif self.Bowl.isChecked():
            bowl_count = self.Bowlers_2.text()
            bowl_count = int(bowl_count)-1
            self.Bowlers_2.setText(str(bowl_count))
        elif self.WK.isChecked() and self.max_WK is not 0:
            self.max_WK = self.max_WK - 1
            WK_count = self.Wicketkeeper_2.text()
            WK_count = int(WK_count)-1
            self.Wicketkeeper_2.setText(str(WK_count))
        else:
            All_count = self.Allrounders_2.text()
            All_count = int(All_count)-1
            self.Allrounders_2.setText(str(All_count))


    def remove_names(self):
        item = self.list2.takeItem(self.list2.currentRow())
        cur.execute("SELECT type FROM player_data WHERE Player = '" + item.text() + "';")
        type_data = cur.fetchall()
        if self.Bat.isChecked() and type_data[0][0] == 'Batsman':
            self.list1.addItem(item)
        elif self.Bowl.isChecked() and type_data[0][0] == 'Bowler':
            self.list1.addItem(item)
        elif self.WK.isChecked() and type_data[0][0] == 'WicketKeeper':
            self.list1.addItem(item)
        elif self.All.isChecked() and type_data[0][0] == 'Allrounder':
            self.list1.addItem(item)
        item = item.text()
        cur.execute("SELECT Points FROM player_data WHERE Player = '" + item + "';")
        play_pt = cur.fetchall()
        actual_pt = self.pointUsedBox.text()
        actual_pt = int(actual_pt) - int(play_pt[0][0])
        self.pointUsedBox.setText(str(actual_pt))
        added_pt = self.pointAvailableBox.text()
        add_pt = int(added_pt) + int(play_pt[0][0])
        self.pointAvailableBox.setText(str(add_pt))

    def create_teams(self):
        self.create_team.show()

    def open_teams(self):
        self.open_team = QtWidgets.QMainWindow()
        self.open_screen = openTeam()
        self.open_screen.setupUi(self.open_team)
        self.open_team.show()

    def evaluate_teams(self):
        self.evaluate_team = QtWidgets.QMainWindow()
        self.evaluate_screen = evaluateTeam()
        self.evaluate_screen.setupUi(self.evaluate_team)
        self.evaluate_team.show()

    def show_teamName(self):
        self.Bat.setEnabled(True)
        self.Bowl.setEnabled(True)
        self.WK.setEnabled(True)
        self.All.setEnabled(True)
        cur.execute('SELECT SUM(Points) from player_data')
        points = cur.fetchall()
        self.pointAvailableBox.setText(str(points[0][0]))
        self.pointUsedBox.setText(str('0'))
        cur.execute('SELECT count(Player) FROM player_data WHERE type ="Batsman"')
        bats_count = cur.fetchone()
        self.Batsman_2.setText(str(bats_count[0]))
        cur.execute('SELECT count(Player) FROM player_data WHERE type ="Bowler"')
        bowl_count = cur.fetchone()
        self.Bowlers_2.setText(str(bowl_count[0]))
        cur.execute('SELECT count(Player) FROM player_data WHERE type ="WicketKeeper"')
        wicket_count = cur.fetchone()
        self.Wicketkeeper_2.setText(str(wicket_count[0]))
        cur.execute('SELECT count(Player) FROM player_data WHERE type ="Allrounder"')
        all_count = cur.fetchone()
        self.Allrounders_2.setText(str(all_count[0]))
        teamName = self.create_screen.lineEdit.text()
        self.teamNameBox.setText(str(teamName))

    def save_teams(self):
        team_list = []
        team_name = self.teamNameBox.text()
        cur.execute("SELECT Matches FROM team WHERE Name='" + team_name + "'")
        data = cur.fetchall()
        if len(data) is not 0:
            match = data[len(data)-1][0]
            a = match.split(match[len(match)-1])
            b = match.split('Matches')
            b[1] = int(b[1])+1
            matches = a[0]+str(b[1])
        else:
            matches = 'Matches1'
        for item in range(self.list2.count()):
            team_list.append(self.list2.item(item).text())
        for item in team_list:
            cur.execute("SELECT Points FROM player_data WHERE Player = '" + item + "';")
            player_pt = cur.fetchall()
            cur.execute('INSERT INTO Team VALUES (?,?,?,?)', (team_name, item, player_pt[0][0], matches))
            conn.commit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Bat.setText(_translate("MainWindow", "Bat"))
        self.Bowl.setText(_translate("MainWindow", "Bowl"))
        self.All.setText(_translate("MainWindow", "All"))
        self.WK.setText(_translate("MainWindow", "WK"))
        self.Batsman_1.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.Batsman_2.setText(_translate("MainWindow", "##"))
        self.Bowlers_1.setText(_translate("MainWindow", "Bowlers (BOWL)"))
        self.Bowlers_2.setText(_translate("MainWindow", "##"))
        self.Allrounders_1.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.Allrounders_2.setText(_translate("MainWindow", "##"))
        self.Wicketkeeper_1.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.Wicketkeeper_2.setText(_translate("MainWindow", "##"))
        self.pointAvailableText.setText(_translate("MainWindow", "Point Available"))
        self.pointAvailableBox.setText(_translate("MainWindow", "##"))
        self.teamNameText.setText(_translate("MainWindow", "Team Name - "))
        self.teamNameBox.setText(_translate("MainWindow", "##"))
        self.pointUsedText.setText(_translate("MainWindow", "Point Used "))
        self.pointUsedBox.setText(_translate("MainWindow", "##"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.CREATE.setText(_translate("MainWindow", "CREATE Teams"))
        self.OPEN.setText(_translate("MainWindow", "OPEN Teams"))
        self.SAVE.setText(_translate("MainWindow", "SAVE Teams"))
        self.EVALUATE.setText(_translate("MainWindow", "EVALUATE Teams"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

